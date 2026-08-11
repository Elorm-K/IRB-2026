#!/usr/bin/env python3
"""Print the plain text of a .docx, one line per paragraph.

Used to diff a rebuilt submission against the previous one, and to run the
verification passes against what a reviewer will actually read.
"""

import re
import sys
import zipfile


def text_of(path):
    xml = zipfile.ZipFile(path).read('word/document.xml').decode('utf-8')
    lines = []
    # Word writes <w:p w:rsidR="..">; our own builder writes a bare <w:p>.
    for para in re.findall(r'<w:p(?:\s[^>]*)?>.*?</w:p>', xml, re.S):
        runs = re.findall(r'<w:t[^>]*>(.*?)</w:t>', para, re.S)
        line = ''.join(runs)
        line = (line.replace('&quot;', '"').replace('&lt;', '<')
                    .replace('&gt;', '>').replace('&amp;', '&'))
        lines.append(line)
    return lines


if __name__ == '__main__':
    print('\n'.join(text_of(sys.argv[1])))
