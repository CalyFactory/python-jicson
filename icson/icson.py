
def fromWeb(icsFileUrl):
    return 'hi'

def fromFile(icsFilePath):
    f = open(icsFilePath, 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    return 'hi'

def fromText(icsFileText):
    return 'hi'
