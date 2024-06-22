import pytest
from task2 import AcceptedPassword, FailedPassword, Error, Other
from task3 import SSHLogJournal


@pytest.mark.parametrize("entry, expected_result", [
    ("Dec 10 11:40:46 LabSZ sshd[27962]: Accepted password for fztu from 113.118.187.34 port 31938 ssh2",
     AcceptedPassword),
    ("Dec 10 11:40:47 LabSZ sshd[27965]: Failed password for invalid user weblogic from 183.62.140.253 port 52751 ssh2",
     FailedPassword),
    (
    "Dec 10 11:40:48 LabSZ sshd[27965]: error: Received disconnect from 195.154.63.158: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]",
    Error),
    ("Dec 10 11:40:46 LabSZ sshd[27962]: pam_unix(sshd:session): session opened for user fztu by (uid=0)", Other)
])
def test_append(entry, expected_result):
    ssh_log_journal = SSHLogJournal()
    ssh_log_journal.appendEntry(entry)
    assert isinstance(ssh_log_journal.logsList[-1], expected_result)