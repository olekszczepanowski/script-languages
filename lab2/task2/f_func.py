import sys
from printHelper import printFunction
def printHours(lowerBound, higherBound):
    if lowerBound < 0 or lowerBound > 23 or higherBound < 0 or higherBound > 23:
        raise ValueError("Wrong input")
    f = sys.stdin
    retVal = ""
    for line in f:
        try:
            
            tmp = line.split(" ")
            date = tmp[3]
            dateSplitted = date.split(":")
            hour = int(dateSplitted[1])
            if(hour>=lowerBound and hour<=higherBound):
                retVal+=line
        except ValueError:
           pass
    return retVal

if __name__ == '__main__':
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    printFunction(printHours(arg1,arg2))