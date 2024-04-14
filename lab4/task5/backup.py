import sys
import os
import datetime
import shutil
import backupHelpers
import csv

def backup():
    folderPath = backupHelpers.pathVerifier()
    if folderPath is None:
        sys.exit()
    
    backupDir = backupHelpers.getBackupDir()

    timeStamp = datetime.datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    dirName = os.path.basename(folderPath)

    zipFileName = f"{timeStamp}-{dirName}.zip"  

    try:
        zipFilePath = shutil.make_archive(os.path.join(backupDir, zipFileName[:-4]), "zip", folderPath)  
    except :
        print("Błąd podczas kompresowania katalogu")
        sys.exit()
    
    if not os.path.isdir(backupDir):
        os.mkdir(backupDir)
    
    shutil.move(zipFilePath, os.path.join(backupDir, zipFileName))  

    row = [timeStamp, folderPath, zipFileName] 

    with open(os.path.join(backupDir, "backups.csv"), "a", newline='') as openedFile:
        writer = csv.writer(openedFile)
        writer.writerow(row)

    
    shutil.rmtree(folderPath)

if __name__ == '__main__':
   backup()

