import csv 
FILENAME= "data.csv"
DATADIR = "C:/Users/fabia/Desktop/Data Analytics/Programming for data analytics/PFDA-mywork/"
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

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print (line)
        count +=1
    print(f"average is {total/count}")