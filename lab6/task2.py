
import re
from lab6.task1 import SSHLogEntry
from lab6.functionalities import readFile, get_ipv4s_from_log, get_user_from_log, get_message_type, createLog


class FailedPassword(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)

    def validate(self):
        if re.search(r"Failed password for", self.description):
            return True
        else:
            return False
        
class AcceptedPassword(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)

    def validate(self):
        if re.search(r"Accepted password for", self.description):
            return True
        else:
            return False
        
class Error(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)

    def validate(self):
        if re.search(r"error:", self.description):
            return True
        else:
            return False
        
class Other(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log)

    def validate(self):
        return True

# logFailedPass = "Dec 31 09:13:16 LabSZ sshd[1761]: Failed password for invalid user app from 95.188.84.199 port 33116 ssh2"
# logAcceptPass = "Dec 10 16:17:52 LabSZ sshd[15139]: Accepted password for jmzhu from 183.62.156.108 port 18507 ssh2"
# logError = "Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]"
# logOther = "Dec 10 11:03:38 LabSZ sshd[25450]: Received disconnect from 183.62.140.253: 11: Bye Bye [preauth]"
# logDifferent = "Dec 10 11:03:40 LabSZ sshd[25448]: error:No more authentication methods available. [preauth]"
# objfp = FailedPassword(logDifferent)
# objap = AcceptedPassword(logDifferent)
# objerr = Error(logDifferent)
# objother = Other(logDifferent)

# print(objfp.validate())
# print(objap.validate())
# print(objerr.validate())
# print(objother.validate())

if __name__ == "__main__":
    logs = readFile("SSHTEST.log")
    print("Tworzymy obiekt AcceptedPassword z podanej linii:")
    firstLine = next(logs)
    entrySSH_accepted = AcceptedPassword(firstLine)
    print(firstLine)
    print("Czy jest to poprawny obiekt AcceptedPassword?:")
    print(entrySSH_accepted.validate())
    print("Czy ma ip?: ")
    print(entrySSH_accepted.hasIP)
    print("----------------------")
    print("Tworzymy niepoprawne obiekty AcceptedPassword;FailedPassword;Error z podanej linii:")
    secondLine = next(logs)
    print(secondLine)
    wrongEntrySSH_accepted = AcceptedPassword(secondLine)
    wrongEntrySSH_failed = FailedPassword(secondLine)
    wrongEntrySSH_error = FailedPassword(secondLine)
    print("Czy jest to poprawny obiekt AcceptedPassword?:")
    print(wrongEntrySSH_accepted.validate())
    print("Czy jest to poprawny obiekt FailedPassword?:")
    print(wrongEntrySSH_failed.validate())
    print("Czy jest to poprawny obiekt Error?:")
    print(wrongEntrySSH_error.validate())
    print("Tworzymy obiekt Other, który zawsze przechodzi walidacje. Czy jest poprawny?")
    entrySSH_other = Other(secondLine)
    print("Walidacja:")
    print(entrySSH_other.validate())
    print("Czy ma ip?:")
    print(entrySSH_other.hasIP)
    print("----------------------")
    thirdLine = next(logs)
    print("Tworzymy obiekt FailedPassword z podanej linii:")
    print(thirdLine)
    entrySSH_failed = FailedPassword(thirdLine)
    print("Czy jest to poprawny obiekt FailedPassword?:")
    print(entrySSH_failed.validate())
    print("Czy ma ip?: ")
    print(entrySSH_accepted.hasIP)
    print("----------------------")
    print("Tworzymy obiekt Error z podanej linii:")
    fourthLine = next(logs)
    print(fourthLine)
    entrySSH_error = Error(fourthLine)
    print("Czy jest to poprawny obiekt Error?:")
    print(entrySSH_error.validate())
    print("Czy ma ip?: ")
    print(entrySSH_accepted.hasIP)
    print("Czy moge utworzyc poprawny obiekt FailedPassword z podaną linią?")
    wrongEntrySSH_failed_2 = FailedPassword(fourthLine)
    print(wrongEntrySSH_failed_2.validate())
    print("Tworzymy obiekt Other, który zawsze przechodzi walidacje. Czy jest poprawny?")
    entrySSH_other_2 = Other(fourthLine)
    print(entrySSH_other_2.validate())
    print("----------------------")

    print("Testowanie funkcji magicznych")
    print("__eq__:")
    print("dla tych samych obiektów")
    mm_entrySHH_accepted = AcceptedPassword(firstLine)
    print(mm_entrySHH_accepted==mm_entrySHH_accepted)
    print("dla róznych obiektów, z tym samym numerem PID")
    print(entrySSH_other==entrySSH_accepted)
    print("dla róznych obiektów, z innym numerem PID")
    print(entrySSH_other==entrySSH_error)
    print("__gt__:")
    mm_other_1 = Other(firstLine)
    mm_other_2 = Other(fourthLine)
    print(mm_other_1>mm_other_2)
    print("__lt__:")
    print(mm_other_1<mm_other_2)
