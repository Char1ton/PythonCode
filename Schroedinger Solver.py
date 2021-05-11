#m=hbar=1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
global gam
E=17  #I found a solution at E=16 so i just started the Energy here

gam=0.0483
V0=83

xL=np.linspace(-4,-2,200)
xW=np.linspace(-2,2.001,200)
xR=np.linspace(2.001,4,200)    #setting up each region of distance for the wave functions

def Schro(psi,xW,k):   #solves the wave equation in the potential well
    S0=psi[1]
    S1=-((gam*(83))-k**2)*psi[0]
    return [S0,S1]

while E>0:    #finds all wavefunctions that satisfy the problem
    k=np.sqrt(gam*E)  
    psiL=np.exp(k*xL)
    psiR=np.exp(-k*xR)
    psiW0=[np.exp(k*-2),(k**2)*np.exp(k*-2)]
    psi=odeint(Schro,psiW0,xW,args=(k,))
    Y=psi[:,0]
    
    dpsiW=[0]*len(xW)   #deriving the wave in the well
    dpsiW[0] = (Y[0] - Y[1])/(xW[0] - xW[1])
    for i in range(1,len(Y)):
      dpsiW[i] = (Y[i] - Y[i-1])/(xW[i]-xW[i-1])
      
    
    PLxm=dpsiW[-1]
    Lxm=Y[-1]
    PRxm=(-k*np.exp(-k*2.001))
    Rxm=psiR[0]
    ep=((PLxm/Lxm)-(PRxm/Rxm))/((PLxm/Lxm)+(PRxm/Rxm))
    
    
    if abs(ep)<.00001:  #if the error is smaller than this it is close enough to zero
        print("error>>",ep,"Energy>>",E)
        plt.plot(xL,psiL, label="PsiLeft")
        plt.plot(xW,Y, label="PsiWell")
        plt.plot(xR,psiR, label="PsiRight")
        plt.xlabel("Distance 'fm'")
        plt.ylabel("Magnitude 'Mev'")
        plt.legend()
        plt.title("Full Wavefunction")
        plt.show()
    E=E-0.001  #completing the loop
