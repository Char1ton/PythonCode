#imports
import numpy as np
from matplotlib import pyplot as plt

#Globals
N=4 #Number of particles
F_air=20 #Average Force of the air
F_grav=10 #Force of Gravity, constant
F_tot=F_air-F_grav
m=1 #Mass of particle, kept unity for now
dt=0.1 #Time Step
TT=int(10/dt)


#Containers
T=np.linspace(0,10,TT)
Energy=[]
B=0

#Boundary Conditions
R=10 #Wall is defined as a semi-infinite hollow cylinder with inner radius R.
r=0.001 #Radius of the particle

#Functions
def Init(N): #Inititalization of starting positions and velocities
    Pos=np.zeros((N,2,len(T))) #Records x, y, and z position
    Vel=np.zeros((N,2,len(T))) #Records x, y, and z velocity    

    for j in range(0,N):
        
        Pos[j][0][0]=np.random.normal(0,1)
        Pos[j][1][0]=np.random.normal(0,1)
        #Pos[n][2][0]=0
        
        
        Vel[j][0][0]=np.random.normal(0,0.1)
        Vel[j][1][0]=np.random.normal(0,0.1)
        #Vel[n][0][0]=1
        
    return Pos, Vel
    
def VelocityVerlet(Pos,Vel,Bounce,Bump): #Velocity Verlet time step
    for i in  range(0,len(T)-1):
        for n in range(0,N):
            Pos[n][0][i+1]=Pos[n][0][i]+Vel[n][0][i]*dt
            Pos[n][1][i+1]=Pos[n][1][i]+Vel[n][1][i]*dt
            #Pos[n][2][i+1]=Pos[n][2][i]+Vel[n][2][i]*dt+(1/2)*F_tot*dt**2
            Vel[n][0][i+1]=Vel[n][0][i]
            Vel[n][1][i+1]=Vel[n][1][i]
            #Vel[n][2][i+1]=Vel[n][2][i]+F_tot*dt
            
            
            #Interactions
            
            #Wall Interaction
            if abs(Pos[n][0][i])>R:
                Pos[n][0][i+1]=(Pos[n][0][i]/abs(Pos[n][0][i]))*R
                Vel[n][0][i+1]=-Vel[n][0][i]*0.5
                Bounce=Bounce+1
                
            if abs(Pos[n][1][i])>R: 
                Pos[n][1][i+1]=(Pos[n][1][i]/abs(Pos[n][1][i]))*R
                Vel[n][1][i+1]=-Vel[n][1][i]*0.5
                Bounce=Bounce+1
            
            #Particle on Particle
            
        for q in range(0,N-1):
            for h in range(q+1,N):
                if Pos[h][0][i]-Pos[q][0][i]<=2*r and Pos[h][1][i]-Pos[q][1][i]<=2*r:
                    
                    Vel[h][0][i+1]=Vel[q][0][i]*0.9
                    Vel[h][1][i+1]=Vel[q][1][i]*0.9
                    Vel[q][0][i+1]=Vel[h][0][i]*0.9
                    Vel[q][1][i+1]=Vel[h][1][i]*0.9
                    Bump=Bump+1
            
            if i==len(T)-2:    
                EnergyTot(Vel[n])
            
    return Pos, Vel, Bounce, Bump

def Fine(Energy):
    Fine=1-(Energy[0][TT-1]/Energy[0][0])
    
    return Fine

def EnergyTot(Vel):
    EnergyX=(1/2)*Vel[0]**2
    EnergyY=(1/2)*Vel[1]**2
    #EnergyZ=(1/2)*Vel[2]**2
    EnergySum=EnergyX+EnergyY#+EnergyZ
    
    Energy.append(EnergySum)
    
    return Energy


def Main():
    P, V=Init(N)
    Pf, Vf, Bounce, Bump=VelocityVerlet(P,V,B,B)
    
    F=Fine(Energy)
    
    
    plt.plot(T,Energy[0])
    
    print(Bounce,Bump)
    
    print(F)

Main()