import sys
import re
import logging
from datetime import datetime
# path = "TEST.log"

def readFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            yield line
    

def createLog(line):
    pattern = r'(\b\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (\w+) (\w+\[(\d+)\]): (.*)'

    match = re.match(pattern, line)
    if match:
        if match.group(1):
            tmpDate = datetime.strptime(match.group(1),"%b %d %H:%M:%S")
            if tmpDate.month == 1:  
                tmpDate = tmpDate.replace(year=2024)
            else:  
                tmpDate = tmpDate.replace(year=2023)
            
            date= tmpDate
            hostName= match.group(2)
            pidNumber= int(match.group(4))
            description= match.group(5)
           
        return (date,hostName,pidNumber,description)
    else:
        print("Błąd dopasowania wzorca dla linii:", line)
        return None

def get_ipv4s_from_log(content):
    return re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", content)

def get_user_from_log(content):
     username = re.search(r'(?<=\buser\s)\w+|(?<=Accepted password for\s)\w+',content)
     if username:
         return username.group()
     else:
         return None

def group_by_user(listOfLogs):
    userEntriesMap = {}
    for log_entry in listOfLogs:
        user = get_user_from_log(log_entry)
        if user:
            if user in userEntriesMap:
                userEntriesMap[user].append(log_entry)
            else:
                userEntriesMap[user] = [log_entry]
    return userEntriesMap

def get_message_type(description):
    if re.search(r"Accepted password for",description):
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

# def runGetIpv4FromLog(logs):
#     for log in logs.values():
#         tab = get_ipv4s_from_log(log)
#         if len(tab) > 0:
#             print(tab)

# def runGetUserFromLog(logs):
#     for log in logs.values():
#         user = get_user_from_log(log)
#         if user:
#             print(user)

# def runGetMessageType(logs):
#     for log in logs.values():
#         print(get_message_type(log["description"]))


