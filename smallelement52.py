n=int(input("Enter n:"))
k=int(input("enter k:"))
a=[]
for i in range(0,n):
  b=int(input("enter the number:"))
  a.append(b)
a.sort()
print(a[k-1])
