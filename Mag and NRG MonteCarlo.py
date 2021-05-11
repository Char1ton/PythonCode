import numpy as np
import matplotlib.pyplot as plt

N=10


def initial(): #Initial state
    i_state=2*np.random.randint(2,size=(N,N))-1
    return i_state

def Adja(state,x,y): #Adjacent states calculations
    west=state[x,(y-1)%N]
    east=state[x,(y+1)%N]
    north=state[(x+1)%N,y]
    south=state[(x-1)%N,y]
    tot=west+east+north+south
    
    return tot

def Calc(state): #energy calculation
    energy=0
    for i in range(len(state)):
        for j in range(len(state)):
            
            Init=state[i,j]
            
            Neigh=Adja(state,i,j)
            energy+= -Neigh*Init
    return energy/4
    

def Monte(state,J): #Monte Carlo, Metropolis Algorithm 
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  state[a, b]
                nb = Adja(state,a,b)
                flipE = 2*s*nb
                if flipE < 0:
                    s *= -1
                elif np.random.random() < np.exp(-flipE*J):
                    s *= -1
                state[a, b] = s
    return state

def Main(Jp): #Main code with plots
    h=10
    hs=100
    T=np.linspace(0.1,2,h)
    MAG,ENG=np.zeros(h),np.zeros(h)
    for t in range(h):
        E0=M0=0
        state=initial()
        J=Jp/T[t]
        for i in range(hs):
            Monte(state,J)
        
        for i in range(hs):
            Monte(state,J)
            M=np.sum(state)
            M0+=M
            E=Calc(state)
            E0+=E
        ENG[t]=(E0)/(hs*N**2)
        MAG[t]=abs(M0)/(hs*N**2)
    plt.figure()
    plt.plot(T[1:],MAG[1:])
    plt.xlabel('Temperatur (T)')
    plt.ylabel('Magnetization per spin (arbitrary units)')
    if Jp==0.4:
        plt.title("Magnetization per spin when J'=0.4")
    else:
        plt.title("Magnetization per spin when J'=0.5")
    plt.show()
    
    
    plt.figure()
    plt.plot(T[1:],ENG[1:])
    plt.xlabel('Temperatur (T)')
    plt.ylabel('Energy per spin (arbitrary units)')
    if Jp==0.4:
        plt.title("Energy per spin when J'=0.4")
    else:
        plt.title("Energy per spin when J'=0.5")
    plt.show()
            

Main(0.5)
#Main(0.5)
        
        