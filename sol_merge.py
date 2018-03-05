#!/usr/bin/python
# -*- coding: utf-8 -*-

# sol_merge
# Copyright (C) 2017  Ilya Golshtein
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from optparse import OptionParser
import sys
import os

usage = """
%prog [options]
    merge solidity files processing import directives
"""

known_files = {}
import_remappings = []

def run(fname):
    if fname not in known_files:
        fbasename = os.path.basename(fname)
        fdir = os.path.dirname(fname)
        origdir = os.getcwd()
        if fdir:
            os.chdir(fdir)

        with open(fbasename, 'r') as f:
            for line in f:
                if line.lstrip().startswith("import"):
                    file_to_import = line.replace("\t", " ").split()[-1]
                    for remap in import_remappings:
                        file_to_import = file_to_import.replace(remap[0], remap[1])
                    for to_replace in "'\";\n":
                        file_to_import = file_to_import.replace(to_replace,"")
                    run(file_to_import)
                else:
                    sys.stdout.write(line)
        os.chdir(origdir)

        known_files[fname] = 1


def main():
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", "--filename", "--source", dest="fname",
                      help="File to start from")
    parser.add_option("--import-remappings", dest="import_remappings", default="",
                      help="path_in_source1=path_in_file_system1 path_in_source2=path_in_file_system2")
    (options, args) = parser.parse_args()
    if options.import_remappings:
        import_remappings_arr = options.import_remappings.replace(",", " ").split()
        for el in import_remappings_arr:
            import_remappings.append(el.split('='))
    run(options.fname)

if __name__ == "__main__":
    main()
