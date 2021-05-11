import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
global q,a0,b1

q=1
a0=(-1/2)+(7/128)-(29/2304) #setting up the constants
b1=(-1/8)+(1/64)-(1/1536)
tb1=np.linspace(0,50,84)
ta0=np.linspace(0,50,85)
def funca0(t,X):   #solving for a0
   S0=X[1]
   S1=-(a0-(2*(np.cos(2*t))))*X[0]
   return [S0,S1]
def funcb1(t,X):  #solving for b1
   S0=X[1]
   S1=-(b1-(2*(np.cos(2*t))))*X[0]
   return [S0,S1]
sola0=solve_ivp(funca0,[0,50],(1,0))  #solve_ivp uses Runge-Kutta45 so I figured this was allowed
solb1=solve_ivp(funcb1,[0,50],(0,1))
za0=sola0.y[0]  #the solutions of x 
zb1=solb1.y[0]  
plt.figure()
plt.plot(tb1,zb1,label="p=b1(q),x(0)=0,x'(0)=1")
plt.plot(ta0,za0,label="p=a0(q),x(0)=1,x'(0)=0")
plt.xlabel('Time "t"')
plt.ylabel('Magnitude "x"')
plt.title('Solutions to Mathieu equation')
plt.legend()
plt.show()
