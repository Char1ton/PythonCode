
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

mew,a,gam= 0.1,0.1,0.1
beta=0.39
beta2=0.41
P0=[5,5,5,0] #arbitrary numbers array set up as [S,E,I,R]
N=sum(P0)
R0=(a*beta)/((mew+a)*(mew+gam))
R02=(a*beta2)/((mew+a)*(mew+gam))
def derives(P,t): #solving the ODE for beta
    S,E,I,R=P
    dS=(mew*N)-(mew*S)-(beta*((I*S)/N))
    dE=(beta*(I*S)/N)-((mew+a)*E)
    dI=(a*E)-((gam+mew)*I)
    dR=(gam*I)-(mew*R)
    return dS,dE,dI,dR
def derives2(P,t): #solving ODE for beta2
    S,E,I,R=P
    dS=(mew*N)-(mew*S)-(beta2*((I*S)/N))
    dE=(beta2*(I*S)/N)-((mew+a)*E)
    dI=(a*E)-((gam+mew)*I)
    dR=(gam*I)-(mew*R)
    return dS,dE,dI,dR
t=np.linspace(0,100,1000)
Pt=odeint(derives,P0,t)
Pt2=odeint(derives2,P0,t)
S2=Pt2[:,0]
E2=Pt2[:,1]
I2=Pt2[:,2]
R2=Pt2[:,3]
S=Pt[:,0]
E=Pt[:,1]
I=Pt[:,2]
R=Pt[:,3]

plt.figure()

plt.plot(t, S, label="S")
plt.plot(t, E, label="E")
plt.plot(t, I, label="I")
plt.plot(t, R, label="R")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("R0<1")
plt.legend()
plt.show()

plt.figure()

plt.plot(t, S2, label="S")
plt.plot(t, E2, label="E")
plt.plot(t, I2, label="I")
plt.plot(t, R2, label="R")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("R0>1")
plt.legend()
plt.show()


#as you can see with the differences between when R0>1 and R0<1, when R0>1 the exposed and infected will stay at constant>0, while R0<1 will converge to 0
