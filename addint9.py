N,K=input("Enter n and k:").split(' ')
N,k=int(N),int(K)
a=list(map(int,input("Enter values:").split(' ')))
print(sum(a[:K]))
