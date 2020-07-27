class guardNode:
    def __init__(self, bananas):
        self.bananas = bananas
        self.loop = []
        self.bored = []
        
def inLoop(a,b):
    if(a == b):
        return False
    if(a > b):
        c = a
        a = b
        b = c
    powerOfTwo = int(b/a)
    powerOfTwo += 1
    return powerOfTwo & (powerOfTwo - 1) 
    
def disconnect(nodeList, node):
    for item in node.bored:
        item.bored.remove(node)
    for item in node.loop:
        item.loop.remove(node)
    nodeList.remove(node)

def removePair(nodeList, node1, node2):
    disconnect(nodeList, node1)
    disconnect(nodeList, node2)
    
def solution(banana_list):
    guards = [guardNode(banana_list[a]) for a in range(len(banana_list))]
    workingGuards = 0

    for a in range(0, len(banana_list) - 1):
        for b in range(a + 1, len(banana_list)):
            if(inLoop(banana_list[a], banana_list[b])):
                guards[a].loop.append(guards[b])
                guards[b].loop.append(guards[a])
            else:
                guards[a].bored.append(guards[b])
                guards[b].bored.append(guards[a])

    if(len(banana_list)%2 == 1):
        single=guardNode(-1)
        for guard in guards:
            single.bored.append(guard)
            guard.bored.append(single)
        guards.append(single)
        workingGuards -= 1

    while len(guards) > 0:
        guards.sort(key = lambda x: len(x.bored), reverse = True)
        currentGuard = guards[0]
        good = False
        for pair in guards[1:]:
            if(pair in currentGuard.loop):
                removePair(guards, currentGuard, pair)
                good = True
                break
        if not good:
            workingGuards += 2
            removePair(guards, currentGuard, guards[1])

    return workingGuards
    
print(solution([1, 7, 3, 21, 13, 19]))
