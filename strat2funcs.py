import random

def _rowCheck(tt, r, sym, num):
    #check how many sym are found in the row.  Match count against num that was input
    count = 0
    emptyCells = []
    
    for c in range(0, 3):
        if tt[r][c] == sym:
            count = count + 1
        elif isFree(tt, r, c):
            emptyCells.append([r, c])

    if count == num:   
        return [True, emptyCells]
    else:
        return [False, emptyCells]
    
def _colCheck(tt, c, sym, num):
    #check how many sym are found in the column.  Match count against num that was input
    count = 0
    emptyCells = []
    
    for r in range(0, 3):
        if tt[r][c] == sym:
            count = count + 1
        elif isFree(tt, r, c):
            emptyCells.append([r, c])

    if count == num:   
        return [True, emptyCells]
    else:
        return [False, emptyCells]

def _diagCheckBackward(tt, sym, num):
    #check how many sym are found in the backward diag.  Match count against num that was input
    count = 0
    emptyCells = []
    
    for d in range(0,3):
        if tt[d][d] == sym:
            count = count + 1
        elif isFree(tt, d, d):
            emptyCells.append([d, d])

    if count == num:   
        return [True, emptyCells]
    else:
        return [False, emptyCells]

def _diagCheckForward(tt, sym, num):
    #check how many sym are found in the forward diag.  Match count against num that was input
    count = 0
    emptyCells = []
    
    for t in [[0,2], [1,1], [2,0]]:
        x=t[0]
        y=t[1]
        if tt[x][y] == sym:
            count = count + 1
        elif isFree(tt, x, y):
            emptyCells.append([x, y])

    if count == num:   
        return [True, emptyCells]
    else:
        return [False, emptyCells]
            
    
def rowCheck(tt, r, sym):
    return _rowCheck(tt, r, sym, 3)[0]

def colCheck(tt, c, sym):
    return _colCheck(tt, c, sym, 3)[0]

def diagCheckBackward(tt, sym):
    return _diagCheckBackward(tt, sym, 3)[0]

def diagCheckForward(tt, sym):
    return _diagCheckForward(tt, sym, 3)[0]
    
def printTTM(tt):
    for r in range(0,3):
        print "%s %s %s" % (tt[r][0], tt[r][1], tt[r][2])

def outOfRange(x, y):
    return x > 2 or y > 2


def setTTM(tt, x, y, sym):
    tt[x][y] = sym

def hasPlayerWon(tt, sym):
    #check all rows
    for r in range(0, 3):
        if rowCheck(tt, r, sym):
            return True
    #check all columns
    for c in range(0, 3):
        if colCheck(tt, c, sym):
            return True
    #check diagonals
    if diagCheckBackward(tt, sym):
        return True
    
    if diagCheckForward(tt, sym):
        return True
    
    return False

def hasWonAnyPlayer(tt, sym1, sym2):
    if hasPlayerWon(tt, sym1) or hasPlayerWon(tt, sym2):
        return True
    else:
        return False
    
def setRandomTTM(tt, sym):
    found = allCellsFilled(tt)
    while not found:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if isFree(tt, x, y):
            tt[x][y] = sym
            found = True
            
def _findImminentWin(tt, symToTest, symToSet):
    #check all rows
    for r in range(0, 3):
        result = _rowCheck(tt, r, symToTest, 2)
#        print result
        if result[0] and len(result[1]) > 0:
            freex = result[1][0][0]
            freey = result[1][0][1]
            setTTM(tt, freex, freey, symToSet)
            return True

    #check all columns
    for c in range(0, 3):
        result = _colCheck(tt, c, symToTest, 2)
#        print result
        if result[0] and len(result[1]) > 0:
            freex = result[1][0][0]
            freey = result[1][0][1]
            setTTM(tt, freex, freey, symToSet)
            return True

    #check backward diagonal
    result = _diagCheckBackward(tt, symToTest, 2)
#    print result
    if result[0] and len(result[1]) > 0:
        freex = result[1][0][0]
        freey = result[1][0][1]
        setTTM(tt, freex, freey, symToSet)
        return True
    
    #check forward diagonal
    result = _diagCheckForward(tt, symToTest, 2)
#    print result
    if result[0] and len(result[1]) > 0:
        freex = result[1][0][0]
        freey = result[1][0][1]
        setTTM(tt, freex, freey, symToSet)
        return True
    
    ##if you got here, there is no imminent danger
    #if symToTest == "X":
    #    print "No danger"
    #else:
    #    print "No win yet"
    
    return False
    

def isFree(tt, x, y):
    return tt[x][y] == '.'

def isOccupied(tt, x, y, sym):
    return tt[x][y] == sym

def blockOpponent(tt, ySym, mSym):
    return _findImminentWin(tt, ySym, mSym)

def setWinningPick(tt, mSym):
    return _findImminentWin(tt, mSym, mSym)

def allCellsFilled(tt):
    for r in range(0,3):
        for c in range(0,3):
            if isFree(tt, r, c):
                return False
    return True

def allButOneCellFilled(tt):
    count = 0
    for r in range(0,3):
        for c in range(0,3):
            if not isFree(tt, r, c):
                count = count + 1
    if count == 8:
        return True
    else:
        return False
    
def isCornerCell(r, c):
    return ([r, c] == [0, 0]) or ([r, c] == [0, 2]) or ([r, c] == [2, 0]) or ([r, c] == [2, 2])

def getOppositeCorner(r, c):
    if [r, c] == [0, 0]:
        return [True, [2, 2]]
    elif [r, c] == [0, 2]:
        return [True, [2, 0]]
    elif [r, c] == [2, 0]:
        return [True, [0, 2]]
    elif [r, c] == [2, 2]:
        return [True, [0, 0]]
    else:
        return [False, False]
    
def blockDiagonal(tt, r, c, sym):
    result = getOppositeCorner(r, c)
    if result[0] == True:
        diagX = result[1][0]
        diagY = result[1][1]
        if isFree(tt, diagX, diagY):
            setTTM(tt, diagX, diagY, sym)
            return True
    
    #if you got here, either it is not a diagonal cell or the corresponding diagonal cell is not free
    return False