import sys
from printHelper import printFunction
def printRequests(data):
    f = sys.stdin
    retVal=""
    for line in f:
        try:
            tmp = line.split(" ")
            if(tmp[-2] == data):
                retVal+=line
        except ValueError:
           pass
    return retVal
if __name__ == '__main__':
    arg1 = sys.argv[1]
    printFunction(printRequests(arg1))

