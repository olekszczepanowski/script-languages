import sys
from datetime import datetime
from formatDate import format_date
from lineChecker import isLineValid
from printHelp import printList
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

def sort_log(logList, sortKey):
    if (sortKey >= len(logList)):
        return "Blad rozmiaru"
    sorted_log = sorted(logList, key=lambda x: x[sortKey])
    return sorted_log

def get_entries_by_addr(logList, address):
    entries = [entry for entry in logList if entry[0] == address]
    return entries

def get_failed_reads(logList, isMerged):
    list_http4 = []
    list_http5 = []
    for tuple in logList:
        if str(tuple[4])[0] == "4":
            list_http4.append(tuple)
        if str(tuple[4])[0] == "5":
            list_http5.append(tuple)
    
    if(isMerged):
        return (list_http4+list_http5)
    return(list_http4,list_http5)

def get_entries_by_extension(logList, extension):
    entries_with_extension = []
    for entry in logList:
        path = entry[2]
        if path.endswith("." + extension):
            entries_with_extension.append(entry)
    return entries_with_extension

def print_entries(logList, n):
    if (n >= len(logList)):
        return "Blad rozmiaru"
    
    output = []
    for log in range(n):
        output.append(logList[log])
    return output
if __name__ == '__main__':
    lista = read_log(sys.stdin)
    # printList(lista)
    # print("\n")
    # printList(sort_log(lista, 3))
    # print("\n")
    # printList(sort_log(lista, 5))
    # print("\n")
    # printList(sort_log(lista, 100))
    # print("\n")
    # printList(sort_log(lista, -1))
    # printList(get_entries_by_addr(lista, "205.189.154.54"))
    # print("\n")
    # printList(get_entries_by_addr(lista, ""))
    # print("\n")
    # printList(get_entries_by_addr(lista, "unicomp6.unicomp.net"))
    # print("\n")
    # printList(get_failed_reads(lista,True))
    # print("\n")
    # printList(get_failed_reads(lista,False))
    # print("\n")
    # printList(get_entries_by_extension(lista,"jpg"))
    # print("\n")
    # printList(get_entries_by_extension(lista,"gif"))
    # print("\n")
    # printList(get_entries_by_extension(lista,""))
    # print("\n")
    printList(print_entries(lista,3))
    print("\n")
    printList(print_entries(lista,-1))
    print("\n")
    printList(print_entries(lista,100))
    print("\n")
