#!/usr/bin/env python

import subprocess
import platform

def main():
    """ User inputs the brand name and keywords, and the script will create a new
    list of words containing the brand name and keywords formatted for google ads
    and copy it to the clipboard."""

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
        subprocess.run(['pbcopy'], input='\n'.join(text_to_clipboard))
    elif platform.system() == 'Windows':
        subprocess.run(['clip'], input='\n'.join(text_to_clipboard))
    else:
        subprocess.run(['xsel', '-ib'], input='\n'.join(text_to_clipboard))

if '__main__' == __name__:
    sorted_keyword_list = main()
    copy_to_clipboard(sorted_keyword_list)
    print('\n'.join(sorted_keyword_list))
    print('\nCopied new keywords to clipboard. Paste into google ads with CMD+V')