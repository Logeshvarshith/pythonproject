n=int(input("enter the number:"))
a=[]
for i in range(0,n):
  b=int(input("Enter number:"))
  a.append(b)
a.sort()
print(min(a),max(a))
