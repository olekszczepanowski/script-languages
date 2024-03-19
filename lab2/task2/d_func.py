import sys

def graphicDownloads():
    graphicExtensions = ["jpg","gif","jpeg","xbm"]
    f = sys.stdin
    extTmp = 0;
    otherTmp = 0;
    for line in f:
        try:
            lineSplitted = line.split(" ")
            path = lineSplitted[-4]
            pathSplitted = path.split(".")
            extension = pathSplitted[-1]
            if(extension in graphicExtensions):
                extTmp+=1
            else:
                otherTmp+=1
        except ValueError:
           pass
    f.close()
    print("Stosunek plików graficznych do innych: "+ str(round(extTmp/otherTmp,3)))

graphicDownloads()