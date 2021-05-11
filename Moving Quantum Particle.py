import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.sparse import diags
from numpy.linalg import inv
import scipy.linalg as la

delx=0.02
delt=delx**2/2
lam=1j*delt/(4*delx**2)
sig=0.5
k0=17*np.pi
N=int(11/delx)
t=np.linspace(0,N*delt,N)
x=np.linspace(5,15,N)
phi0=np.exp(1j*k0*x)*np.exp((-1/2)*(x-5/sig)**2)
phit=[] #initialize phi
phit.append(phi0)



def CrankMatrix(lam,phit): #Using the Crank Nicolson method have a matrix that moves our psi through time
    a=1+2*lam
    b=1-2*lam
    ka=np.array([-lam*np.ones(N-1),a*np.ones(N),-lam*np.ones(N-1)])
    kb=np.array([lam*np.ones(N-1),b*np.ones(N),lam*np.ones(N-1)])
    offset=[-1,0,1]
    A=diags(ka,offset).toarray()
    B=diags(kb,offset).toarray()
    Ainv=inv(A)
    for i in range(0,N): #the system is in a Ax=B state where the next phi is x, the previous phi is B and Ainv is our operator 
        Mat=np.matmul(Ainv,B)
        phitt=np.matmul(Mat,phit[i])
        phit.append(phitt)
    Probs(phit) #probabilty function
def Probs(Phi):
    probab=np.zeros(N)
    for i in range(0,N):
         probab[i]=abs(np.matmul(phit[i],phit[i]))
    P=integrate.cumtrapz(probab,t,initial=probab[0])
    plt.figure()
    plt.plot(t,P)
    plt.xlabel("Time t")
    plt.ylabel("Probability")
    plt.title("Probability as a function of time")
    plt.show()
     
        

        
    

CrankMatrix(lam,phit)         

plt.figure()
plt.plot(x,phit[0], label="Psi 0")  
plt.plot(x,phit[N], label="Psi N")
plt.ylabel("Arbitrary Amplitude")
plt.xlabel("Distance x")
plt.title("Starting Psi vs Ending Psi")
plt.legend()
plt.show()



 
    