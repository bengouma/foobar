import math

class guardNode:
    def __init__(self, bananas):
        self.bananas = bananas
        self.loop = []
        self.discard = []

def inLoop(a, b):
    powerOfTwo = int((a + b)/math.gcd(a, b))
    return bool(powerOfTwo & (powerOfTwo - 1))

def disconnect(nodeList,node):
    for n in node.discard:
        n.discard.remove(node)
    for n in node.loop:
        n.loop.remove(node)
    nodeList.remove(node)

def removePair(nodeList,node1,node2):
    disconnect(nodeList,node1)
    disconnect(nodeList,node2)

def solution(banana_list):
    guards = [guardNode(banana_list[a]) for a in range(len(banana_list))]
    workingGuards = 0

    for a in range(0, len(banana_list) - 1):
        for b in range(a + 1, len(banana_list)):
            if(inLoop(banana_list[a], banana_list[b])):
                guards[a].loop.append(guards[b])
                guards[b].loop.append(guards[a])
            else:
                guards[a].discard.append(guards[b])
                guards[b].discard.append(guards[a])

    if(len(banana_list)%2==1):
        single=guardNode(-1)
        for guard in guards:
            single.discard.append(guard)
            guard.discard.append(single)
        guards.append(single)
        workingGuards-=1

    while len(guards) > 0:
        guards.sort(key = lambda x: len(x.discard), reverse = True)
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

#print(inLoop(1,7))
print(solution([1, 7, 3, 21, 13, 19]))
# [1, 7, 3, 21, 13, 19]