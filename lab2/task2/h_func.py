import sys

def printRequests():
    polishDomain = "pl"
    f = sys.stdin
    for line in f:
        try:
            lineSplitted = line.split(" ")
            path = lineSplitted[-4]
            pathSplitted = path.split(".")
            extension = pathSplitted[-1]
            if(extension == polishDomain):
                print(line)
        except ValueError:
           pass

if __name__ == '__main__':
    printRequests()