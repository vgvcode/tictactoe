def func():
    emptyCells = []
    emptyCells.append([1,1])
    return [True, emptyCells]
    
    
v = func()
if v[0]:
    lst = list(v[1])
    
    if len(v[1]) > 0:
        print lst[0][0], lst[0][1]
    else:
        print "Empty"