import numpy as np
import matplotlib.pyplot as plt
def func(N,M):
    I=0
    ER=0
    R=155/6
    for i in range(M):
       Y=np.random.uniform(0,1,size=(N,10))
       ER+=abs(I-R)/R
       I=0
       for j in range(N):
            I+=((sum(Y[j]))**2)/N
            
    ER=ER/M   
    E=1/(np.sqrt(N))
    return I,E,ER

def Main():
    M=200
    N=1000
    EInt=[]
    ERInt=[]
    
    while N>0:
        IA,EA,ERA=func(N,M)
        EInt.append(EA)
        ERInt.append(ERA)
        N-=20
    plt.scatter(EInt,ERInt)
    plt.xlabel("1/sqrt(N)")
    plt.ylabel("Deviation from actual")
    plt.title("Deviation as a function of 1/sqrt(N)")
    plt.show()
    print("As you can see it has a linear reperesentation")
Main()
    