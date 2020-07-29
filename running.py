import collections

def locationOfItems(listItem, item):
    startNum = -1
    location = []
    while True:
        try:
            loc = listItem.index(item, startNum + 1)
        except ValueError:
            break
        else:
            location.append(loc)
            startNum = loc
    
    return location

def solution(time, time_limit):
    savedBunnies = []
    closed = False
    start = 0

    while closed == False:
        currentPos = time[start]
        
        if(time_limit < 0):
            closed = True

        if(min(currentPos) == 0):
            currentPosTemp = sorted(currentPos)
            delta = currentPosTemp[1]
            nextPos = time[currentPos.index(currentPosTemp[1])]
            if(time.index(nextPos) - 1 in savedBunnies):
                nextPos = time[locationOfItems(currentPos, time.index(nextPos))[1]]
            start = time.index(nextPos)

        else:
            delta = min(currentPos)
            nextPos = time[currentPos.index(min(currentPos))]
            if(time.index(nextPos) - 1 in savedBunnies):
                nextPos = time[locationOfItems(currentPos, time.index(nextPos))[1]]
            start = time.index(nextPos)
            
        if(currentPos != time[0] and currentPos != time[len(time) - 1]):
            savedBunnies.append(time.index(currentPos) - 1)

        time_limit -= delta
        
        if(len(savedBunnies) == len(time) - 2):
            break

    return savedBunnies

# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))

print(solution([[0, 2, 2, 2, -1], 
                            [9, 0, 2, 2, -1], 
                            [9, 3, 0, 2, -1], 
                            [9, 3, 2, 0, -1], 
                            [9, 3, 2, 2, 0]], 1))
