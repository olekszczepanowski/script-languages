import sys
import os
import subprocess
def func():
    if len(sys.argv) < 2:
        sys.exit()
    folderPath = sys.argv[1]
    if folderPath[-1] == '"':
        folderPath = folderPath[:-1]
    try:
        files = os.listdir(folderPath)
    except:
        print("Blad odczytu folderu: " + folderPath)
        sys.exit()

    fileStats = {}

    for stat in files:
        if stat.endswith(".txt"):
            try:
                filePath = os.path.join(folderPath, stat)
                result = subprocess.run(['java','-cp', 'java_files/src','Main', filePath], 
                                    input=filePath, 
                                    encoding='ascii', 
                                    capture_output=True)
                result = result.stdout.strip()
                resultTab = result.split("\t")  
                if len(resultTab) >= 6:
                    filePathTsv = resultTab[0]
                    chars = int(resultTab[1])
                    words = int(resultTab[2])
                    lines = int(resultTab[3])
                    charMostUsed = resultTab[4]
                    charMostUsedFrequency = int(resultTab[6])
                    mostUsedWord = resultTab[5]
                    mostUsedWordFrequency = int(resultTab[7])
                    fileStats[stat] = {
                        "filePathTsv": filePathTsv,
                        "chars": chars,
                        "words": words,
                        "lines": lines,
                        "charMostUsed": charMostUsed,
                        "charMostUsedFrequency": charMostUsedFrequency,
                        "mostUsedWord": mostUsedWord,
                        "mostUsedWordFrequency": mostUsedWordFrequency
                    }
            except:
                print("Błąd oczytu pliku: "+filePath)

    totalChars = 0
    totalWords = 0
    totalLines = 0
    charMostUsed = ""
    wordMostUsed = ""
    tmp_charMostUsedFreq = 0
    tmp_wordMostUsedFreq = 0

    for data in fileStats.values():
        totalChars += data["chars"]
        totalWords += data["words"]
        totalLines += data["lines"]
        if(data["charMostUsedFrequency"]>tmp_charMostUsedFreq):
            tmp_charMostUsedFreq = data["charMostUsedFrequency"]
            charMostUsed = data["charMostUsed"]
        if(data["mostUsedWordFrequency"]>tmp_wordMostUsedFreq):
            tmp_wordMostUsedFreq = data["mostUsedWordFrequency"]
            wordMostUsed = data["mostUsedWord"]

    print("Ilosc odczytanych plikow: ", len(fileStats))
    print("Ilosc znakow:", totalChars)
    print("Ilosc slow:", totalWords)
    print("Ilosc linii:", totalLines)
    print("Najczesciej uzywany znak: ", charMostUsed)
    print("Najczesciej uzywane slowo: ", wordMostUsed)

if __name__ == '__main__':
    func()

    