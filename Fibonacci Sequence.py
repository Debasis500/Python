#fibonacci sequence up to nth term

def fibonacci(val):
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(2,val):
        c=a+b
        if c < val:
            print(c, end=' ')
        else:
                break
        a=b
        b=c
val=int(input('Enter the number:'))
fibonacci(val)

    
        
    
