import numpy as np
import matplotlib.pyplot as plt

#Constants
beta=1/10
m=5
om=1
N=100
L=10
h=100
dt=0.01

#Velocity Verlot
def new_pos(r,v,F,dt):
    rnew= r+(v*dt)+(0.5*(dt**2)*F)/m
   
    return rnew

def new_vel(v,Fnew,F,dt):
    vnew=v+(0.5*dt*(Fnew+F))/m
    return vnew

#Initial Conditions
def Pos0(N, L):
    pos=np.random.randint(1000,size=(N,2))/100
    return pos

def Vel0(N):
    vel=np.random.rand(N,2)
    
    return vel

#Force Calculation
def Force(pos,N,om):
    F=np.zeros((N,2))
    Fx=np.zeros((N,N))
    Fy=np.zeros((N,N))
    f=np.zeros((N,N))
    for i in range(0,N):
        for j in range(0,N):
            Rij=np.sqrt((pos[j,0]-pos[i,0])**2+(pos[j,1]-pos[i,1])**2)
            if i==j:
                f[i,j]=0
                Fx[i,j]=f[i,j]
                Fy[i,j]=f[i,j]
            elif Rij<=0.1:
                f[i,j]=-0.1
                Fx[i,j]=f[i,j]*(pos[j,0]-pos[i,0])/Rij
                Fy[i,j]=f[i,j]*(pos[j,1]-pos[i,1])/Rij
            else:
                f[i,j]=-(24*(om**6)*(Rij**6-2*om**6))/Rij**13
                Fx[i,j]=f[i,j]*(pos[j,0]-pos[i,0])/Rij
                Fy[i,j]=f[i,j]*(pos[j,1]-pos[i,1])/Rij
        F[i,0]=sum(Fx[:,0])
        F[i,1]=sum(Fy[:,1])
    return F

#Putting it all together and recording data
def Sim(N, L, h, dt):
    T=np.linspace(0,h*dt,h)
    R = Pos0(N, L)
    V = Vel0(N)
    K=np.zeros(h)
    RR=np.zeros((h,N))
    Vavg=np.zeros(h)
    PS=np.zeros((N,N))
    for i in range(0,N):
            for j in range(0,N):
                PS[i,j]=np.sqrt((R[j,0]-R[i,0])**2+(R[j,1]-R[i,1])**2)
    for ii in range(0,N):
        RR[0,ii]=np.sum(PS[ii,:])
    Rsum=np.sum(RR[:,0])/N-1
    
    Ravg=np.zeros(h)
    U=np.zeros(h)
    
    
    Ravg[0]=Rsum
    
    K[0]=0.5*m*np.sum(V**2)
    
    Vavg[0]=np.sum(V**2)/N
    
    
#Change over time 
    for t in range(1,h):
        PSt=np.zeros((N,N))
        F=Force(R,N,om)
        rnew = new_pos(R, V, F, dt)
        Fnew = Force(rnew,N,om)
        vnew=new_vel(V,Fnew,F,dt)
        for i in range(0,N):
            for j in range(0,N):
                PSt[i,j]=np.sqrt((rnew[j,0]-rnew[i,0])**2+(rnew[j,1]-rnew[i,1])**2)
        for ii in range(0,N):
            RR[t,ii]=np.sum(PSt[ii,:])
        #Boundary conditions, I could never get the incident velocity given the assignment to work
        #So I just chose my own incident velocity
        for n in range(0,N):
            if rnew[n,0]>=10:
                vnew[n,0]=-vnew[n,0]/100
            elif rnew[n,0]<=0:
                vnew[n,0]=-vnew[n,0]/100
            if rnew[n,1]>=10:
                vnew[n,1]=--vnew[n,1]/100
            elif rnew[n,1]<=0:
                vnew[n,1]=-vnew[n,1]/100
        
        Rsum=np.sum(RR[:,t])
        Ravg[t]=Rsum
        Vavg[t]=np.sum(vnew**2)/N
        K[t]=0.5*m*np.sum(vnew**2)
    R, V = rnew, vnew
    plt.figure()
    plt.plot(T,Vavg)
    plt.title("Average Velocity")
    plt.show()
    plt.figure()
    plt.plot(T,K)
    plt.title("Instantaneous Internal Energy")
    plt.show()
    plt.figure()
    plt.plot(T,Ravg)
    plt.title("Average Seperation")
    plt.show()
Sim(N,L,h,dt)


#I understand that these plots are wrong and i'm going to explain why i think so
#I think my force calculation is wonky to say the least. In with this I think how I am
#Calculatin my "radius" for each particle is listed incorrectly but I can't find where I am wrong
#and i've already put 12 hours into this and still can't figure it out





