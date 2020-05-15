# pattern formation

def pattern():
    num=int(input("Enter no. of rows:"))
    for i in range(0,num+1):
        for j in range(0,i+1):
            print("*",end="")

        print("")
    option= input(print("Do you want to continue:"))
    if(option == 'y'):
        pattern("")
    else:
        print("Thank You")
pattern()
        
