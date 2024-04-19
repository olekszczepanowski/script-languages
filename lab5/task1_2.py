import logging
import sys
from task1_1 import createDict, get_message_type

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


readFile(path)