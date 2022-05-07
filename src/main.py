import os

from utils import JsonManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())


def exampleJsonRead():
    data = JsonManager.readFile('./assets/squad.json')
    print(data)
    print(JsonManager.prettyPrint(data))


exampleJsonRead()
