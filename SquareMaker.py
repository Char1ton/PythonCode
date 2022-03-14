import numpy as np
import matplotlib.pyplot as plt
import math as m
import random as rand
import imageio
import os

def ThreeDPlot(Pos):
    Xp=[]
    Yp=[]
    Zp=[]
    for n in range(0,len(Pos)):
        Xp.append(Pos[n][0])
        Yp.append(Pos[n][1])
        Zp.append(Pos[n][2])
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(Xp, Yp, Zp, color = "green")
    plt.title("simple 3D scatter plot")
    plt.xlim([0,1])
    plt.ylim([0,1])
    ax.set_zlim([0,1])
    

def ThreeDPositionInit(N,X,Y,Z):
    PosInit=[]
    density=N/(X*Y*Z)
    Cube=int(N**(1/3))#+1
    for i in range(1,Cube+1):
        for j in range(1,Cube+1):
            for k in range(1,Cube+1):
                PosInit.append((X*i/(Cube+1),Y*j/(Cube+1),Z*k/(Cube+1)))
    return PosInit, density

def ThreeDVelInit(N):
    VelInit=[]
    for n in range(0,N):
        VelInit.append((rand.gauss(0,0.5),rand.gauss(0,0.5),rand.gauss(-0.5,0.5)))
    return VelInit

def Motion(Pos,Vel):
    PosM=np.zeros((100,8,3))
    VelM=np.zeros((100,8,3))
    T=1
    dt=0.01
    PosM[0]=Pos
    VelM[0]=Vel
    for t in range(1,int(T/dt)):
        for n in range(0,int(len(Pos))):
            for i in range(0,3):
                PosM[t][n][i]=PosM[t-1][n][i]+VelM[t-1][n][i]*dt
                VelM[t][n][i]=VelM[t][n][i]
                PosM[t][n][i],VelM[t][n][i]=Wall(10,dt,PosM[t][n][i],VelM[t-1][n][i])
    ET=EnergyState(VelM)
                
    return PosM,VelM,ET

def Wall(X,dt,Pos,Vel):
    if X-Pos<=0.01 or Pos<=0.01:
        Pos=Pos-Vel*dt
        Vel*=-0.95
        print('Bounce')
    else:
        Vel=Vel
        Pos=Pos
    return Pos, Vel

def EnergyState(Vel):
    E=[]
    for t in range(0,100):
        E.append(sum(sum(Vel[t]**2)/2))
    return E

Time=np.linspace(0,99,100)
TestPos,Density=ThreeDPositionInit(8,1,1,1)
TestVel=ThreeDVelInit(8)
TestMotionPos,TestMotionVel,ET=Motion(TestPos,TestVel)

plt.plot(Time,ET)
print(ET)
