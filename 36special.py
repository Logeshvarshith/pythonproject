s="~`!@#$%^&*()_-+={}[]:>;',</?*-+"
n=input("Enter the symbol:")
c=0
for i in n:
  if i in s:
    c=c+1
print(c)
