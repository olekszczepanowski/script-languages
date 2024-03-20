import sys
from printHelper import printFunction
def printRequests(domain):
    f = sys.stdin
    retVal = ""
    for line in f:
        try:
            lineSplitted = line.split(" ")
            if(lineSplitted[0].endswith(domain)):
                retVal+=line
        except ValueError:
           pass
    return retVal

if __name__ == '__main__':
    arg1 = sys.argv[1]
    printFunction(printRequests(arg1))