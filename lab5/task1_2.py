import logging
import sys
from task1_1 import createDict, get_message_type, get_ipv4s_from_log, get_user_from_log

path = "TEST.log"

def readFile(filePath):
    try:
        file = open(filePath, "r")
        lines = file.readlines()
        logs = {}
        
        for index in range(0, len(lines)):
            line = lines[index]
            log = createDict(line)
            if log:
                logs[index] = log
                description = get_message_type(log["description"])
                sys.stdout.write(line)
                print()
                logger.debug("Odczytywanie linii, liczba przeczytanych bitów: %d", len(line.encode("utf-8")))
                if description == "udane logowanie" or description == "polaczenie zamkniete":
                    logger.info(description)
                elif description == "nieudane logowanie":
                    logger.warning(description)
                elif description == "wlamanie":
                    logger.critical(description)
                else:
                    logger.error(description)
                print()
        file.close()
        return logs
    except FileNotFoundError:
        logger.error("Plik nie został znaleziony: %s", filePath)
        return None
    except Exception as e:
        logger.error("Błąd odczytu pliku z podaną ścieżką: %s", e)
        return None

def runGetIpv4FromLog(logs):
    for log in logs.values():
        tab = get_ipv4s_from_log(log)
        if len(tab) > 0:
            print(tab)

def runGetUserFromLog(logs):
    for log in logs.values():
        user = get_user_from_log(log)
        if user:
            print(user)

def runGetMessageType(logs):
    for log in logs.values():
        print(get_message_type(log["description"]))

class StdoutFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO, logging.WARNING)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
outputFormat = logging.Formatter("%(levelname)s - %(message)s")

stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setLevel(logging.DEBUG)
stdoutHandler.setFormatter(outputFormat)
stdoutHandler.addFilter(StdoutFilter())
logger.addHandler(stdoutHandler)

stderrHandler = logging.StreamHandler(sys.stderr)
stderrHandler.setLevel(logging.ERROR)
stderrHandler.setFormatter(outputFormat)
logger.addHandler(stderrHandler)

def analyze_logs(args):
    # Ustawienie poziomu logowania
    log_level = getattr(logging, args.log_level)
    logger.setLevel(log_level)

    # Odczytanie pliku z logami
    logs = readFile(args.file)

    if args.subcommand == "ipv4":
        runGetIpv4FromLog(logs)
    elif args.subcommand == "user":
        runGetUserFromLog(logs)
    elif args.subcommand == "message":
        runGetMessageType(logs)


# logs = readFile(path)
# runGetIpv4FromLog(logs)