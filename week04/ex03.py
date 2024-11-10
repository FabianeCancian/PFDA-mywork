import re
regex = "\[.*\]"
filename = "smalleracess.log"

with open (filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall (regex, line)
        if (len(foundTextList) != 0):
            foundText = foundTextList[0]
            print(foundText)