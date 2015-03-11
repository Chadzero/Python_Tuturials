__author__ = 'Chad_Ramey'

import os
import re

def url_find(filename):
    url_log = []
    google = "https://developers.google.com/edu/python/"
    with open(filename) as urlfile:
        for line in urlfile.readlines():
            url = re.search(r'GET \S*class/(\S*puzzle.*) HTTP', line)
            if url is not None:
                url_log.append(google + url.group(1))
    return sorted(set(url_log))

urls = url_find("animal_code.google.com")
for url in urls:
    print url
