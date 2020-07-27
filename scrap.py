    guards = [[] for x in range(len(banana_list))]
    workingGuards = 0

    if(len(banana_list) == 2 and banana_list[0] == banana_list[1]):
        return 2
    elif(len(banana_list) == 2):
        if(inLoop(banana_list[0], banana_list[1])):
            return 0
        else:
            return 2

    for guardOne, a in enumerate(banana_list):
        for guardTwo, b in enumerate(banana_list):
            if(guardOne != guardTwo and inLoop(a, b)):
                guards[guardOne].append(guardTwo)
    
    leftToProcess = len(banana_list)
    print(guards)
    while leftToProcess > 0:
        minGuards = 0
        
        for a in range(len(guards)):
            if(a!=0 and (len(guards[a])<len(guards[minGuards]) or guards[minGuards]
                == [-1]) and guards[a]!=[-1]):
                minGuards=a
                print(minGuards)
        
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
                remove(guards, min_node)
                leftToProcess-=2

    return workingGuards