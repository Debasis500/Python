#fibonacci sequence up to nth term

a=int(input("How many terms:"))
    
n1,n2 = 0,1
count = 0

if a <= 0:
    print("Enter positive number")
elif a == 1:
    print("Fibonacci sequence")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < a:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    
        
    
