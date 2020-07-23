    elif(len(banana_list) == 2):
        guardOne, guardTwo = banana_list[0], banana_list[1]

        while guardOne != guardTwo:
            distractedGuards.append([guardOne, guardTwo])
            if(guardOne < guardTwo):
                guardTwo -= guardOne
                guardOne += guardOne
            elif(guardOne > guardTwo):
                guardOne -= guardTwo
                guardTwo += guardTwo
            if([guardOne, guardTwo] == banana_list):
                break

        if(guardOne == guardTwo):
            return 2
    else:
        for itemOne in banana_list:
            watchingGuardsNum = 0
            for itemTwo in banana_list:
                itemOneRep = itemOne
                itemTwoRep = itemTwo
                if(itemOneRep == itemTwoRep):
                    watchingGuardsNum += 2
                else:
                    repititions = []
                    repititions.append([itemOneRep, itemTwoRep])
                    while itemOneRep != itemTwoRep:
                        if([itemOneRep, itemTwoRep] == repititions[0]):
                            distractedGuardsNum += 2
                            break
                        if(itemOneRep < itemTwoRep):
                            itemTwoRep -= itemOneRep
                            itemOneRep += itemOneRep
                        elif(itemOneRep > itemTwoRep):
                            itemOneRep -= itemTwoRep
                            itemTwoRep += itemTwoRep
            print(distractedGuardsNum)

def inLoop(a, b):
    aCopy, bCopy = a, b

    if(a == b):
        return False

    while a != b:
        print(a,b)
        if(a < b):
            b -= a
            a += a
        elif(a > b):
            a -= b
            b += b
        print(a,b)
        break
        if((a, b) == (aCopy, bCopy)):
            return True
            break

    return False