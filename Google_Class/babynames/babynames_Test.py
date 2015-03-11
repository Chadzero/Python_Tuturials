#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import unittest

def extract_date(filename):
    # Get the current year for the filename
    # <h3 align="center">Popularity in 1990</h3>
    with open(filename) as f:
        file_text = f.read()
        year = re.search(r'(Popularity in )(\d\d\d\d)', file_text).group(2)

    return year

# <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
# <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
# <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>

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

if __name__ == '__main__':

    print extract_names(r"C:\GitHub\Python_Tuturials-master\Google Class\babynames\baby1990.html")


"""
    years = [1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008]
    for year in years:
        filename = r'C:\GitHub\Python_Tuturials-master\Google Class\babynames\baby%s.html' % year
        print extract_date(filename)
"""

