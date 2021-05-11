def Problem3():
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    from mpmath import sec
    n=50
    f=[]
    fcder=[]
    ffder=[]
    fder=[]
    nx=[]
    ErrCen=np.zeros(n-10)
    ErrFor=np.zeros(n-10)
    XX=np.linspace(10,n-1,n-10)
    for j in range(10,n):
        x= np.linspace(-2, 2, j)
        delx=(4/j)
        nx.append(delx)
        for i in range(len(x)):
                f.append(m.tan(x[i])) #tan(x) function
        for i in range(1,len(x)-1):
                fcder.append((f[i+1]-f[i-1])/(2*delx)) #Central derivative
        for i in range(1,len(x)-1):
                ffder.append((f[i+1]-f[i])/(delx)) #forward derivative
        for i in range(1,len(x)-1):
                fder.append((sec(x[i])*sec(x[i]))) #analytical derivative
        ErrCen[j-10]=abs(sum(np.subtract(fcder,fder)))
        ErrFor[j-10]=abs(sum(np.subtract(ffder,fder)))
    print(ErrCen)
    plt.loglog(XX,ErrCen,label='Central Error')
    plt.loglog(XX,ErrFor,label='Forward Error')
    plt.legend()
    plt.xlabel('log(N)')
    plt.ylabel('Log(Error)')


#I know this function is wrong but i do not understand why
#I have a suspision that it is with me "summing" the Error instead of having it as a list
#but it was the only way i could get a value and how i understood the question, but my intuition on the 
#loglog plot tells me this is wrong, If possible i would like to have a discussion with either the TA or the Proffessor on what i did wrong

#main
Problem3()