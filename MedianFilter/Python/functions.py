# -*- coding: utf-8 -*-
"""
Common functions for analysis of median filter characteristics
Created on Thu Oct 15 10:07:55 2015

@author: Dominik
"""
import numpy as _np
import matplotlib.pylab as _plt
import scipy.signal as _sps

def _medianFilter(data, windowLength): 
    """Calculate the the median filtered wave with defined window length."""
    if (windowLength < len(data) and data.ndim == 1):
        # Creating an array where the filtered values will be saved in.
        tempret = _np.zeros(len(data)) 
        # Check if the window length is odd or even because with 
        # even window length we get an unsynchrone filtered wave.                     
        if windowLength % 2 == 1:                                            
            tempret = _sps.medfilt(data,windowLength) 
            return tempret
        else:
            raise  ValueError('Window length  should be odd')

    else:
         raise ValueError("windowLength must be smaller " + 
                          "than len(data) and data must be a 1D array")

def _medianFilterPlotterImpl(data, windowLength, plotStart, plotEnd):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)
    data = data[plotStart : plotEnd]
    datafiltered = datafiltered[plotStart : plotEnd]
    _plt.axis([0, len(data), -1.5, 1.5])                 
    _plt.plot(data)
    _plt.plot(datafiltered, )
    _plt.plot(data - datafiltered, linewidth = 1.9)
    
def medianSinPlot(waveNumber, windowLength, samples=128, plotStart=0, plotEnd=-1):
    """ Plot a sine wave, the  medain filtered and the difference between
    sine and median filtered wave.
    """ 
    time = _np.linspace(0,2,samples)
    # Creating an array with sine waves.
    data = _np.sin(_np.pi* time *waveNumber) 
    _medianFilterPlotterImpl(data,windowLength,plotStart, plotEnd)
        
def medianSinPlotNoised(waveNumber, windowLength, samples=128, plotStart=0, plotEnd=-1):
    """ Plot a noised sine wave, the  medain filtered and the difference
    between sine and median filtered wave.
    """ 
    time = _np.linspace(0,2,samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise = _np.random.normal(0,0.2,len(data))
    data = data + noise
    _medianFilterPlotterImpl(data, windowLength, plotStart, plotEnd)
       
def _ErrorRateWindow(data, datafiltered, windowLength):
    """Calculate the error rate of the filtered wave
    with different windowLength and defined wave number.
    """
    # Calculate the difference between the sine wave and the filtered wave.
    errorrate = data-datafiltered                    
    error = []                                        
    errorrate = _np.abs(errorrate)
    # Fill the list with the errorrate and corresponding wave number.
    error.append([windowLength ,_np.mean(errorrate)])
     # Zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3]).
    error = zip(*error)                              
    return error

def _windowErrorPlotterImpl(data, windowLength, waveNumber):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength) 
    error = _ErrorRateWindow(data,datafiltered, windowLength)
    error = _np.asarray(error)
    error[1:] = error[1:]/0.63662
    
    ax = _plt.subplot()
    _plt.axis([0, windowLength+1, 0, 1.5])
    #_plt.xlabel('Window Length', fontsize=13)
    #_plt.ylabel('resolution', fontsize=13)
    xticks = _np.arange(0, windowLength + 1, 128)
    ax.set_xticks(xticks)
    x_label = [r"${%s\pi}$" %(2*w) for w in range(0,len(xticks))]
    ax.set_xticklabels(x_label)
    _plt.scatter(*error, c='red', lw=0)
    _plt.hlines(1, 0, windowLength, color = 'b', linestyle='--')

def ErrorPlotWindow(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number
    """
    time = _np.linspace(0,2,samples)
    data = _np.sin(_np.pi*time*waveNumber)
    _windowErrorPlotterImpl(data,windowLength, waveNumber)
    
def ErrorPlotWindowNoised(waveNumber,windowLength,samples = 128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number,
    sine wave is noised
    """
    time = _np.linspace(0,2,samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise =_np.random.normal(0, 0.5, len(data))
    data = data + noise
    _windowErrorPlotterImpl(data, windowLength)
     
      
def _ErrorRateWave(data,datafiltered, waveNumber):
    """Calculate the error rate of the filtered wave
    with different wave number and defined window length
    """
    errorrate = data-datafiltered                   
    error = []                                       
    errorrate = _np.abs(errorrate)
    error.append([waveNumber, _np.mean(errorrate)])
    error = zip(*error)                             
    return error   
     
def _waveErrorPlotterImpl(data, waveNumber, windowLength):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)
    # Calculate the error with the ErrorRate function.                      
    error = _ErrorRateWave(data,datafiltered, waveNumber)
    _plt.axis([0, waveNumber + 1, 0, 1.2])
    _plt.xlabel('Wave number', fontsize=13)
    _plt.ylabel('resolution', fontsize=13)
    _plt.scatter(*error)
         
def ErrorPlotWave(waveNumber, windowLength, samples = 128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length
    """
    time = _np.linspace(0,2,samples)
    data = _np.sin(_np.pi*time*waveNumber)
    _waveErrorPlotterImpl(data,waveNumber,windowLength)
         
def ErrorplotWaveNoised(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length,
    sine wave is noised
    """
    time = _np.linspace(0,2,samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise = _np.random.normal(0, 0.5,len(data))
    data = data + noise
    _waveErrorPlotterImpl(data, waveNumber)
    
    
#==============================================================================
#        
# def _medianFilterPlotterImplLegend(data, windowLength, plotStart, plotEnd):
#     # Calculate the filtered wave with the medianFiltered function.
#     datafiltered = _medianFilter(data, windowLength)
#     data = data[plotStart : plotEnd]
#     datafiltered = datafiltered[plotStart : plotEnd]                     
#     p1 = _plt.plot(data)
#     p2 = _plt.plot(datafiltered)
#     p3 = _plt.plot(data - datafiltered)
#     _plt.legend((p1[0], p2[0], p3[0]), 
#                 ('Sine wave','Filtered wave', 'Resolution'),
#                  loc='lower center', ncol=3, labelspacing=0)
#     _plt.tight_layout()
#     
# def medianSinPlotLegend(waveNumber, windowLength, samples=128, plotStart=0,
#                         plotEnd=-1):
#     """ Plot a sine wave, the  medain filtered and the difference between
#     sine and median filtered wave.
#     """ 
#     time = _np.linspace(0,2,samples)
#     # Creating an array with sine waves.
#     data = _np.sin(_np.pi* time *waveNumber) 
#     _medianFilterPlotterImplLegend(data,windowLength,plotStart, plotEnd)
#==============================================================================