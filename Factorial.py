def Fact(n):
    if n == 0:
     return 1
    
    smallprob=Fact(n-1)
    bigprob=n * smallprob
    return bigprob
print(Fact(6))


'''n=5
n= n*(n-1)*(n-2)*(n-3)
print(n)'''