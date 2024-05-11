from lab6.functionalities import createLog, get_ipv4s_from_log
import ipaddress
from abc import ABC, abstractmethod
class SSHLogEntry(ABC):
    def __init__(self, log):
        self.date, self.hostname, self.pidNumber, self.description = createLog(log)
        self.rawEntry = log

    def __str__(self):
        return f"date: {self.date}, hostname: {self.hostname}, pidNumber: {self.pidNumber}, description: {self.description}"
    
    def __repr__(self):
        return f"{type(self).__name__}(date='{self.date}', hostname=''{self.hostname}, pidNumber='{self.pidNumber}', descripiton='{self.description}')"
    
    def __eq__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.pidNumber == other.pidNumber
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.date > other.date
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.date < other.date
        return NotImplemented

    def getIpObject(self):
        entryIp = get_ipv4s_from_log(self.description)
        if entryIp:
            return ipaddress.IPv4Address(entryIp[0])
        else:
            None

    @abstractmethod
    def validate(self):
        pass

    @property
    def hasIP(self):
        return self.getIpObject() is not None
    
    def getRawEntry(self):
        return self.rawEntry

# log = "Dec 31 09:13:09 LabSZ sshd[1759]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=95.188.84.199"

# obj = SSHLogEntry(log)

# print(obj.getIpObject())