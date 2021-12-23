#!/usr/bin/env python

""" kmix.py: create a new list of words containing the brand name and keywords
    formatted for google ads and copies it to the clipboard."""

__author__      = "G. Thomas Simmons"
__copyright__   = "MIT License"

import subprocess
import platform

def main():
    """ User inputs the brand name and keywords and the program creates a new list."""

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

def copy_to_clipboard(sorted_keyword_list):
    """ Copy the new list to the clipboard."""
    text_to_clipboard = '\n'.join(sorted_keyword_list)
    if platform.system() == 'Darwin':
        subprocess.run(['pbcopy'], universal_newlines=True, input=text_to_clipboard)
    elif platform.system() == 'Windows':
        subprocess.run(['clip'], universal_newlines=True, input=text_to_clipboard)
    else:
        subprocess.run(['xsel', '-ib'], universal_newlines=True, input=text_to_clipboard)

if '__main__' == __name__:
    sorted_keyword_list = main()
    copy_to_clipboard(sorted_keyword_list)
    print()
    print('\n'.join(sorted_keyword_list))
    print('\nKeyword list has been copied to your clipboard!')