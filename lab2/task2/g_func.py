import sys
from printHelper import printFunction
def printDays(targetDate):
    f = sys.stdin
    retVal=""
    for line in f:
        try:
            tmp = line.split(" ")
            date = tmp[3]
            dateSplitted = date.split(":")
            day = str(dateSplitted[0])
            daySplitted = day.split('[')
            finalDate = daySplitted[1]
            if(finalDate == targetDate):
                retVal+=line
        except ValueError:
           pass
    return retVal

if __name__ == '__main__':
    arg1 = (sys.argv[1])
    printFunction(printDays(arg1))