#!/usr/bin/env python3
import os
import re


base_path = 'build/html/'


def main():
    """
    Updates the generated html files in build/html dir
    """
    files = os.listdir(base_path)
    for cur_file in files:
        if cur_file[-5::] != '.html':
            continue
        fsock = open(os.path.join(base_path, cur_file), 'r')
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

        open(os.path.join(base_path, cur_file), 'w').write(content)


if __name__ == '__main__':
    main()
