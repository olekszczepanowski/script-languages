import sys

def sumOfData():
    f = sys.stdin
    i = 0
    for line in f:
        try:
            tmp = line.split(" ")
            i+=int(tmp[-1])
        except ValueError:
           pass
    f.close()
    print("Gigabytes of data: "+str(round((i/(1024**3)),2))+"GB")

sumOfData()