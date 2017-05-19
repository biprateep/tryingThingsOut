import numpy as np
import matplotlib.pyplot as plt

def MySineWave(waveLength):
    step=0.01
    xData=np.arange(-2*np.pi, 2**np.pi+step, step)
    yData=np.sin(2*np.pi*xData/float(waveLength))
    plt.plot(xData,yData)
    plt.grid()
    plt.xlim(-2*np.pi,2**np.pi)
    plt.show()
    
MySineWave(2.0)