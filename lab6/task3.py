import ipaddress
import re
from task2 import FailedPassword, AcceptedPassword, Error, Other
from functionalities import readFile, get_ipv4s_from_log
from ipaddress import IPv4Address
from datetime import datetime
from task1 import SSHLogEntry
from typing import List, Iterator, Union, Optional, Dict


class SSHLogJournal:
    def __init__(self) -> None:
        self.logsList: List[SSHLogEntry] = []
        self.ipDict: Dict[str, List[SSHLogEntry]] = {}
        self.dateDict: Dict[datetime, List[SSHLogEntry]] = {}

    @staticmethod
    def validateLogType(log: str) -> SSHLogEntry:
        if re.search(r"Accepted password for", log):
            return AcceptedPassword(log)
        elif re.search(r"Failed password for", log):
            return FailedPassword(log)
        elif re.search(r"error:", log):
            return Error(log)
        else:
            return Other(log)

    def appendDateDict(self, log: SSHLogEntry):
        if log.date in self.dateDict:
            self.dateDict[log.date].append(log)
        else:
            self.dateDict[log.date] = [log]

    def appendIpDict(self, log: SSHLogEntry):
        ips: list[str] = get_ipv4s_from_log(log.description)
        for ip in ips:
            if ip in self.ipDict:
                self.ipDict[ip].append(log)
            else:
                self.ipDict[ip] = [log]

    def appendEntry(self, entry: str):
        logObject: SSHLogEntry = self.validateLogType(entry)
        if logObject.validate():
            self.logsList.append(logObject)
            self.appendDateDict(logObject)
            self.appendIpDict(logObject)
        else:
            entryOther: Other = Other(entry)
            self.logsList.append(entryOther)
            self.appendDateDict(entryOther)
            self.appendIpDict(entryOther)

    def __len__(self) -> int:
        return len(self.logsList)

    def __contains__(self, item: SSHLogEntry) -> bool:
        if not isinstance(item, SSHLogEntry):
            return False
        strItem: str = str(item)
        for log in self.logsList:
            if str(log) == strItem:
                return True

        return False

    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.logsList)

    def get_log_by_key(self, key: Union[int, ipaddress.IPv4Address, datetime]) -> Optional[Union[SSHLogEntry, List[SSHLogEntry]]]:
        if isinstance(key, int):
            return self.logsList[key]
        elif isinstance(key, IPv4Address):
            return self.ipDict.get(str(key), None)
        elif isinstance(key, datetime):
            return self.dateDict.get(key, None)
        else:
            raise KeyError("Nieprawidlowy klucz.")

    def getLogsWithGivenIp(self, searchedIP: ipaddress.IPv4Address) -> Union[SSHLogEntry | list[SSHLogEntry] | None]:
        strIP: str = str(searchedIP)
        ipAddress: ipaddress.IPv4Address = IPv4Address(strIP)
        return self.get_log_by_key(ipAddress)


def createLogsList(path: str) -> SSHLogJournal:
    logJournal: SSHLogJournal = SSHLogJournal()
    logs: Iterator[str] = readFile(path)
    for log in logs:
        logJournal.appendEntry(log)

    return logJournal


# if __name__ == '__main__':
#     logJournal = createLogsList("SSHTEST.log")
#     print(logJournal.logsList)
#     logs = readFile("SSHTEST.log")
#     ipAddress = IPv4Address('113.118.187.34')
#     otherIpAddress = IPv4Address('183.62.140.253')
#     date = datetime(2023, 12, 10, 11, 40, 46)
#     print("Len test:")
#     print(len(logJournal))
#     print("Contains test:")
#     print("Test dla obiektu AcceptedPassword: ")
#     firstLine = next(logs)
#     test = AcceptedPassword(firstLine)
#     print(test in logJournal)
#     print("Test dla stringa nieznajdującego się w logJournal:")
#     print("lalalal" in logJournal)
#
#     print("getLogsWithGivenIP: ")
#     logsWithGivenIP = logJournal.getLogsWithGivenIp(ipAddress)
#     print(logsWithGivenIP)
#
#     print("Iterator:")
#     for log in logJournal:
#         print(log)
#
#     print("__getattr__ dla indexu:")
#     print(logJournal.get_log_by_key(2))
#     print("__getattr__ dla adresu ip:")
#     print(logJournal.get_log_by_key(otherIpAddress))
#     print("__getaddr__ dla daty:")
#     print(logJournal.get_log_by_key(date))
