def Problem3(p):
    import numpy as np
    from scipy.interpolate import interp1d
    import matplotlib.pyplot as plt
    x=[1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    y=[4.7, 3.5, 3.0, 2.7, 3.0, 2.4]
    xnew=np.linspace(1,1.5,num=100,endpoint=True)
    f2=interp1d(x,y,kind='cubic')
    plt.plot(x,y,'x',xnew,f2(xnew))
    plt.xlabel('Molar Volume')
    plt.ylabel('Pressure')  #plotting both the true points and the spline

#main
Problem3(3.25)
