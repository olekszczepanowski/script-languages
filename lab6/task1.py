from datetime import datetime
from typing import Optional
from datetime import datetime
from functionalities import createLog, get_ipv4s_from_log
import ipaddress
from abc import ABC, abstractmethod
from typing import List


class SSHLogEntry(ABC):
    def __init__(self, log: str) -> None:
        self.date: datetime
        self.hostname: str
        self.pidNumber: int
        self.description: str
        log_parsed = createLog(log)
        if log_parsed is not None:
            self.date, self.hostname, self.pidNumber, self.description = log_parsed
        else:
            self.date = datetime.now()
            self.hostname = "default"
            self.pidNumber = -1
            self.description = "default"
        self.rawEntry = log

    def __str__(self) -> str:
        return f"date: {self.date}, hostname: {self.hostname}, pidNumber: {self.pidNumber}, description: {self.description}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(date='{self.date}', hostname=''{self.hostname}, pidNumber='{self.pidNumber}', descripiton='{self.description}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.pidNumber == other.pidNumber
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.date > other.date
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.date < other.date
        return NotImplemented

    def getIpObject(self) -> Optional[ipaddress.IPv4Address]:
        entryIp: Optional[List[str]] = get_ipv4s_from_log(self.description)
        if entryIp:
            return ipaddress.IPv4Address(entryIp[0])
        return None

    @abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def hasIP(self) -> bool:
        return self.getIpObject() is not None

    def getRawEntry(self) -> str:
        return self.rawEntry

    def append(self, log):
        pass

# log = "Dec 31 09:13:09 LabSZ sshd[1759]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=95.188.84.199"
#
# obj = SSHLogEntry(log)
#
# print(obj.getIpObject())
