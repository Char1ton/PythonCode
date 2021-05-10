import numpy as np
import matplotlib.pyplot as plt

#Traitor Ants

T=100
N=30
TT=np.linspace(0,T,T)
NT=int(N/3)

def main():
    pos,col,datR,datB,datG=initial()
    
    for t in range(T):
        unique,counts=np.unique(col,return_counts=True)
        datR[t]=counts[0]
        datB[t]=counts[1]
        datG[t]=counts[2]
        
        pos,col=walk(pos,col)
    
    print(counts)
    plt.plot(TT,datR,'r')
    plt.plot(TT,datB,'b')
    plt.plot(TT,datG,'g')
    
def walk(pos,col):
    
    for n in range(N):
        Dire=np.random.randint(0,4)
        if Dire==0:
            pos[n][0]=pos[n][0]-1
        elif Dire==1:
            pos[n][0]=pos[n][0]+1
        elif Dire==2:
            pos[n][1]=pos[n][1]-1
        elif Dire==3:
            pos[n][1]=pos[n][1]+1
            
        for nn in range(N):
            if pos[n][0]==pos[nn][0] and pos[n][1]==pos[nn][1]:
                col[nn]=col[n]
    return pos,col



def initial():
    pos=np.zeros((N,2))
    col=np.zeros(N)
    datR=np.zeros(T)
    datB=np.zeros(T)
    datG=np.zeros(T)
    
    for n in range(N):
        pos[n][0]=np.random.randint(-N,N)
        pos[n][1]=np.random.randint(-N,N)
        #col[n]=np.random.randint(0,2) 
    col[0:NT]=1
    col[NT:2*NT]=2
    
    return pos, col, datR, datB, datG


main()