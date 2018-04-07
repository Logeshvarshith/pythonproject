def power(k):
  k=k/2
  if k==2:
    print("yes")
  elif k>2:
    return power(k)
  else:
    print("no")
s=int(input("Enter the number:"))
power(s)
