#Fibonnaci sequence: 1,1,2,3,5,8,13...

#t[n] = t[n-2] + t[n-1]
num_run2 = 0
def fibo(n):
    global num_run2
    if n == 1 or n == 2:
        return 1
    
    else:
        num2 = fibo(n-2)+fibo(n-1)
        print 'return',num2
        num_run2+=1
        return num2

print fibo(7)
print 'Numberof times for fib:',num_run2
print



#MODIFIED FUNCTION

fibo_dic = {}

num_run = 0

def new_fibo(n):    
    global fibo_dic, num_run
    
    if n == 1 or n == 2:
        return 1
    
    elif fibo_dic.has_key(n):
        ans = fibo_dic.get(n)
        return ans
       
    else:
        num = new_fibo(n-2) + new_fibo(n-1)
        fibo_dic[n] = num
        print 'return',num
        num_run+=1
        return num
               
print new_fibo(7)
print 'Number of times for new fibo', num_run
