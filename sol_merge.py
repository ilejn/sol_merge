#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys
import os

usage = """
%prog [options]
    merge solidity filee processing import directives
"""

known_files = {}

def run(fname):
    if fname not in known_files:
        fbasename = os.path.basename(fname)
        fdir = os.path.dirname(fname)
        origdir = os.getcwd()
        if fdir:
            os.chdir(fdir)

        with open(fbasename, 'r') as f:
            for line in f:
                if line.startswith("import"):
                    file_to_import = line.split(" ")[1]
                    for to_replace in "'\";\n":
                        file_to_import = file_to_import.replace(to_replace,"")
                    run(file_to_import)
                else:
                    sys.stdout.write(line)
        os.chdir(origdir)

        known_files[fname]=1


def main():
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", "--source", dest="fname",
                      help="File to start from")
    (options, args) = parser.parse_args()
    run(options.fname)

if __name__ == "__main__":
    main()
