import os
import json
import re

def cleanJsonTrailingCommas(string):
    string = re.sub(",[ \t\r\n]+}", "}", string)
    string = re.sub(",[ \t\r\n]+\]", "]", string)

    return string

def loadJsonFileFromPath(path):
    with open(path, 'r') as f:
        return json.loads(cleanJsonTrailingCommas(f.read()))

def forEachFilePathInDirectory(directoryPath, action):
    for filename in os.listdir(directoryPath):
        f = os.path.join(directoryPath, filename)
        if os.path.isfile(f):
            action(f)

def processJsonFile(path):
    print("")

    if not path.endswith(".json"):
        print(f"Ignoring {path} because it doesn't end with '.json'")
        return

    fileName = os.path.basename(path)[:-5]
    print(f"{path} file name is {fileName}")

    print(f"Loading {path} into JSON object")
    jsonObj = loadJsonFileFromPath(path)

    jsonObj["name"] = f"MINI #{fileName}"
    jsonObj["edition"] = int(fileName)
    jsonObj["image"] = f"https://ipfs.io/ipfs/Qmf4o9ZgJUG28Cct967WurRz1GEkBBNNeQEHvhhQzNuGhj/{fileName}.png"
    #jsonObj["image"] = f"{fileName}.png"


    outFolderName = "JSON_edited"

    if not os.path.exists(outFolderName):
        os.makedirs(outFolderName)

    outPath = path.replace("JSON", outFolderName)
    print(f"Writing result to {outPath}")

    with open(outPath, 'w') as f:
        json.dump(jsonObj, f, indent=4)

def main():
    forEachFilePathInDirectory("./JSON", processJsonFile)
    pass

if __name__ == '__main__':
    main()
