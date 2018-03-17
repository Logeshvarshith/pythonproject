import math
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
p=m*n
print(p)
p_sqrt=p**0.5
if(p_sqrt==int(math.sqrt(p))):
  print("Yes")
else:
  print("No")
