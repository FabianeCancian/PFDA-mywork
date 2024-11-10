import re
regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"
replecementText = "\\1xxx.xxx"
filename = "smalleracess.log"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            newLine = re.sub(regex, replecementText, line)
            outputFile.write(newLine)