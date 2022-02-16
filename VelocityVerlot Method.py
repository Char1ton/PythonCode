#Imports
import numpy as np
from matplotlib import pyplot as plt
import random

#Variables

N=2 #Number of particles
R=0.1 #Radius of particle
T=20 #Time Steps
L=2 #Length of the Box

#Universal Containers
Time=np.linspace(0,1,T)


#Functions

def Init(N,T):
    
    #Zeros Init; Init[Particle][X][Y]
    PosInit=np.zeros((N,T,2))
    VelInit=np.zeros((N,T,2))
    
    #Step 1 Init
    for i in range(0,N):
        PosInit[i][0][0]=random.gauss(0,1)
        PosInit[i][0][1]=random.gauss(0,1)
        VelInit[i][0][0]=random.gauss(0,1)
        VelInit[i][0][1]=random.gauss(0,1)

    return PosInit, VelInit

def Move(Pos,Vel,R,L,N,T):
    for t in range(1,T):
        for n in range(0,N):
            Pos[n][t][0]=Pos[n][t-1][0]+Vel[n][t-1][0]*(1/T)
            Pos[n][t][1]=Pos[n][t-1][1]+Vel[n][t-1][1]*(1/T)
            Vel[n][t][0]=Vel[n][t-1][0]
            Vel[n][t][1]=Vel[n][t-1][1]
            if abs(Pos[n][t][0])>=L-R:
                Vel[n][t][0]=-Vel[n][t-1][0]
            if abs(Pos[n][t][1])>=L-R:
                Vel[n][t][1]=-Vel[n][t-1][1]
                           
    return Pos, Vel

PosInit,VelInit=Init(N,T)
Pos, Vel=Move(PosInit,VelInit,R,L,N,T)
print(Pos,Vel)