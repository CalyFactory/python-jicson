import json
import sys
from urllib.request import urlopen
import io

sys.setrecursionlimit(10000)

class StreamObject:

    def __init__(self, type, uri = None, auth = None, filePath = None, text = None):
        self.type = type 
        self.uri = uri 
        self.auth = auth
        self.filePath = filePath
        self.text = text
        
        if self.type == "web":
            self.response = urlopen(uri)    
        elif self.type == "file":
            self.file = open(filePath)
        elif self.type == "text":
            self.buf = io.StringIO(text)
        else:
            self.buf = io.StringIO(text)
    
    def readline(self):
        if self.type == "web":
            line = (self.response.readline().decode('utf-8'))
        elif self.type == "file":
            line = (self.file.readline())
        elif self.type == "text":
            line = (self.buf.readline())
        else:
            line = (self.buf.readline())
        
        line = line.rstrip('\n')
        return line

def fromWeb(icsFileUrl):
    streamObject = StreamObject(
        type = "web",
        uri = icsFileUrl
    )
    return parseChild({}, streamObject)

def fromFile(icsFilePath):
    streamObject = StreamObject(
        type = "file",
        filePath = icsFilePath
    )
    return parseChild({}, streamObject)

def fromText(icsFileText):
    streamObject = StreamObject(
        type = "text",
        text = icsFileText
    )
    return parseChild({}, streamObject)

def parseChild(json, fileObject):
    while True:
        line = fileObject.readline()
        if not line: 
            return json

        line = line.rstrip('\n')

        separator = line.find(":")
        
        if separator == -1:
            continue

        key = line[:separator]
        value = line[separator+1:]

        if key == "BEGIN":
            if value not in json:
                json[value] = []
            json[value].append(parseChild({}, fileObject))
        elif key == "END":
            return json
        else:
            json[key] = value

"""

def fromFile(icsFilePath):

    json = {}

    with open(icsFilePath) as fileObject:

        keyStack = []
        depthStack = []
        depthCounter = 0
        c = 0
        for line in fileObject:
            line = line.rstrip('\n')

            separator = line.find(":")
            
            if separator == -1:
                continue

            key = line[:separator]
            value = line[separator+1:]
            print(key)
            if key == "BEGIN":
                keyStack.append(value)
                depthStack.append({})

                innerJson = json
                for prevKey in keyStack:
                    if prevKey not in json:
                        json[prevKey] = []
                    innerJson = innerJson[prevKey]
                position = innerJson
            elif key == "END":
                jsonObject = depthStack.pop()
                innerJson = json
                for prevKey in keyStack:
                    if prevKey not in json:
                        json[prevKey] = []
                    innerJson = innerJson[prevKey]
                print("inner : " + str(innerJson))
                print("json : " + str(jsonObject))
                print("stack : " + str(keyStack))
                position.append(jsonObject)
                print(json)
                keyStack.pop()
            else:
                innerJson = depthStack[len(depthStack)-1]
                innerJson[key] = value
                print(innerJson)
            c+=1
#            print(json)
            if c==71:
                break
            print(key + "//" + value)
    print(json)
    f = open("./json.json",'w')
    f.write(str(json))
    f.close()
    return 'hi'
"""