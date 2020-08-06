import re

######## Section 1 # content.txt -> p1.txt

content = open("content.txt").read()

file = open("p1.txt","w")

match1 = re.findall("[A-Z][a-zA-Z\-\']{3,}", content)
print( ('\n'.join(match1)), file = open("p1.txt","a") )

file.close()


######## Section 2 # content.txt -> p2.txt

file = open("p2.txt","w")

match2 = re.findall(r"(?:(?<!'))\b(?:[^AEIOUaeiou\s\'\,\.])*(?:(?:[e][^AEIOUaeiou\s\'\,\.])|(?:[^AEIOUaeiou\s\,\.][e]))\b(?:(?!'))", content)
print( ('\n'.join(match2)), file = open("p2.txt","a") )

file.close()


######## Section 3 # content.txt -> p3.txt

file = open("p3.txt","w")

match3 = re.findall(r"(?:[A-Z]\.?){2,}(?:(?=s)|\b)", content)
print( ('\n'.join(match3)), file = open("p3.txt","a") )

file.close()

#########################
