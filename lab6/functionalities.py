import sys
import re
import logging
from datetime import datetime
from typing import List, Optional, Tuple, Iterator, Dict


# path = "TEST.log"

def readFile(filePath: str) -> Iterator[str]:
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def createLog(line: str) -> Optional[Tuple[datetime, str, int, str]]:
    pattern: str = r'(\b\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}) (\w+) (\w+\[(\d+)\]): (.*)'

    match: Optional[re.Match] = re.match(pattern, line)
    if match:
        if match.group(1):
            tmpDate: datetime = datetime.strptime(match.group(1), "%b %d %H:%M:%S")
            if tmpDate.month == 1:
                tmpDate = tmpDate.replace(year=2024)
            else:
                tmpDate = tmpDate.replace(year=2023)

            date: datetime = tmpDate
            hostName: str = match.group(2)
            pidNumber: int = int(match.group(4))
            description: str = match.group(5)

        return (date, hostName, pidNumber, description)
    else:
        print("Błąd dopasowania wzorca dla linii:", line)
        return None


def get_ipv4s_from_log(content: str) -> List[str]:
    ip_regex = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b")
    return ip_regex.findall(content)


def get_user_from_log(content: str) -> Optional[str]:
    username = re.search(r'(?<=\buser\s)\w+|(?<=Accepted password for\s)\w+', content)
    if username:
        return username.group()
    else:
        return None


def group_by_user(listOfLogs: List[str]) -> Dict[str, List[str]]:
    userEntriesMap: Dict[str, List[str]] = {}
    for log_entry in listOfLogs:
        user: Optional[str] = get_user_from_log(log_entry)
        if user:
            if user in userEntriesMap:
                userEntriesMap[user].append(log_entry)
            else:
                userEntriesMap[user] = [log_entry]
    return userEntriesMap


def get_message_type(description: str) -> str:
    if re.search(r"Accepted password for", description):
        return "udane logowanie"
    elif re.search(r"authentication failure", description):
        return "nieudane logowanie"
    elif re.search(r"Failed password for", description):
        return "bledne haslo"
    elif re.search(r"Connection closed", description):
        return "polaczenie zamkniete"
    elif re.search(r"Invalid user|invalid user|user unknown", description):
        return "niewlasciwy uzytkownik"
    elif re.search(r"BREAK-IN", description):
        return "wlamanie"
    else:
        return "inne"
print(get_user_from_log("192.168.0.1"))    # Powinno zwrócić "192.168.0.1"
print(get_user_from_log("666.777.88.213"))  # Powinno zwrócić None
print(get_user_from_log("255.255.255.255")) # Powinno zwrócić "255.255.255.255"
print(get_user_from_log("999.999.999.999"))