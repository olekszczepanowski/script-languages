import pytest
from datetime import datetime
from task2 import Other


def test_time_extraction():
    entry = "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2)"
    ssh_log_entry = Other(entry)
    assert ssh_log_entry.date == datetime(2023, 12, 10, 6, 55, 48)

def test_invalid_log():
    entry = "Invalid log"
    ssh_log_entry = Other(entry)
    assert ssh_log_entry.date == datetime.now()

def test_empty_log():
    entry = ""
    ssh_log_entry = Other(entry)
    assert ssh_log_entry.date == datetime.now()