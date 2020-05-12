# pattern formation

def pattern(number):
    for i in range(0,number+1):
        for j in range(0,i):
            print("*",end="")

        print("")
num=int(input())
pattern(num)
        
