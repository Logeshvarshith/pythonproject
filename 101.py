n=int(input("Enter the number:"))
b=[]
c=0
for i in range(0,n):
  a=int(input())
  b.append(a)
for i in range(1,n):
  if(b[i]<b[i-1]):
    c=c+b[i-1]
  else:
    c=c+b[i]
print(c)
