#!/usr/bin/env python3
"""Build an IRB submission .docx from the assembled protocol markdown.

The UMaine IRB returns applications that are not Word documents, and requires the
whole document to be page-numbered. This writes the same six-part OOXML package the
v5 submission used, including the `Page X of Y` footer field.

    python3 tools/build_docx.py source/protocol_v6_MERGED.md CURRENT/OUT.docx

Markdown supported is the subset the protocol sources actually use: three heading
levels, paragraphs, `- ` bullets, `> ` block quotes, and inline `**bold**` / `*italic*`.
"""

import re
import sys
import zipfile
from pathlib import Path

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'

# Paragraph shapes, keyed by block type. Values are (spacing-before, spacing-after,
# extra pPr XML). Taken from the v5 document so rebuilds stay visually identical.
SHAPES = {
    'h1': (0, 120, '<w:jc w:val="center"/>'),
    'h2': (240, 90, ''),
    'h3': (180, 70, ''),
    'p': (0, 80, ''),
    'bullet': (0, 80, '<w:ind w:left="720" w:hanging="360"/>'),
    'quote': (0, 80, '<w:ind w:left="360" w:hanging="0"/>'),
    'spacer': (0, 60, ''),
}

# Run properties applied to every run in a block, before inline markup.
RUN_STYLE = {
    'h1': '<w:b/><w:sz w:val="28"/>',
    'h2': '<w:b/><w:sz w:val="26"/>',
    'h3': '<w:b/><w:sz w:val="24"/>',
    'quote': '<w:i/>',
}

STYLES_XML = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    f'<w:styles {W}><w:docDefaults><w:rPrDefault><w:rPr>'
    '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
    '<w:sz w:val="22"/></w:rPr></w:rPrDefault></w:docDefaults>'
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>'
    '</w:style></w:styles>'
)

# `Page N of M` centred in the footer. This is what satisfies the board's
# "page number entire document" gate; do not drop it.
FOOTER_XML = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    f'<w:ftr {W}><w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
    '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t xml:space="preserve">Page </w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
    '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t xml:space="preserve"> of </w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:instrText xml:space="preserve"> NUMPAGES </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'
)

CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
    '</Types>'
)

ROOT_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    '</Relationships>'
)

DOC_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
    '</Relationships>'
)

SECT_PR = (
    '<w:sectPr><w:footerReference w:type="default" r:id="rId2"/>'
    '<w:pgSz w:w="12240" w:h="15840"/>'
    '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
    'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
)


def esc(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;')
                .replace('>', '&gt;').replace('"', '&quot;'))



# Text wrapped in {{...}} renders bold and red — used to show a reviewer what changed
# since the version they last read. Purely a review aid; strip before submitting.
MARK_STYLE = '<w:b/><w:color w:val="C00000"/>'


def runs(text, base_style=''):
    """Split inline {{changed}} / **bold** / *italic* into separate w:r elements."""
    out = []
    for part in re.split(r'(\{\{.+?\}\}|\*\*.+?\*\*|(?<!\*)\*[^*]+?\*(?!\*))', text):
        if not part:
            continue
        style = base_style
        if part.startswith('{{') and part.endswith('}}'):
            # A marked span may still carry **bold** inside it.
            inner = part[2:-2].replace('**', '')
            out.append(f'<w:r><w:rPr>{base_style}{MARK_STYLE}</w:rPr>'
                       f'<w:t xml:space="preserve">{esc(inner)}</w:t></w:r>')
            continue
        if part.startswith('**') and part.endswith('**'):
            part, style = part[2:-2], base_style + '<w:b/>'
        elif part.startswith('*') and part.endswith('*'):
            part, style = part[1:-1], base_style + '<w:i/>'
        rpr = f'<w:rPr>{style}</w:rPr>' if style else ''
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    return ''.join(out) or '<w:r><w:t/></w:r>'


def paragraph(kind, text=''):
    before, after, extra = SHAPES[kind]
    ppr = (f'<w:pPr><w:spacing w:before="{before}" w:after="{after}" '
           f'w:line="259" w:lineRule="auto"/>{extra}</w:pPr>')
    body = '<w:r><w:t/></w:r>' if kind == 'spacer' else runs(text, RUN_STYLE.get(kind, ''))
    return f'<w:p>{ppr}{body}</w:p>'


def classify(line):
    """Map one markdown line to (block kind, text)."""
    if line.startswith('### '):
        return 'h3', line[4:]
    if line.startswith('## '):
        return 'h2', line[3:]
    if line.startswith('# '):
        return 'h1', line[2:]
    if line.startswith('> '):
        return 'quote', line[2:]
    if re.match(r'^[-*] ', line):
        return 'bullet', '•\t' + line[2:]
    return 'p', line


def build_document(markdown):
    paragraphs = []
    for raw in markdown.split('\n'):
        line = raw.rstrip()
        if not line.strip():
            # Each blank markdown line becomes a short spacer paragraph. Runs of two
            # are how the sources put extra air before an appendix heading, so they
            # are preserved rather than collapsed.
            paragraphs.append(paragraph('spacer'))
            continue
        kind, text = classify(line.strip())
        paragraphs.append(paragraph(kind, text))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            f'<w:document {W} {R}><w:body>{"".join(paragraphs)}\n{SECT_PR}'
            '</w:body></w:document>')




def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    document = build_document(src.read_text())
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CONTENT_TYPES)
        z.writestr('_rels/.rels', ROOT_RELS)
        z.writestr('word/document.xml', document)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('word/styles.xml', STYLES_XML)
        z.writestr('word/footer1.xml', FOOTER_XML)
    print(f'{dest} — {document.count("<w:p>")} paragraphs')


if __name__ == '__main__':
    main()
