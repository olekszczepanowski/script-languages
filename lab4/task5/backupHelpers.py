import os
import sys

def pathVerifier():
    folderPath = None  
    if len(sys.argv) < 2:
        print('Brak podanego folderu.')
    else:
        provided_path = sys.argv[1]
        if not os.path.isdir(provided_path):
            print(f'Brak folderu: {provided_path}')
        else:
            folderPath = provided_path
    return folderPath

def getBackupDir():
    backupDir = os.getenv("BACKUPS_DIR",os.path.join(os.path.expanduser('~'), '.backups'))
    return backupDir