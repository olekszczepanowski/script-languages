import random
import statistics
import datetime
import numpy as np
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


def calculateStatisticsForUser(sshConnections):
    statistics_results = {}
    for user, connection_times in sshConnections.items():
        connection_times = sorted(connection_times)
        if len(connection_times) > 1:
            durations = [(connection_times[i + 1] - connection_times[i]).total_seconds() for i in range(len(connection_times) - 1)]
            mean_duration = statistics.mean(durations)
            stdev_duration = statistics.stdev(durations)
        else:
            mean_duration = 0
            stdev_duration = 0
        statistics_results[user] = {'mean': mean_duration, 'stdev': stdev_duration}
    return statistics_results



def calculateStatistics(sshConnections):
    statistics_results = {}
    
    all_connection_times = []
    for connection_times in sshConnections.values():
        connection_times = sorted(connection_times)
        firstConnection = connection_times[0]
        lastConnection = connection_times[-1]
        duration = (lastConnection-firstConnection).total_seconds()
        all_connection_times.append(duration)
    
    all_mean = statistics.mean(all_connection_times)
    all_stdev = statistics.stdev(all_connection_times) if len(all_connection_times) > 1 else 0
    
    statistics_results['global'] = {'mean': all_mean, 'stdev': all_stdev}

    return statistics_results

def getUsersLoggingFrequency(logs):
    users = getUsers(logs)
    mostFrequentUser = max(users, key=lambda user: len(users[user]))
    leastFrequentUser = min(users, key=lambda user: len(users[user]))
    output = "Most frequent user: "+str(mostFrequentUser)+" value:"+str(len(users[mostFrequentUser]))
    +"\nLeast frequent user: "+str(leastFrequentUser)+" value:"+str(len(users[leastFrequentUser]))
    return output
logs = readFile(path)


sshConnections = getSSHfromUsers(logs)

print(calculateStatisticsForUser(sshConnections))


