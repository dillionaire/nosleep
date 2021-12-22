import subprocess


brandname = input("Enter comma seperated branded terms: ")
keywords = input("Enter comma seperated product keywords: ")
brnds = [brnd.strip() for brnd in brandname.split(',')]
kwds = [kwd.strip() for kwd in keywords.split(',')]


def main():
    """ create a new list of words containing the brand name and keywords """
    new_list = []
    for brnd in brnds:
        for kwd in kwds:
            if brnd != kwd:
                new_list.append(f'"{brnd} {kwd}"')
                new_list.append(f'[{brnd} {kwd}]')
    return new_list


new_list = main()
new_list.sort()
out_text = '\n'.join(new_list)
subprocess.run("pbcopy", universal_newlines=True, input=out_text)
print('Copied new keywords to clipboard!')