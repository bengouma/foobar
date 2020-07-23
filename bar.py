def convertBase(n, b):
    digits = '0123456789abcdef'
    remainder_stack = []

    while n > 0:
        remainder = n % b
        remainder_stack.append(remainder)
        n = n // b
    newDigits = []

    while remainder_stack:
        newDigits.append(digits[remainder_stack.pop()])
    
    return int("".join(newDigits))

idList = []

def solution(n, b):
    k = len(n)
    if(2 <= k <= 9 and 2 <= b <= 10):
        idList.append(n)
        idNum = []
        results = []

        for item in idList[len(idList) - 1]:
            idNum.append(item)

        if(len(idList) == 1):
            xList = sorted(idNum, reverse=True)
            yList = sorted(idNum)
        else:
            xList = sorted(idList[len(idList) - 1], reverse=True)
            yList = sorted(idList[len(idList) - 1])

        if(b < 10):
            x = int("".join(xList), b)
            y = int("".join(yList), b)
            z = x - y
            z = convertBase(z, b)
        else:
            x = int("".join(xList))
            y = int("".join(yList))
            z = x - y

        strz = str(z).zfill(k)

        if(n == strz):
            return 1
        elif(n == 0):
            return 1
        else:
            for item in idList:
                if(item == strz):
                    return len(idList) - idList.index(item)
            return solution(strz, b) 
    else:
        return 1

solution('1111', 10)
