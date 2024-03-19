import sys
def printDays(targetDate):
    f = sys.stdin
    for line in f:
        try:
            tmp = line.split(" ")
            date = tmp[3]
            dateSplitted = date.split(":")
            day = str(dateSplitted[0])
            daySplitted = day.split('[')
            finalDate = daySplitted[1]
            if(finalDate == targetDate):
                print(line)
        except ValueError:
           pass
printDays("01/Jul/1995")