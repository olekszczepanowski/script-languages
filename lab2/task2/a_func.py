import sys

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
    print("Number of requests for "+data+": "+str(i))


if __name__ == '__main__':
    arg = sys.argv[1]
    numberOfRequests(arg)

