#TOWER OF HANOI RECURSIVE

def hanoi(n):
    if n == 1:
        print "Turns required: 1"
    else:
       recursive = 2*(n+1)+1
       
       return recursive
       
    
print hanoi(4) 
