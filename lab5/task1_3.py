import random
import statistics
import copy
from task1_1 import get_user_from_log, readFile

path = "TEST.log"

def getUsers(logs):
    users = {}

    for log in logs.values():
        user = get_user_from_log(log)
        if user:
            if user not in users:
                users[user] = []
            users[user].append(log)
    return users

def getRandomUserLogs(logs, n):
    if n<1:
        raise ValueError("Niepoprawna wartość n, wprowadź wartość większą od 0")
    users = getUsers(logs)
    if not users:
        return []
    
    selectedUser, userLogs = random.choice(list(users.items()))

    if len(userLogs) < int(n):
        return(selectedUser, userLogs)
    
    return(selectedUser, random.sample(userLogs, int(n)))

def printRandomUserLogs(logs, n):
    userAndLogs = getRandomUserLogs(logs,n)
    print("Wybrany użytkownik: ",userAndLogs[0])
    print("Wybrane wpisy:")
    for log in userAndLogs[1]:
        print(log)

def getSSH(logs):
    tmpLogs = copy.deepcopy(logs)
    sshConnections = {}
    for log in tmpLogs.values():
        logSSH = log["appComponent"]
        if logSSH not in sshConnections:
            sshConnections[logSSH] = []
        sshConnections[logSSH].append(log["date"])
    return sshConnections

def getSSHfromUsers(logs):
    tmpLogs = getUsers(logs)
    sshConnections = {}
    for user, userLogs in tmpLogs.items():
        for log in userLogs:
            user = get_user_from_log(log)
            if user not in sshConnections:
                sshConnections[user] = []
            sshConnections[user].append(log["date"])
    return sshConnections


def calculateStatistics(logs, global_=True):
    statisticsResults = {}
    
    if global_:
        sshConnections = getSSH(logs)
        allConnectionTimes = []
        for connectionTimes in sshConnections.values():
            connectionTimes = sorted(connectionTimes)
            firstConnection = connectionTimes[0]
            lastConnection = connectionTimes[-1]
            duration = (lastConnection-firstConnection).total_seconds()
            allConnectionTimes.append(duration)
    
        allMean = statistics.mean(allConnectionTimes)
        allStdev = statistics.stdev(allConnectionTimes) if len(allConnectionTimes) > 1 else 0
    
        statisticsResults['global'] = {'mean': allMean, 'stdev': allStdev}

        return statisticsResults
    else:
        sshConnections = getSSHfromUsers(logs)
        for user, connectionTimes in sshConnections.items():
            connectionTimes = sorted(connectionTimes)
            if len(connectionTimes) > 1:
                durations = [(connectionTimes[i + 1] - connectionTimes[i]).total_seconds() for i in range(len(connectionTimes) - 1)]
                meanDuration = statistics.mean(durations)
                stdevDuration = statistics.stdev(durations)
            else:
                meanDuration = 0
                stdevDuration = 0
            statisticsResults[user] = {'mean': meanDuration, 'stdev': stdevDuration}
        
        return statisticsResults

def getUsersLoggingFrequency(logs):
    users = getUsers(logs)
    mostFrequentUser = max(users, key=lambda user: len(users[user]))
    leastFrequentUser = min(users, key=lambda user: len(users[user]))
    output = "Most frequent user: " + str(mostFrequentUser) + " value: " + str(len(users[mostFrequentUser])) + "\nLeast frequent user: " + str(leastFrequentUser) + " value: " + str(len(users[leastFrequentUser]))
    return output


# logs = readFile(path)

# print(calculateStatistics(logs,False))


