from task3 import SSHLogJournal, createLogsList
from datetime import datetime
import re
from task1 import SSHLogEntry
class SSHUser:
    def __init__(self, username, lastSeen):
        self.username = username
        self.lastSeen = lastSeen
    def validate(self):
        return re.compile(r'^[a-z_][a-z0-9_-]{0,31}$').match(self.username) is not None
    def __repr__(self):
        return f"User: {self.username}, last seen: {self.lastSeen}\n"

if __name__ == '__main__':
    logJournal = createLogsList("SSHTEST.log")
    usersAndLogs = []
    for log in logJournal:
        usersAndLogs.append(log)

    usersAndLogs.append(SSHUser("!Testuje_B$rdzo_Ni3Po0#rawna_nazweuzytkownika_ktora_nie_przejdzie_walidacji", datetime.now()))
    usersAndLogs.append(SSHUser("user1337", datetime.now()))
    print("Testowanie kaczego typowania: (validate() na czwartym indeksie zwroci False, poniewaz nazwa uzytkownika nie przechodzi walidacji)")
    for element in usersAndLogs:
        if isinstance(element, SSHUser):
            print(str(element.validate())+" "+element.username)