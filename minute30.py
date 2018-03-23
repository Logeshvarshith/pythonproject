a,b=map(int,input("Enter the number:").split(':'))
c,d=map(int,input("Enter the number:").split(':'))
v=a*60+b
p=c*60+d
sub=p-v
print(sub//60,":",sub%60)
