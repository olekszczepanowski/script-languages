import sys
def printHours(lowerBound, higherBound):
    f = sys.stdin
    for line in f:
        try:
            
            tmp = line.split(" ")
            date = tmp[3]
            dateSplitted = date.split(":")
            hour = int(dateSplitted[1])
            if(hour>=int(lowerBound) and hour<=int(higherBound)):
                print(line)
        except ValueError:
           pass

if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    printHours(arg1,arg2)