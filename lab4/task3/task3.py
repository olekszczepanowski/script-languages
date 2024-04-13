import sys
import time
LINES = "--lines="
BYTES = "--bytes="
FOLLOW = "--follow"
DEFAULT_N = 10
FOLLOW_MODE = False
SLEEP_DELAY = 0.5
def tail():
    lineCount = DEFAULT_N
    isFollow = FOLLOW_MODE
    lines = None
    filePath = None
    byteCount = None
    isByte = False
    isLines = False

    for i in range(1, len(sys.argv)):
        if "." in sys.argv[i] and not sys.argv[i].startswith("--"):
            filePath=sys.argv[i]
        if sys.argv[i].startswith(LINES):
            try:
                lineCount = int(sys.argv[i].split("=")[1])
                isLines = True
            except:
                pass
        if sys.argv[i].startswith(BYTES):
            try:
                byteCount = int(sys.argv[i].split("=")[1])
                isByte = True
            except:
                pass
        if sys.argv[i] == FOLLOW:
            isFollow = True

    
    if isLines and isByte:
        print("Blad. Nie mozna podac ilosci linii i bajtow jednoczesnie.")
        return
    

    if filePath:
        if isByte:
            try:
                file = open(filePath, "rb")
                file.seek(0, 2)
                file.seek(max(file.tell() - byteCount, 0), 0)
                lines = file.read(byteCount)
                file.close()
                print(lines)
            except:
                print("Blad odczytu pliku z wykorzystaniem --bytes.")
        elif not isByte:
            try:
                file = open(filePath, "r")
                lines = file.readlines()[-lineCount:]
                file.close()
                for line in lines:
                    print(line)
            except:
                print("Blad odczytu pliku z wykorzystaniem --lines.")
    else:
        try:
            lines = sys.stdin.readlines()[-lineCount:]
            for line in lines:
                print(line)
        except:
            print("Blad odczytu danych z wejscia standardowego.")
    
    if isFollow and filePath:
        if not isByte:
            while True:
                try:
                    file = open(filePath, "r")
                    newLines = file.readlines()
                    file.close()
                    if len(newLines) > len(lines):
                        for line in newLines[len(lines):]:
                            print(line)
                    lines = newLines
                    time.sleep(SLEEP_DELAY)
                except:
                    print("Blad odczytu pliku.")
                    break
        else:
            while True:
                try:
                    file = open(filePath, "rb")
                    file.seek(0, 2)
                    file.seek(max(file.tell() - byteCount, 0), 0)
                    newLines = file.read()
                    file.close()
                    if(newLines != lines):
                        print(newLines)
                    lines = newLines
                    time.sleep(SLEEP_DELAY)
                except:
                    print("Blad odczytu pliku.")
                    break


if __name__ == '__main__':
    tail()



