n=int(input("Enter the number:"))
a=0
for i in range(2,n):
    n%i==0
    a=i
if n>1:
  print ('Yes')
elif n==1:
  print ('neither prime nor composite')
else:
  print("n0")
