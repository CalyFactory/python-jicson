
def fromWeb(icsFileUrl):
    return 'hi'

def fromFile(icsFilePath):
    with open(icsFilePath) as fileObject:
        for line in fileObject:
            line = line.rstrip('\n')
            print(line)
    return 'hi'

def fromText(icsFileText):
    return 'hi'
