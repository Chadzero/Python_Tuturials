#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    url_log = []
    google = "https://developers.google.com/edu/python/"
    with open(filename) as urlfile:
        for line in urlfile.readlines():
            url = re.search(r'GET \S*class/(\S*puzzle.*) HTTP', line)
            if url is not None:
                url_log.append(google + url.group(1))

    urltype = re.search(r'-\w+-\w+', url_log[0])
    if urltype:
        returnVar = sorted(set(url_log), key=lambda x: re.search(r'-\w+-(\w+)', x).group(1))
    else:
        returnVar = sorted(set(url_log))
    return returnVar

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # Build directory if it does not currently exist.
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    index = file(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')
    for x, img_url in enumerate(img_urls):
        dest_file = os.path.join(dest_dir, "img%d.jpg" % x) # rename
        try:
            print "Retrieving.....%s" % img_url
            urllib.urlretrieve(img_url, dest_file)  # downloads the url data to the given file path
        except IOError:
            print "Problem reading url: %s" % img_url
        else:
            index.write('<img src="%s">' % os.path.abspath(dest_file))
    index.write('\n</body></html>\n')
    index.close()
    return


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)

if __name__ == '__main__':
    main()


# Contents of the index.html.  lay the image tage together and Firefox will concatanate them for us.