#!/usr/bin/env python

import subprocess


def main():
    """ create a new list of words containing the brand name and keywords """
    brandname = input("Enter comma seperated branded terms: ")
    keywords = input("Enter comma seperated product keywords: ")
    brnds = [brnd.strip() for brnd in brandname.split(',')]
    kwds = [kwd.strip() for kwd in keywords.split(',')]
    new_list = []

    for brnd in brnds:
        for kwd in kwds:
            if brnd != kwd:
                new_list.append(f'"{brnd} {kwd}"')
                new_list.append(f'[{brnd} {kwd}]')

    new_list.sort()

    return new_list


if '__main__' == __name__:
    sorted_keyword_list = main()
    text_to_clipboard = '\n'.join(sorted_keyword_list)
    subprocess.run("pbcopy", universal_newlines=True, input=text_to_clipboard)
    print('Copied new keywords to clipboard!')