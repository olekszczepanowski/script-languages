import os
import sys

def func():
    outputList = []
    for key, value in os.environ.items():
        display = (len(sys.argv) == 1) 
        if not display:
            for arg in sys.argv[1:]:
                if arg.lower() in key.lower():
                    display = True
                    break
        if display:
            element = key + ": " + value
            outputList.append(element)
    
    outputList.sort()
    for element in outputList:
        sys.stdout.write(element+"\n")

if __name__ == '__main__':
    func()