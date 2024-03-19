import sys
def printRequests(data):
    f = sys.stdin
    for line in f:
        try:
            tmp = line.split(" ")
            if(tmp[-2] == data):
                print(line) 
        except ValueError:
           pass
if __name__ == '__main__':
    arg1 = sys.argv[1]
    printRequests(arg1)

