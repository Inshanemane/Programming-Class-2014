#Recursive factorial function
#n!

def factorial(n):
    if n  == 1:
        print "returning 1"
        return 1
    else:
        result = n*factorial(n-1)
        print "returning", result
        return result
    
print factorial(5)    

#Fibonnaci sequence: 1,1,2,3,5,8,13...

#t[n] = t[n-2] + t[n-1]

def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fibo(n-2)+fibo(n-1)
    
print fibo(5)    
