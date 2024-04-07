import sys
from lineChecker import isLineValid
from formatDate import format_date
from printHelp import printDict, printList
def read_log(f):
    listOfTuples = []
    for line in f:
        try:
            lineSplitted = line.split()
            if(isLineValid(lineSplitted)):
                ip = lineSplitted[0]
                date = format_date(lineSplitted[3][1:])
                path = lineSplitted[6]
                httpVersion = lineSplitted[7][:-1]
                code = int(lineSplitted[8])
                bytes = lineSplitted[9]
                tuple = (ip, date, path, httpVersion, code, bytes)
                listOfTuples.append(tuple)
        except ValueError:
            pass
    return listOfTuples

def entry_to_dict(entry):
    dict = {
        "ip": entry[0],
        "date": entry[1],
        "path": entry[2],
        "httpVersion": entry[3],
        "code": entry[4],
        "bytes": entry[5]
    }
    return dict

def log_to_dict(logList):
    dict = {}
    for entry in logList:
        key = entry[0]
        if key not in dict:
            dict[key] = []
        dict[key].append(entry_to_dict(entry))
    return dict

def get_addrs(logDict):
    addrs = logDict.keys()
    return addrs

code = 200

def print_dict_entry_dates(logDict):
    outputList = get_dict_entry_dates(logDict)
    for element in outputList:
        sys.stdout.write(element+"\n")

def get_dict_entry_dates(logDict):
    outputList = []
    for key, value in logDict.items():
        outputString = ""
        outputString += ("Address: " + key + ", ")
        outputString += ("Number of requests: " + str(len(value))+", ")
        datesList = get_dates_list(value)
        outputString+=("First request: "+ str(min(datesList))+", ")
        outputString+=("Last request: "+ str(max(datesList))+", ")
        outputString+=("Code: "+str(code)+ " proportion to other codes: "+str(get_code_count(value,code)))
        outputList.append(outputString)

    return outputList

def get_code_count(dictList, code):
    codeCount = 0
    otherCount = 0
    for dict in dictList:
        if(dict["code"] == code):
            codeCount += 1
        else:
            otherCount += 1
    if codeCount == 0 or otherCount == 0:
        return 0
    
    return codeCount/otherCount

def get_dates_list(dictList):
    datesList = []
    for dict in dictList:
        datesList.append(dict["date"])

    return datesList


if __name__ == '__main__':
    lista = read_log(sys.stdin)
    # printDict(entry_to_dict(lista[0]))
    # print("\n")
    # printDict(entry_to_dict(lista[1]))

    # printDict(log_to_dict(lista))
    # printList(get_addrs(log_to_dict(lista)))
    print_dict_entry_dates(log_to_dict(lista))
