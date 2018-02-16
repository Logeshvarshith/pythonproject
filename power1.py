def power(base,a):
     if(a==1):
         return(base)
     if(a!=1):
         return(base*power(base,a-1))
base=int(input("Enter base: "))
a=int(input("Enter exponential value: "))
print("Result:",power(base,a))
