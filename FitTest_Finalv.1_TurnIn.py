import holopy as hp, numpy as np
from holopy.core.process import normalize, subimage, center_find
from holopy.scattering import Sphere, calc_holo
from holopy.inference import prior, TemperedStrategy, AlphaModel, ExactModel
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import h5py

pix=0.43**2  #Pixel Size
frame=10 #Framerate
med_n=1.33; wl=0.633; pol=(1,0); medwl=wl/med_n
H=10 #Number of frames to Analyze over
yy=np.linspace(0,(H-1)/frame,H) #Time Axis
Hx=np.zeros(H)
Hy=np.zeros(H)
Hz=np.zeros(H)
Hrr=np.zeros(H)
Hxerr=np.zeros(H)
Hyerr=np.zeros(H)
Hzerr=np.zeros(H)

def CustomFit(midx,midy,z,ExHolo):
    x = prior.Uniform(int(0*pix), int(120*pix), midx*pix)
    y = prior.Uniform(int(0*pix), int(120*pix), midy*pix)
    z = prior.Uniform(-10,1,z)
    par_sphere = Sphere(n=1.59, r=prior.Gaussian(1.5, 0.15), center=[x, y, z])
    noise_sd=ExHolo.std()
    model = ExactModel(scatterer=par_sphere, calc_func=calc_holo, noise_sd=noise_sd, theory='auto')
    fit_result = hp.fit(ExHolo, model)
    
    ExFitVal = fit_result.parameters
    #InitGuessValues = fit_result.guess_parameters
    BestFitSphere = fit_result.scatterer
    BestFitHolo= fit_result.hologram
    #BestFitProb = fit_result.max_lnprob
    
    return ExFitVal,BestFitSphere, BestFitHolo#, InitGuessValues, BestFitSphere, BestFitHolo, BestFitProb

def Analysis(pos): #MSD Analyzer
    DR=np.zeros((H,len(pos)))
    for h in range(1,H+1):
        for i in range(0,len(pos)):
            if (i+h)>=len(pos):
                DR[h-1][i]=0
                
            else:
                DR[h-1][i]=((pos[i+h]-pos[i])**2)/(len(pos)-h)
    return DR

def Image():
    Images=[#put images here]
    x=np.zeros(len(Images))
    y=np.zeros(len(Images))
    z=np.zeros(len(Images))
    r=np.zeros(len(Images))
    
    
    for i in range(0,len(Images)):
        data_holo=hp.load_image(Images[i],pix, med_n, wl, pol)
        data_holo=normalize(data_holo)
        mid=center_find(data_holo,threshold=0.55,blursize=0.15)
        if i==0:
            BFV,BFS,BFH=CustomFit(mid[0],mid[1],0,data_holo)
        else:
            BFV,BFS,BFH=CustomFit(mid[0],mid[1],z[i-1],data_holo)
        r[i]=BFV.get('r')
        x[i]=mid[0]*pix#BFV.get('center.0')
        y[i]=mid[1]*pix#BFV.get('center.1')
        z[i]=BFV.get('center.2')
    
   return x, y, z, r
    
X,Y,Z,R=Image()
n=len(X)
Analrr=Analysis(rr)
Analx=Analysis(X)
Analy=Analysis(Y)
Analz=Analysis(Z)


for h in range(0,H):
    Hx[h]=sum(Analx[h])
    Hy[h]=sum(Analy[h])
    Hz[h]=sum(Analz[h])
    Hrr[h]=sum(Analrr[h])
    
    for i in range(0,n-h):
        #Standard error of the mean
        Hxerr[h]+=np.sqrt((Analx[h][i]-(sum(Analx[h])/(n-h)))**2)/np.sqrt(n-h-1)
        Hyerr[h]+=np.sqrt((Analy[h][i]-(sum(Analy[h])/(n-h)))**2)/np.sqrt(n-h-1)
        Hzerr[h]+=np.sqrt((Analz[h][i]-(sum(Analz[h])/(n-h)))**2)/np.sqrt(n-h-1)
    
    
mx,bx=np.polyfit(yy,Hx,1)
my,by=np.polyfit(yy,Hy,1)
mz,bz=np.polyfit(yy,Hz,1)
mrr,brr=np.polyfit(yy,Hrr,1)

Dexp=0.278

#Many plot functions

#plt.figure()   
#plt.errorbar(yy,Hx,yerr=Hxerr,fmt='+')
#plt.plot(yy,mz*yy+bz)
#plt.errorbar(yy,Hy,yerr=Hyerr,fmt='*')
#plt.errorbar(yy,Hz,yerr=Hzerr,fmt='o')
#plt.plot(yy,Hrr,'*')
#plt.plot(yy,Dexp*yy)
#plt.xlabel("Time (s)")
#plt.ylabel("Mean Squared Displacement (microns)")
#plt.title("Mean Squared Displacement for X")
#plt.legend(['X MSD Linear Fit','X MSD'])
#plt.figure()
#plt.axes(projection='3d').plot3D(X,Y,Z)  


