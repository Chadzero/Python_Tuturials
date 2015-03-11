__author__ = 'Chad_Ramey'

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for letter in s:
    if letter in vowels:
        count += 1

print "Number of vowels: " + str(count)



# Write a program that prints the number of times the string 'bob' occurs in s.

letterPos = 0
bobCount = 0
for letter in s:
    if letter == 'b':
        if s[letterPos:letterPos+3] == 'bob':
            bobCount += 1
    letterPos += 1

print"Number of times bob occurs is: " + str(bobCount)


# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# In the case of ties, print the first substring.

longestStart = 0
longestEnd = 0
letterIndex = 0
subIndex = 0
strLength = len(s)

while letterIndex < strLength:
    subIndex = letterIndex
    while subIndex < strLength-1:
        if s[subIndex] <= s[subIndex+1]:
           subIndex += 1
        else:
            break
    if (longestEnd - longestStart) < (subIndex - letterIndex):  #update the longest indexes if longer match found
        longestStart = letterIndex
        longestEnd = subIndex
    letterIndex = subIndex + 1
print "Longest substring in alphabetical order is: " + s[longestStart:longestEnd+1]