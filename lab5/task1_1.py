import sys
import re
import logging
from datetime import datetime
path = "TEST.log"

def readFile(filePath):
    try:
        file = open(filePath, "r")
        lines = file.readlines()
        logs = {}
        
        for index in range(0, len(lines)):
            line = lines[index]
            log = createDict(line)
            if log:
                logs[index] = log
               
        file.close()
        return logs
    except :
        print("Plik nie został znaleziony: ", filePath)
        return None
    

def createDict(line):
    pattern = r'(\b\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (\w+) (\w+\[\d+\]): (.*)'

    logDict= {}
    
    match = re.match(pattern, line)
    if match:
        if match.group(1):
           tmpDate = datetime.strptime(match.group(1),"%b %d %H:%M:%S").replace(year=2000)
           logDict = {
               "date": tmpDate,
               "username": match.group(2),
               "appComponent": match.group(3),
               "description": match.group(4)
           }
        return logDict
    else:
        print("Błąd dopasowania wzorca dla linii:", line)
        return None

def get_ipv4s_from_log(logLine):
    return re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",logLine["description"])

def get_user_from_log(logLine):
     username = re.search(r'(?<=\buser\s)\w+',logLine["description"])
     if username:
         return username.group()
     else:
         return None
def get_message_type(description):
    if re.search(r"Accepted password",description):
        return "udane logowanie"
    elif re.search(r"authentication failure", description):
        return "nieudane logowanie"
    elif re.search(r"Failed password for",description):
        return "bledne haslo"
    elif re.search(r"Connection closed",description):
        return "polaczenie zamkniete"
    elif re.search(r"Invalid user|invalid user|user unknown",description):
        return "niewlasciwy uzytkownik"
    elif re.search(r"BREAK-IN",description):
        return "wlamanie"
    else:
        return "inne"

logs = readFile(path)
# print(logs)
# list_ipv4s = get_ipv4s_from_log(logs[2])
# print(list_ipv4s)
user = get_user_from_log(logs[4])
print(user)
# description = get_message_type(logs[1]["description"])
# print(description)

