def inLoop(a, b):
    aCopy, bCopy = a, b
    steps = []

    if(a == b):
        return False

    while a != b:
        steps.append([a,b])
        if(a < b):
            b -= a
            a += a
        elif(a > b):
            a -= b
            b += b

        if([a,b] in steps):
            return True
            break

        if((a, b) == (aCopy, bCopy)):
            return True
            break

    return False

def remove(guards, ref):
    for a in range(len(guards)):
        b = 0 
        while b < len(guards[a]):
            if(guards[a][b]==ref):
                guards[a].pop(b)
            b+=1 
    guards[ref]=[-1]

def solution(banana_list):
    guards = [[] for x in range(len(banana_list))]
    workingGuards = 0

    if(len(banana_list) == 2 and banana_list[0] == banana_list[1]):
        return 2
    elif(len(banana_list) == 2):
        if(inLoop(banana_list[0], banana_list[1])):
            return 0
        else:
            return 2
    
    for guardOne in range(len(guards)):
        for guardTwo in range(len(guards)):
            if(inLoop(guardOne, guardTwo)):
                guards[guardOne].append(guardTwo)
    
    leftToProcess = len(banana_list)
    while leftToProcess > 0:
        minGuards = 0

        sortedGuards = sorted(guards, key=len)
        minGuards = guards.index(sortedGuards[0])

        ### ???
        if((len(guards[minGuards])) == 0 or (len(guards[minGuards])==1 and
                guards[minGuards][0] == guards[minGuards]) and guards[minGuards] !=
                [-1]):
            remove(guards, minGuards)
            leftToProcess-=1
            workingGuards+=1
        else:
            min_node=guards[minGuards][0]
            for i in range(len(guards[minGuards])):
                if(i!=0 and guards[minGuards][i]!=minGuards and len(guards[guards[minGuards][i]])<len(guards[min_node])):
                    min_node=guards[minGuards][i]
            if(guards[min_node]!=[-1]):
                remove(guards, minGuards)
                remove(guards, minGuards)
                leftToProcess-=2
        ### ??? write out on paper

    return workingGuards

#print(inLoop(1,7))
print(solution([1, 7, 3, 21, 13, 19]))
# [1, 7, 3, 21, 13, 19]