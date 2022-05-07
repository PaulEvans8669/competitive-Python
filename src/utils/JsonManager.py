import json


class JsonManager:

    @staticmethod
    def readFile(path):
        with open(path, 'r') as f:
            return json.load(f)

    @staticmethod
    def prettyPrint(data):
        print(json.dumps(data, indent=4, sort_keys=True))
