n=int(input("Enter the number:"))
a=[]
for i in range(0,n):
  b=int(input("enter the array:"))
  a.append(b)
for x in a:
  print(x,a.index(x))
