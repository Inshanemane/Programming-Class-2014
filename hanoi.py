#TOWER OF HANOI RECURSIVE

def hanoi(n):
    if n == 1:
        print "Turns required:"
        return 1
    else:
       recurse= 2*hanoi(n-1)+1
       return recurse
       
       
       
       
    
print hanoi(7) 
