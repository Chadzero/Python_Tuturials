#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename) as f:
        name_Return = {}
        file_text = f.readlines()
        for line in file_text:
            result = re.search(r'<tr.+<td>(\d+)</td><td>(\w+)</td><td>(\w+)', line)
            if result:
                for name in range(2, 4):
                    if not (name_Return.get(result.group(name))) or name_Return.get(result.group(name)) > result.group(0):
                        name_Return[result.group(name)] = result.group(1)
    return name_Return

def extract_date(filename):
    # Get the current year for the filename
    # <h3 align="center">Popularity in 1990</h3>
    with open(filename) as f:
        file_text = f.read()
        year = re.search(r'Popularity\sin\s(\d\d\d\d)', file_text).group(1)
    return year

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:
        year = extract_date(filename)
        if not year:
            # We didn't find a year, so we'll exit with an error message.
            sys.stderr.write('Couldn\'t find the year!\n')
            sys.exit(1)

        names = extract_names(filename)
        namesList = []
        for key in sorted(names.keys()):
                namesList.append('%s %s' % (key, str(names[key])))
        text = '\n'.join(namesList)

        if summary:
            outf = open(filename + '.summary', 'w')
            outf.write(year + '\n' + text + '\n')
            outf.close()
        else:
            print year
            print text



if __name__ == '__main__':
    main()
