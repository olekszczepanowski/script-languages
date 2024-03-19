import sys

def numberOfRequests(filePath, data):
    f = open(filePath,"r", encoding="utf8")
    i = 0
    errors = 0
    for line in f:
        try:
            tmp = line.split(" ")
            if(tmp[8] == data):
             i+=1
        except:
           errors+=1
    f.close()
    print("Number of requests for "+data+": "+str(i))
    print("Errors in format: "+str(errors))


numberOfRequests("lab2/NASA","200")
numberOfRequests("lab2/NASA","302")
numberOfRequests("lab2/NASA","404")



# for line in sys.stdin:
#     print(line.rstrip())
