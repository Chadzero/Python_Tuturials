#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    full_paths = []
    files = os.listdir(dir)
    for fileName in files:
        match = re.search(r'__(\w+)__', fileName)
        if match:
            full_paths.append(os.path.abspath(fileName))
    return full_paths

def copy_to(paths, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for path in paths:
        file_name = os.path.basename(path)
        shutil.copy(path, os.path.join(destination, file_name))
    print "Copied files to %s" % destination
    return

def zip_to(paths, zippath):
    zip_exe_path = '"C:\\Program Files\\7-Zip\\7z.exe"'
    zip_command = "%s a %s %s" % (zip_exe_path, zippath, ' '.join(paths))
    print "Executing the following command: %s" % zip_command
    # execute the command here...
    status = subprocess.Popen(zip_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if status.wait():
        for line in status.stdout.readlines():
            print line
    return

def main():
    # This basic command line argument parsing code is provided.
    #  Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
      print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
      sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
      todir = args[1]
      del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
      tozip = args[1]
      del args[0:2]

    if len(args) == 0:
      print "error: must specify one or more dirs"
      sys.exit(1)

    # +++your code here+++
    # Call your functions
    directoryPaths = get_special_paths(args[0])

    if todir:
        copy_to(directoryPaths, todir)

    elif tozip:
        zip_to(directoryPaths, tozip)

    else:
        print '\n'.join(directoryPaths)

if __name__ == "__main__":
  main()