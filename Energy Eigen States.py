def Problem2(N,n):
    import numpy as np
    H=np.zeros((N,N))
    x=np.linspace(0,1,n)
    dx=1/n
    Uj=[]
    Ui=[]
    V=(1/2)*x**2
    Uider=np.zeros((N,len(x)))
    Uider2=np.zeros((N,len(x)))
    Hint=np.zeros((N,len(x)))
    Sij=[]
    Sijint=np.zeros((N,len(x)))
    SijintSum=[]
    HintSum=[]
    #All of what is above is to just store values 
    for i in range(0,N):
        Uj.append(np.sin(i*(np.pi)*x)) #assuming that the functions are orthoganol i set them up
        Ui.append(np.sin(i*(np.pi)*x))        
    for i in range(0,N):
        for j in range(0,len(x)-1):
            ider=(Ui[i][j+1]-Ui[i][j])/dx #calculating the first derivative, i do the same on the next for loop for the 2nd derivative
            Uider[i][j]=ider
            
    for i in range(0,N):
        for j in range(0,len(x)-2):
            ider2=(Uider[i][j+1]-Uider[i][j])/dx
            Uider2[i][j]=ider2
    VUi=V*Ui
    HUi=VUi-Uider2
    HUij=HUi*Uj
    
    for i in range(0,N):
        for j in range(0,len(x)-1):
            F=((HUij[i][j+1]-HUij[i][j])*(dx/2))+(HUij[i][j]*dx) #numerically integrating for the Hamiltonian
            Hint[i][j]=F
            
    for i in range(0,N):
        HintSum.append(sum(Hint[i]))
    for i in range(0,N):
        Sij.append(Ui[i]*Uj[i])
        
    for i in range(0,N):
        for j in range(0,len(x)-1):
            Sijint[i][j]=((Sij[i][j+1]-Sij[i][j])*(dx/2))+(Sij[i][j]*dx) #integrating for the normalization
    
    for i in range(0,N):
        SijintSum.append(sum(Sijint[i]))
    np.fill_diagonal(H,HintSum) #diagonalizing the hamiltonian to solve for the Energy Eigens
    SS=np.linalg.eig(H)
    Eig=(SS[0]*SijintSum)
    
    
    print("Energy Eigen Values :",Eig) # the solution to the energy eigens, approximated as we do have error from the derivatives and integrals

Problem2(10,1000)
