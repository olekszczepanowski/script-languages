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
    print("Gigabytes of data: "+str(round((i/(1024**3)),2))+"GB")

if __name__ == '__main__':
    sumOfData()
