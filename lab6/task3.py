import re
from lab6.task2 import FailedPassword, AcceptedPassword, Error, Other
from lab6.functionalities import readFile, get_ipv4s_from_log
from ipaddress import IPv4Address
from datetime import datetime
from lab6.task1 import SSHLogEntry


class SSHLogJournal:
    def __init__(self):
        self.logsList = []
        self.ipDict = {}
        self.dateDict = {}

    @staticmethod
    def validateLogType(log):
        if re.search(r"Accepted password for", log):
            return AcceptedPassword(log)
        elif re.search(r"Failed password for", log):
            return FailedPassword(log)
        elif re.search(r"error:", log):
            return Error(log)
        else:
            return Other(log)

    def appendDateDict(self, log):
        if log.date in self.dateDict:
            self.dateDict[log.date].append(log)
        else:
            self.dateDict[log.date] = [log]

    def appendIpDict(self, log):
        ips = get_ipv4s_from_log(log.description)
        for ip in ips:
            if ip in self.ipDict:
                self.ipDict[ip].append(log)
            else:
                self.ipDict[ip] = [log]

    def appendEntry(self, entry):
        logObject = self.validateLogType(entry)
        if logObject.validate():
            self.logsList.append(logObject)
            self.appendDateDict(logObject)
            self.appendIpDict(logObject)
        else:
            entryOther = Other(entry)
            self.logsList = (entryOther)
            self.appendDateDict(entryOther)
            self.appendIpDict(entryOther)

    def __len__(self):
        return len(self.logsList)

    def __contains__(self, item):
        if not isinstance(item, SSHLogEntry):
            return False
        strItem = str(item)
        for log in self.logsList:
            if str(log) == strItem:
                return True

        return False

    def __iter__(self):
        return iter(self.logsList)

    def __getattr__(self, key):
        if isinstance(key, int):
            return self.logsList[key]
        elif isinstance(key, IPv4Address):
            return self.ipDict.get(str(key), None)
        elif isinstance(key, datetime):
            return self.dateDict.get(key, None)
        else:
            raise KeyError("Nieprawidlowy klucz.")

    def getLogsWithGivenIp(self, searchedIP):
        strIP = str(searchedIP)
        ipAddress = IPv4Address(strIP)
        return self.__getattr__(ipAddress)


def createLogsList(path):
    logJournal = SSHLogJournal()
    logs = readFile(path)
    for log in logs:
        logJournal.appendEntry(log)

    return logJournal





if __name__ == '__main__':
    logJournal = createLogsList("SSHTEST.log")
    print(logJournal.logsList)
    print(logJournal.logsList.getRawEntry())
    # logs = readFile("SSHTEST.log")
    # ipAddress = IPv4Address('113.118.187.34')
    # otherIpAddress = IPv4Address('183.62.140.253')
    # date = datetime(2023, 12, 10, 11, 40, 46)
    # print("Len test:")
    # print(len(logJournal))
    # print("Contains test:")
    # print("Test dla obiektu AcceptedPassword: ")
    # firstLine = next(logs)
    # test = AcceptedPassword(firstLine)
    # print(test in logJournal)
    # print("Test dla stringa nieznajdującego się w logJournal:")
    # print("lalalal" in logJournal)
    #
    # print("getLogsWithGivenIP: ")
    # logsWithGivenIP = logJournal.getLogsWithGivenIp(ipAddress)
    # print(logsWithGivenIP)
    #
    # print("Iterator:")
    # for log in logJournal:
    #     print(log)
    #
    # print("__getattr__ dla indexu:")
    # print(logJournal.__getattr__(2))
    # print("__getattr__ dla adresu ip:")
    # print(logJournal.__getattr__(otherIpAddress))
    # print("__getaddr__ dla daty:")
    # print(logJournal.__getattr__(date))
