import numpy as np
N=50
L=2000
def func(m):
    States=np.zeros((L,N))
    Omega=np.math.factorial(N)/(np.math.factorial(m)*np.math.factorial(N-m))
    pairs=0
    coin=0
    for i in range(0,L):
        pairs+=i
        for k in range(0,m):
            States[i,k]=1
            np.random.shuffle(States[i])
        for j in range(0,L):
            if i==j:
                coin+=0
            elif np.array_equal(States[i],States[j])==True:
                coin+=1
            else:
                coin+=0
    
    return Omega, pairs, coin

def Main():
    m=1
    while m<=7:
        Omega,pairs,coin=func(m)
        if coin==0:
            OmegaApprox=float('inf')
            OmegaError=float('inf')
        else:
            OmegaApprox=pairs/coin
            OmegaError=abs((Omega-OmegaApprox)/Omega)*100
        print("m:",m,"Calculated Omega:",Omega,"Approximate Omega:",OmegaApprox,"Omega Error Percentage:",OmegaError)
        m+=1

Main()
print("As you can see after m is greater than 3 the approximation of Omega quickly gets out of hand and even starts having error that approaches or exceeds 100% and at some points the error is infinite because our approximated Omega is infinite. For this algorithm, N=50 and the number of states(L)=1500. L is at 2000 because otherwise this algorithm took forever to process.")