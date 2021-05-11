import numpy as np
import matplotlib.pyplot as plt

A=5
x=np.pi/4
t=np.linspace(0,10,200)
Psi=[]

for i in range(1,22):
    Psin=A*np.sin(x)*np.cos(i*t)
    Psi.append(Psin)
Sum2=Psi[0]+Psi[1]
Sum5=Psi[2]+Psi[3]+Psi[4]+Sum2
Sum20=0
for j in range(0,21):
    Sum20=Sum20+Psi[j]

plt.figure()
plt.plot(t,Sum2, label="2 Psi's")

plt.plot(t,Sum5, label="5 Psi's")

plt.plot(t,Sum20, label="20 Psi's")

plt.xlabel('Time t')
plt.ylabel('Arbitrary Amplitude')
plt.title("Pulsed Psi's at x=pi/4")
plt.legend()

