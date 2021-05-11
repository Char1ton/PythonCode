def Problem1(tt,xx,n,N,D):
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(0,xx,N+1)
    delt=tt/n
    delx=xx/N
    a=(D*delt)/(delx**2)
    U=np.zeros((n+1,N+1))
    A=np.zeros((N+1,N+1))
    np.fill_diagonal(A,2*a+1) #creating the diagonal matrix A
    for i in range(0,N-1):
        if i ==0:
            A[0][i+1]=-a
        else:
            A[i][i+1]=-a
            A[i][i-1]=-a
    A[N][N-1]=-a
    for i in range(0,N+1): #setting the "heat" of the bar at the center at t=0
        if i==N/2:
            U[0][i]=1
        else:
            U[0][i]=0
    for i in range(0,N+1):
            UFl=np.vstack(U[i])
            XX=np.linalg.solve(A,UFl)
            U[i+1,:]=XX[:,0]       #solving the heat equation and plotting different times below
    plt.plot(x,U[0],label="Time=0")
    plt.plot(x,U[1],label="Time=1")
    plt.plot(x,U[5],label="Time=5")
    plt.plot(x,U[10],label="Time=10")
    plt.plot(x,U[20],label="Time=20")
    plt.legend()
    plt.xlabel("Arbitrary Distance")
    plt.ylabel("Arbitrary Heat")
#Main
Problem1(20,2,200,10,0.1)