def power(n):
  n=n/2
  if n==2:
    print("yes")
  elif n>2:
    return power(n)
  else:
    print("no")
s=int(input("Enter the number:"))
power(s)
