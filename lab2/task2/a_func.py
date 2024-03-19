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

numberOfRequests(sys.argv[1])
# numberOfRequests("200")
# numberOfRequests("lab2/NASA","302")
# numberOfRequests("lab2/NASA","404")



# for line in sys.stdin:
#     print(line.rstrip())
