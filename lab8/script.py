import os
from datetime import datetime

from lab6.task3 import createLogsList, SSHLogJournal


def createLogList(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    logs_list = createLogsList(path)
    return logs_list


def createRawEntriesList(list):
    raw_entries_list = []
    for entry in list:
        modified_entry = changeRawEntry(entry.getRawEntry())
        raw_entries_list.append(modified_entry)
    return raw_entries_list


def filterLogList(base_list, start_date, end_date):
    filtered_list = []
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid date format. Usage: (YYYY-MM-DD)')
    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid date format. Usage: (YYYY-MM-DD)')
    for entry in base_list:
        if start_date <= entry.date <= end_date:
            filtered_list.append(entry)
    return filtered_list


def changeRawEntry(entry):
    modified_entry = entry
    if len(modified_entry) > 50:
        modified_entry = modified_entry[:50] + "..."
    return modified_entry


logs = createLogList("TEST.log")
raw_entries = createRawEntriesList(logs)
# print(raw_entries)
date_dec_28 = datetime(year=2023, month=12, day=28, hour=0, minute=0, second=0)
date_dec_30 = datetime(year=2023, month=12, day=30, hour=23, minute=59, second=59)
filtered_logs = filterLogList(logs, "2023-12-28", "2023-12-30")
print(filtered_logs)
