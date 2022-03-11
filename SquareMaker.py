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
    #plt.xlim([0,1])
    #plt.ylim([0,1])
    #ax.set_zlim([-1,1]))
    

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
        VelInit.append((rand.random(),rand.random(),-1*abs(rand.random())))
    return VelInit

def Motion(Pos,Vel):
    PosM=np.zeros((10,27,3))
    VelM=np.zeros((10,27,3))
    T=1
    dt=0.1
    PosM[0]=Pos
    VelM[0]=Vel
    for t in range(1,int(T/dt)):
        for n in range(0,int(len(Pos))):
            for i in range(0,3):
                PosM[t][n][i]=PosM[t-1][n][i]+VelM[0][n][i]*dt
                
    return PosM,VelM

def GifMaker(frames,pos):
        
    p=pos
                
TestPos,Density=ThreeDPositionInit(27,1,1,1)
TestVel=ThreeDVelInit(27)
TestMotionPos,TestMotionVel=Motion(TestPos,TestVel)
GifMaker(10,TestMotionPos)
#print(TestMotionPos)
