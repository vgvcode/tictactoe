import random
from strat2funcs import *

yourSym = 'X'
mySym = '*'
yourScore = 0
myScore = 0
    
matchOver = False

while not matchOver:
    ttm = [['.','.','.'], ['.','.','.'], ['.','.','.']]    
    printTTM(ttm)
    print "Your symbol: %s.  My symbol: %s" % (yourSym, mySym)
    gameOver = False

    toss = random.randint(0,1)
    if toss > 0.5:
        #computer picks first
        print "I get to go first"
        setRandomTTM(ttm, mySym)
        printTTM(ttm)
    
    #go through the loop until all cells are filled, alternating between player (first) and computer(next)
    while not gameOver:
        if allCellsFilled(ttm) or allButOneCellFilled(ttm):
            print "It's a draw.  Your score: %s, My score: %s" % (yourScore, myScore)
            gameOver = True
        else:
            xy = raw_input("Your pick (q to quit):")
            if xy[0].isalpha():
                if xy[0] == 'q':
                    gameOver = True
                    matchOver = True
                else:
                    print "Invalid input. Try again"
            else:    
                x = int(xy[0])
                y = int(xy[1])
                
                if outOfRange(x, y):
                    print "Out of range. Pick again"
                elif isFree(ttm, x, y):
                    setTTM(ttm, x, y, yourSym)
        
                    # first see if you can win in this round
                    # if not, see if you can block the opponent from an imminent win
                    # if not, apply the block diagonal strategy
                    # if not, pick a random cell
                    if not setWinningPick(ttm, mySym):
                        if not blockOpponent(ttm, yourSym, mySym):
                            if not blockDiagonal(ttm, x, y, mySym):
                                setRandomTTM(ttm, mySym)
                    
                    printTTM(ttm)
                    if hasPlayerWon(ttm, yourSym):
                        yourScore = yourScore + 1
                        print "Congratulations. You win. Your score: %s, My score: %s" % (yourScore, myScore) 
                        gameOver = True
                    elif hasPlayerWon(ttm, mySym):
                        myScore = myScore + 1
                        print "Hey, I won. Your score: %s, My score: %s" % (yourScore, myScore)
                        gameOver = True
                else:
                    print "That cell is taken. Pick again"
    

