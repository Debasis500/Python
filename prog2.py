l=["Pen","Pencil","Eraser","Sharpner","Book","Notebook"]
print(l)
print('select an option:')
print('1.Purchase')
print('2.Sell')
a=int(input('Enter your option'))
if(a==1):
     b=str(input('Enter name:'))
     l.append(b)
     print("Customer Purchased")
     print(b)
elif(a==2):
      c=str(input('Enter name:'))
      l.remove(c)
      print("Item Sold")
      print(l)
      print("Order")
else:
     print('Enter a valid choice')

