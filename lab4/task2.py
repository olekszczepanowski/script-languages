import os 
import sys
path = os.environ["PATH"]

for folder in path.split(';'):
    print(folder)
    if '--exe' in sys.argv:
        try:
            for file in os.listdir(folder):
                if file.endswith('.exe'):
                    print(file)
        except:
                pass