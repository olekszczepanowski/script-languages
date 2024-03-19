def printRequests(filePath, data):
    f = open(filePath,"r", encoding="utf8")
    for line in f:
        try:
            tmp = line.split(" ")
            if(tmp[-2] == data):
                print(line) 
        except ValueError:
           pass
    f.close()

printRequests("lab2/NASA","404")

