import sys

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
    print("Path to file: "+path+" "+str(biggestData)+"B")
if __name__ == '__main__':
    pathToTheBiggestData()