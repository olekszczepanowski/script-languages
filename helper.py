import re
def is_valid_ip(ip):
    regex = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$")
    return bool(regex.match(ip))

# Przykłady użycia
print(is_valid_ip("192.168.0.1"))    # True
print(is_valid_ip("666.777.88.213"))  # False
print(is_valid_ip("255.255.255.255")) # True
print(is_valid_ip("999.999.999.999")) # False