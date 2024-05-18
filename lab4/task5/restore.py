import os
import sys
import shutil
import csv
import backupHelpers

def list_backups():
    backupDir = backupHelpers.getBackupDir()
    backup_history_path = os.path.join(backupDir, "backups.csv")

    if not os.path.exists(backup_history_path):
        print("Brak historii kopii zapasowych.")
        sys.exit(0)

    with open(backup_history_path, "r", newline='') as history_file:
        reader = csv.reader(history_file)
        backups = list(reader)

    if len(backups) < 1:
        print("Brak kopii zapasowych w historii.")
        sys.exit(0)

    print("Dostępne kopie zapasowe:")
    for index in range(len(backups)):
        print(f"{index + 1}. {backups[index][0]} : {backups[index][1]}")

def restore_backup(selected_backup_index):
    backupDir = backupHelpers.getBackupDir()
    backup_history_path = os.path.join(backupDir, "backups.csv")

    with open(backup_history_path, "r", newline='') as history_file:
        reader = csv.reader(history_file)
        backups = list(reader)

    if selected_backup_index < 1 or selected_backup_index > len(backups):
        print("Nieprawidłowy numer kopii zapasowej.")
        return

    selected_backup = backups[selected_backup_index - 1]
    zip_file = os.path.join(backupDir, selected_backup[2])

    folder_path = selected_backup[1]

    try:
        shutil.unpack_archive(zip_file, folder_path)  
        print("Kopia zapasowa została przywrócona pomyślnie.")
        del backups[selected_backup_index - 1]
        with open(backup_history_path, "w", newline='') as history_file:
            writer = csv.writer(history_file)
            writer.writerows(backups)
        
        os.remove(zip_file)
    except :
        print("Błąd podczas przywracania kopii zapasowej.")

if __name__ == '__main__':
    list_backups()
    selected_backup_index = int(input("Wybierz numer kopii zapasowej do przywrócenia: "))
    restore_backup(selected_backup_index)
