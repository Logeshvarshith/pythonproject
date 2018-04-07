k=input("Enter the strig:")
a=len(k)
n=0
for i in k:
  if(i=='a' or i=='b'): 
    n=n+1
if(n==a):
  print("yes")
else:
  print("no")
