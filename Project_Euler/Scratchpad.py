####################################################################
##  Python Challenge #1
####################################################################
'''
cypher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

offset = 2
letterList = []

import string
for letter in cypher:
    # convert letter to Ascii
    letterint = ord(letter)

    # apply offset
    if letterint in range(ord('a'), ord('z') - offset):
        letterint += offset
    elif letterint in range(ord('z') - offset + 1, ord('z') + 1):
        letterint -= (26 - offset)

    letterList.append(chr(letterint))

print ''.join(letterList)
'''
####################################################################
# Python Challenge #2
####################################################################
'''
filepath = r"C:\Users\Chad_Ramey\Desktop\ocr.html"
cutoff = 30
occDict = {}
with open(filepath) as text_file:
    blob_text = text_file.read()
    for letter in blob_text:
        if letter in occDict:
            occDict[letter] += 1
        else:
            occDict[letter] = 1

    for key, value in occDict.items():
        if value > cutoff:
            blob_text = blob_text.translate(None, key)
            print key
    print blob_text
'''
####################################################################
# Python Challenge #3
####################################################################
'''
import re
filepath = r"C:\Users\Chad_Ramey\Desktop\equality.html"


with open(filepath) as text_file:
    blob_text = text_file.read()
    equality = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', blob_text)
    print ''.join(equality)
'''
####################################################################
# Python Challenge #4
####################################################################
'''
import urllib
import re

nothing_parameter = "12345"
site_base = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

for attempt in range(0, 400):
    current_page = urllib.urlopen(site_base + nothing_parameter)
    text = current_page.read()
    print text
    match = re.search(r'nothing is (\d+)', text)
    if match:
        if nothing_parameter == match.group(1):
            print nothing_parameter
            break
        nothing_parameter = match.group(1)
    else:
        match = re.search(r'Divide by two', text)
        if match:
            nothing_parameter = str(int(nothing_parameter) / 2)

    current_page.close()


'''
####################################################################
# Python Challenge #5
####################################################################
'''
import cPickle
import urllib

f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
obj = cPickle.load(f)
f.close()

print f

for item in obj:
    print ''.join(e[0]*e[1] for e in item)
'''
####################################################################
# Python Challenge #6
####################################################################
'''
import zipfile
import urllib
import re

# site_base = r"http://www.pythonchallenge.com/pc/def/"
site_base = "C:\\Users\\Chad_Ramey\\Desktop\\"
currentfile = "90052"

#f = urllib.urlopen(site_base + "channel.zip")
#f = open(site_base + "channel.zip")
comment_store = []
nothing_regex = re.compile(r"Next nothing is (\d+)")

while True:
    with zipfile.ZipFile(site_base + "channel.zip", 'r') as myzip:
        content = myzip.read(currentfile + ".txt")

        print content

        match = re.search(nothing_regex, content)
        if match:
            newfile = match.group(1)
            comment_store.append(myzip.getinfo(currentfile + ".txt").comment)


        if newfile:
            if newfile == currentfile:
                break
            else:
                currentfile = newfile
        else:
            break
print "".join(comment_store)

#f.close()
'''

####################################################################
# Python Challenge #7
####################################################################


