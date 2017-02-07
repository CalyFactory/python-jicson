import json

def fromWeb(icsFileUrl):
    return 'hi'

def fromFile(icsFilePath):

    json = {}

    with open(icsFilePath) as fileObject:

        keyStack = []
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

                innerJson = json
                for prevKey in keyStack:
                    if prevKey not in json:
                        json[prevKey] = []
                    innerJson = json[prevKey]
                depthCounter = 0
            elif key == "END":
                keyStack.pop()
            else:
                innerJson = json
                for prevKey in keyStack:
                    if prevKey not in json:
                        json[prevKey] = {}
                    innerJson = json[prevKey]
                #innerJson[key] = value
#                print(innerJson)
                if depthCounter==0:
                    innerJson.append({})
                innerJson[depthCounter][key] = value
                
            c+=1
            print(json)
            if c==6:
                break
#            print(key + "//" + value)
    print(json)
    f = open("./json.json",'w')
    f.write(str(json))
    f.close()
    return 'hi'

def fromText(icsFileText):
    return 'hi'
