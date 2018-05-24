n=int(input("Enter the number:"))
l=list(map(int,input("Enter:").split(" ")))
for i in range(0,n):
  if(l[i]>l[i+1]):
    print(i+1)
    break
