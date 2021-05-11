from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

ep,gam= 1,1

def derives(P, t):
    return [P[0]*(ep - gam*P[1]), -P[1]*(ep - gam*P[0])]

t=np.linspace(0, 10, 1000)
P0=[0.1, 0.1]
Ps=odeint(derives, P0, t)
lit=Ps[:,0]
big=Ps[:,1]

plt.figure()

plt.plot(t, lit, label="Little Fish")
plt.plot(t, big, label="Big Fish")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()

plt.figure()
plt.plot(lit, big, "-")
plt.xlabel("Little Fish")
plt.ylabel("Big Fish")
plt.title("Big v. Little")
plt.show()

#With the Big v. Little graph you can see that it should move in a counterclockwise motion
#where a lot of little fish begin and slowly decline as the big fish numbers increase
#and then go down because of lack of little fish and then the cycle repeats itself
#going clockwise would make little sense as you go from few little fish to a lot of big fish
#which is wrong