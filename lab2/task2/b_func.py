import sys
from printHelper import printFunction
def sumOfData():
    f = sys.stdin
    i = 0
    for line in f:
        try:
            tmp = line.split(" ")
            i+=int(tmp[-1])
        except ValueError:
           pass
    return(i/(1024**3))

if __name__ == '__main__':
    printFunction(sumOfData())