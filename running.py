def solution(time, time_limit):
    savedBunnies = []
    closed = False
    start = 0

    while closed == False:
        startPos = time[start]
        
        if(time_limit < 0):
            closed = True

        if(min(startPos) == 0):
            startPosTemp = sorted(startPos)
            delta = startPosTemp[1]
            nextPos = time[startPos.index(startPosTemp[1])]
            start = time.index(nextPos)
        else:
            delta = min(startPos)
            nextPos = time[startPos.index(min(startPos))]
            start = time.index(nextPos)

        if(time.index(startPos) - 1 in savedBunnies):
            pass
        else:
            if(startPos != time[0] and startPos != time[len(time) - 1]):
                savedBunnies.append(time.index(startPos) - 1)

        time_limit -= delta
        print(startPos, start, time_limit)

    return savedBunnies

print(solution([[0, 2, 2, 2, -1], 
                            [9, 0, 2, 2, -1], 
                            [9, 3, 0, 2, -1], 
                            [9, 3, 2, 0, -1], 
                            [9, 3, 2, 2, 0]], 1))

# [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3