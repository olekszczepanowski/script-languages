import os 
import sys

path = os.environ["PATH"]
def func():
    for folder in path.split(';'):
        sys.stdout.write(folder+"\n")
        if "--exe" in sys.argv:
            try:
                for file in os.listdir(folder):
                    if file.endswith('.exe'):
                        sys.stdout.write(file + "\n")
            except:
                    pass

if __name__ == '__main__':
    func()