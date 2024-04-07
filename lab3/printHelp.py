import sys

def printList(result):
    sys.stdout.write(str(result))

def printDict(result):
    for key, value in result.items():
        sys.stdout.write(str(key) +": "+str(value)+", ")