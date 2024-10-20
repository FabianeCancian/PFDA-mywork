# ex 2
import csv 
FILENAME= "data.csv"
DATADIR = ""

#with open (DATADIR + FILENAME, "rt") as fp:
 #   reader = csv.reader(fp, delimiter=",")
  #  for line in reader:
   #     print (line)

# ex 3
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount:
            print (f"{line}\n------------")
        else:
            print(line)
        linecount += 1

# ex 4

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            pass
        else:
            total += line[1]#int(line[1])
        linecount += 1

print (f"average is {total/(linecount-1)}")