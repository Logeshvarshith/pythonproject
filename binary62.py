n=input("Enter the number:")
a=n.count('1')
b=n.count('0')
c=len(n)
if(c==a+b):
  print("yes")
else:
  print("no")
