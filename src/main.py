import os

import numpy as np
from PIL import Image

from utils import JsonManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())


#==================== JSON READER =====================

def exampleJsonRead():
    data = JsonManager.readFile('./assets/squad.json')
    #print(data)
    #print(JsonManager.prettyPrint(data))
    print(data.get('squadGang'))


# exampleJsonRead()


#=================== HAPPY NUMBERS ====================

def sumOfSquares(n):
    nBuffer = n
    result = 0
    while (n // 10) != 0 :
        lastDigit = n % 10
        result += lastDigit**2
        n = n//10
    result += n**2
    print("Sum of squares of ", nBuffer , " : ", result)
    return result

def processHappyNumber(n):
    n = sumOfSquares(n)
    while (n // 10) != 0:
        n = sumOfSquares(n)
    print("Final result :", n)
    return n

def findHappyNumbers(min=0, max=100):
    happyNumbers = []
    for i in range(min, max+1):
        if processHappyNumber(i) == 1:
            happyNumbers.append(i)
    print("Happy numbers between ", min, " and ", max, " are : ", happyNumbers)

#sumOfSquares(8)
#processHappyNumber(8)
findHappyNumbers(0, 10)


