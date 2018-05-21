def power(k):
   k=k/n
   if k==n:
     print("yes")
   elif k>n:
     return power(k)
   else:
     print("no")
s=int(input("Enter the number:"))
n=int(input("Entet n:"))
power(s)
