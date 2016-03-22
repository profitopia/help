#!/usr/bin/env python3
import os
import re


base_path = 'build/html/'


def main():
    """
    Updates the generated html files in build/html dir
    """
    files = [os.path.join(dp, f) for dp, dn, fn in
             os.walk(base_path) for f in fn]
    for cur_file in files:
        if cur_file[-5::] != '.html':
            continue
        fsock = open(cur_file, 'r')
        content = fsock.read()

        content = re.sub(r'<div class="version">.*?</div>', '', content,
                         flags=re.DOTALL)
        content = re.sub(r'placeholder="Search docs"',
                         r'placeholder="Hilfe durchsuchen ..."',
                         content, flags=re.DOTALL)
        content = re.sub(r'Profitopia-Hilfe 1 Dokumentation',
                         r'Profitopia-Hilfe',
                         content, flags=re.DOTALL)
        content = re.sub(r'>Docs</a>',
                         r'>Profitopia-Hilfe</a>',
                         content, flags=re.DOTALL)
        content = re.sub(r'Built with (.*?)>Sphinx</a> using a ' +
                         r'(.*?)>theme</a> provided by (.*?)</a>.',
                         r'Mit \1>Sphinx</a> und einem \2>Theme</a> von ' +
                         r'\3</a> erstellt.',
                         content)
        content = re.sub(r'<a (.*?)> Previous</a>',
                         r'<a \1> Zurück</a>',
                         content, flags=re.DOTALL)
        content = re.sub(r'<a (.*?)>Next (.*?)</a>',
                         r'<a \1>Weiter \2</a>',
                         content, flags=re.DOTALL)
        # add links to game and blog
        content = re.sub(r'(class="icon icon-home".*?</a>)', r'\1<br />\n  <a href="https://www.profitopia.de" target="_blank">Zum Spiel</a> &bull; <a href="https://blog.profitopia.de" target="_blank">Blog</a>', content, flags=re.DOTALL)

        open(cur_file, 'w').write(content)


if __name__ == '__main__':
    main()
