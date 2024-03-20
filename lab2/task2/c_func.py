import sys
from printHelper import printFunction
def pathToTheBiggestData():
    f = sys.stdin
    biggestData = 0
    for line in f:
        try:
            tmp = line.split(" ")
            if(int(tmp[-1])>biggestData):
                biggestData = int(tmp[-1])
                path = tmp[-4]
        except ValueError:
           pass
    return path+" "+str(biggestData)
if __name__ == '__main__':
    printFunction(pathToTheBiggestData())