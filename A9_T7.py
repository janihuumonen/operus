########################################################
# Task A9_T7
# Developer Jani Huumonen
# Date 2025-12-07
########################################################

import sys
import os

def showHelp() -> None:
    print('Invalid amount of arguments.')
    print(f'[USAGE] python {sys.argv[0]} src_file dst_file')
    return None

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    print(f'Source file "{PSrcFile}"')
    print(f'Destination file "{PDstFile}"')
    print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
    Proceed = True # One-way flag
    if (os.path.exists(PDstFile)):
        print(f'Destination file "{PDstFile}" already exists.')
        Proceed = 'y' == input('Do you want to overwrite it? (y/n): ')
    if Proceed:
        try:
            with open(PSrcFile) as rf:
                with open(PDstFile, "w") as wf:
                    wf.write(rf.read())
        except:
            print(f'''Couldn't copy "{PSrcFile}" to "{PDstFile}".''')
    return None

def main() -> None:
    print("Program starting.")
    if (len(sys.argv) == 3):
        copyFile(*sys.argv[1:3])
    else:
        showHelp()
    print("Program ending.")
    return None

main()

