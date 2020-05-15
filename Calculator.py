print('1.ADD')
print('2.SUB')
print('3.MUL')
print('4.DIV')
a= input('Enter choice(1/2/3/4):')
b=int(input('Enter 1st no:'))
c=int(input('Enter 2nd no:'))

if a=='1':
      print('Sum=',b+c)

elif a=='2':
    print('Sub=',b-c)

elif a=='3':
    print('Mul=',b*c)

elif a=='4':
    print('Div=',b/c)
else:
    print("Invalid Choice")
    
      
         
