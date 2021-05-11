import numpy as np
import matplotlib.pyplot as plt

NN=100

def walk(pos):
    Direction=np.random.randint(0,4)
    Distance=1
    if Direction==0:
        pos[0]=pos[0]+Distance
    elif Direction==1:
        pos[1]=pos[1]+Distance
    elif Direction==2:
        pos[0]=pos[0]-Distance
    elif Direction==3:
        pos[1]=pos[1]-Distance
    return pos

def Analysis(X,Y):
    DR=[]
    for i in range(NN-1):
        j=i+1
        DR.append(np.sum((X[0:-j]-X[j::])**2)/float(NN-j))
    return DR

def main():
    N=0
    pos=[0,0]
    X=[]
    Y=[]
    X.append(pos[0])
    Y.append(pos[1])
    yy=np.linspace(0,NN,NN)
    while N<NN-1:
        pos=walk(pos)
        X.append(pos[0])
        Y.append(pos[1])
        N+=1
    Rad=Analysis(X,Y)
    plt.plot(yy,Rad)

main()