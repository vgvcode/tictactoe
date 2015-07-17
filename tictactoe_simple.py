import random

def rowCheck(tt, r, sym):
    if tt[r][0] == sym and tt[r][1] == sym and tt[r][2] == sym:
        return True
    else:
        return False
    
def colCheck(tt, c, sym):
    if tt[0][c] == sym and tt[1][c] == sym and tt[2][c] == sym:
        return True
    else:
        return False

def diagCheckBackward(tt, sym):
    #backward slash
    if tt[0][0] == sym and tt[1][1] == sym and tt[2][2] == sym:
        return True
    else:
        return False

def diagCheckForward(tt, sym):
    #forward slash
    if tt[0][2] == sym and tt[1][1] == sym and tt[2][0] == sym:
        return True
    else:
        return False

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
    found = False
    while not found:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if isFree(tt, x, y):
            tt[x][y] = sym
            found = True

def isFree(tt, x, y):
    return tt[x][y] == '.'

def isOccupied(tt, x, y, sym):
    return tt[x][y] == sym

ttm = [['.','.','.'], ['.','.','.'], ['.','.','.']]
yourSym = 'X'
mySym = '*'

#if rowCheck(ttm, 0, 'X') == True:
#    print ('Row set:', 0)
#else:
#    print ('Row unset:', 0)
#        
#if rowCheck(ttm, 1, 'X') == True:
#    print ('Row set:', 1)
#else:
#   print ('Row unset:', 1)
    
gameOver = False

printTTM(ttm)

while not gameOver:
    xy = raw_input("Your pick (q to quit):")
    if xy[0] == 'q':
        gameOver = True
    else:    
        x = int(xy[0])
        y = int(xy[1])
        
    if outOfRange(x, y):
        print "Out of range. Pick again"
    elif isFree(ttm, x, y):
        setTTM(ttm, x, y, yourSym)
        setRandomTTM(ttm, mySym)
        
        printTTM(ttm)
        if hasPlayerWon(ttm, yourSym):
            print "Congratulations. You win"
            gameOver = True
        elif hasPlayerWon(ttm, mySym):
            print "Hey, I won"
            gameOver = True
    else:
        print "That cell is taken. Pick again"
    

