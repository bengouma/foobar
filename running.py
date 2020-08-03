from itertools import permutations

def powerset(listItem):
    x = len(listItem)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, listItem) if i & mask]

def floyd(times):
    for k in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])

    return times

def solution(times, time_limit):
    numOfBunnies = len(times) - 2
    ids = []
    savedBunnies = []

    if(len(times) <= 2):
        return []

    for item in range(numOfBunnies):
        ids.append(item)

    pset = powerset(ids)
    pset = sorted(pset)
    
    spaths = floyd(times)

    for item in times:
        if(times[item][item] < 0):
            return [num for num in range(0, len(times) - 2)]

    for sub in pset:
        for permutation in permutations(sub):
            subsum = 0
            prev = 0
            nextItem = len(times) - 1
            
            for idNum in permutation:
                nextItem = idNum + 1
                subsum += spaths[prev][nextItem]
                prev = nextItem

            subsum += spaths[prev][len(times) - 1]

            if(subsum <= time_limit and len(sub) > len(savedBunnies)):
                savedBunnies = sub
                if(len(savedBunnies) == numOfBunnies):
                    break
            else:
                pass
            
    return savedBunnies

# print(solution([[0, 1, 1, 1, 1], 
#                             [1, 0, 1, 1, 1], 
#                             [1, 1, 0, 1, 1], 
#                             [1, 1, 1, 0, 1], 
#                             [1, 1, 1, 1, 0]], 3))

# print(solution ([[0, 2, 2, 2, -1], 
#                             [9, 0, 2, 2, -1], 
#                             [9, 3, 0, 2, -1], 
#                             [9, 3, 2, 0, -1], 
#                             [9, 3, 2, 2, 0]], 1))
