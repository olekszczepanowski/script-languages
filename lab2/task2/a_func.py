import sys
from printHelper import printFunction
def numberOfRequests(data):
    f = sys.stdin
    i = 0
    for line in f:
        try:
            tmp = line.split(" ")
            if(tmp[-2] == data):
             i+=1
        except ValueError:
           pass
    return i


if __name__ == '__main__':
    arg = sys.argv[1]
    printFunction(numberOfRequests(arg))

