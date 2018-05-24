n=input("enter the number:")
a=[]
for i in n:
  if(int(i)%2==0):
    continue
  else:
    a.append(i)
print(" ".join(str(x) for x in a))
