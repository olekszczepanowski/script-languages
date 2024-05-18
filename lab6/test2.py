import pytest
from functionalities import get_ipv4s_from_log

def test_correct_ipv4_address_extraction():
    entry = "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
    expected_ipv4 = ["173.234.31.186"]
    extracted_ipv4 = get_ipv4s_from_log(entry)
    assert extracted_ipv4 == expected_ipv4


def test_incorrect_ipv4_address():
    entry = "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 666.777.88.213 port 38926 ssh2"
    ips = get_ipv4s_from_log(entry)
    assert ips == []


def test_no_ipv4_address():
    entry = "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from port 38926 ssh2"
    extracted_ipv4 = get_ipv4s_from_log(entry)
    assert extracted_ipv4 == []
