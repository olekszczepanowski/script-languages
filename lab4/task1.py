import os
import sys

for key, value in os.environ.items():
    display = (len(sys.argv) == 1)
    if not display:
        for arg in sys.argv[1:]:
            if arg in key:
                display = True
                break

    if display:
        print(f"{key} = {value}")
