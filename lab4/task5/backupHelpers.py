import os
import sys

def pathVerifier():
    folderPath = None  
    if len(sys.argv) < 2:
        print('No folder path provided, enclose path in quotes if it contains spaces.')
    else:
        provided_path = sys.argv[1]
        if not os.path.isdir(provided_path):
            print(f'Folder not found: {provided_path}')
        else:
            folderPath = provided_path
    return folderPath

def getBackupDir():
    backupDir = os.getenv("BACKUPS_DIR",os.path.join(os.path.expanduser('~'), '.backups'))
    return backupDir