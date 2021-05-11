import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#c0+c2*P**2+c3*P**3+c6*P**6, fit the curve and c0 will be when p=0
XX=np.linspace(0,1,10)
p=[0.8,0.4,0.2,0.1,0.05]
x=[740,487,475,485,489]
P=[]

def func(p,a,b,c,d):
    return a+(b*p**2)+(c*p**3)+(d*p**3) #extrapolating the curve
def func2(p,a,b,c,d):
    for i in range(0,len(XX)):
        P.append(a+(b*p[i]**2)+(c*p[i]**3)+(d*p[i]**3))
popt,pcov=curve_fit(func,p,x)
func2(XX, *popt)
print(popt[0], "This is the value of x when p=0" )

plt.figure() 
plt.plot(p,x, label="data")
plt.plot(XX, P, label="Fitted data")
plt.xlabel("p")
plt.ylabel("x(p)")
plt.legend()
plt.show()