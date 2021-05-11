import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.fft import fft, ifft
from numpy import linalg as la



N=50

L=1
kmax=400

alph=1

def matrix():
    brill=np.linspace(0,L,N)
    return brill
    
def short(brill):
    PotS=np.zeros((N,N))
    for i in range(N):
        ri=brill[i]
        for j in range(N):
            rj=brill[j]
            if i==j:
                PotS[i][j]=np.inf
            else:
                rij=dist(ri,rj)
                Uij=(1/2)*((1)/(rij))*np.exp(rij*np.sqrt(alph))
                PotS[i][j]=Uij
    
    return PotS

def fourier(matrix):
    result=np.zeros(N)
    pre=1/np.pi
    
    for i in range(N):
        ri=matrix[i]
        Pk=0
        for j in range(N):
            rj=matrix[j]
            rij=dist(ri,rj)
            for ki in range(0,kmax+1):
                if ki==0:
                    continue
                
                k=ki*2*np.pi
                Pk+=np.exp(1j*k*ri)
                ksq=(k*k)
                result[i]+=(2*np.pi/ksq)*np.exp(-ksq/(4*alph))*abs(Pk)**2
    
    result[0]=result[1]
    result[N-1]=result[N-2]
    return (result)

def dist(coords1, coords2):
    return ((coords1 - coords2) ** 2) ** 0.5

def Uself(Num):
    Uself=Num
    
    return Uself

def graphical(T,Tot,ShortPot,Fourier):
    
    Num=1
    H=int(N/Num)
    TT=np.zeros(N)
    ShT=np.zeros(N)
    Real=1/T
    for i in range(Num):
        TT+=Tot[i*H]-Uself(Num)
        ShT+=ShortPot[i*H]-Uself(Num)
        
    ET=Errors(TT,Real,ShT,Fourier)
    
    plt.figure(1)
    plt.plot(T,TT,label='Total Potential')
    #plt.plot(T,ShT,label='Short Range Potential')
    #plt.plot(T,Fourier,label='Long Range Potential')
    plt.plot(T,Real,label='1/r')
    plt.axis([0,L,0,50])
    plt.legend()
    plt.title('Potential vs Length \nFor Particles Uniformly Distributed \n Alpha=1\nError~%i percent'%ET )
    plt.xlabel('Radial Plane (r)')
    plt.ylabel('Arbitrary Potential (psi)')
    plt.show()
    
    

def Errors(TT,Real,ShT,Fourier):
    TotalError=sum(abs(Real[1:]-TT[1:])/Real[1:])/N
    
    return TotalError
    
    

def main():
    T=np.linspace(0,L,N)
    Tot=[]
    
    lattice=matrix()
    
    ShortPot=short(lattice)
    
    EFour=fourier(lattice)

    
    
    for i in range(N):
        Tot.append((ShortPot[i])+EFour)
            
    graphical(T,Tot,ShortPot,EFour)      
            
main()



#testing, be sure to mute main() first