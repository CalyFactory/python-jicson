import json
import sys
sys.setrecursionlimit(10000)


def fromWeb(icsFileUrl):
    return 'hi'

def fromFile2(icsFilePath):
    with open(icsFilePath) as fileObject:
        json = read({}, fileObject)
    print(json)
    return json
def read(json, fileObject):
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


#        print(json)
        if key == "BEGIN":
            if value not in json:
                json[value] = []
            json[value].append(read({}, fileObject))
        elif key == "END":
            return json
        else:
            json[key] = value


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

def fromText(icsFileText):
    return 'hi'
