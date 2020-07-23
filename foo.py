class knight:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

def onBoard(x, y, board):
    if(x >= 0 and x < board and y >= 0 and y < board):
        return True
    else:
        return False

def solution(src, dest):
    startx = 0
    starty = 0
    destx = 0
    desty = 0
    boardSize = 8

    # Convert start position to coordinate
    if src < 8:
        startx = src
        starty = 0
    elif 7 < src < 16:
        startx = src - 8
        starty = 1
    elif 15 < src < 24:
        startx = src - 16
        starty = 2
    elif 23 < src < 32:
        startx = src - 24
        starty = 3
    elif 31 < src < 40:
        startx = src - 32
        starty = 4
    elif 39 < src < 48:
        startx = src - 40
        starty = 5
    elif 47 < src < 56:
        startx = src - 48
        starty = 6
    elif 55 < src < 64:
        startx = src - 54
        starty = 7
    else:
        print("Start not in range")

    # Convert end position into coordinate
    if dest < 8:
        destx = dest
        desty = 0
    elif 7 < dest < 16:
        destx = dest - 8
        desty = 1
    elif 15 < dest < 24:
        destx = dest - 16
        desty = 2
    elif 23 < dest < 32:
        destx = dest - 24
        desty = 3
    elif 31 < dest < 40:
        destx = dest - 32
        desty = 4
    elif 39 < dest < 48:
        destx = dest - 40
        desty = 5
    elif 47 < dest < 56:
        destx = dest - 48
        desty = 6
    elif 55 < dest < 64:
        destx = dest - 56
        desty = 7
    else:
        print("Destination not in range")

    rowDir = [2, 2, -2, -2, 1, 1, -1, -1]
    colDir = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []
    queue.append(knight(startx, starty, 0))

    visited = [[False for i in range(boardSize + 1)] for j in range(boardSize + 1)]
    visited[startx][starty] = True

    #print(destx, desty)

    while(len(queue) > 0): 

        piece = queue[0] 
        queue.pop(0)

        if(piece.x == destx and piece.y == desty):
            if piece.dist > 0:
                print(piece.dist)
                return piece.dist
            else:
                return 0
                
        for i in range(8): 
            x = piece.x + rowDir[i]
            y = piece.y + colDir[i] 

            if(onBoard(x, y, boardSize) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(knight(x, y, piece.dist + 1)) 
                #print(x,y)
            else:
                pass

    if(piece.x is not destx or piece.y is not desty):
        #print(piece.x, piece.y)
        return piece.dist

solution(0, 62)