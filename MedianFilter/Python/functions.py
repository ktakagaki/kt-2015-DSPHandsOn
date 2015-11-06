# -*- coding: utf-8 -*-
"""
Common functions for analysis of median filter characteristics
Created on Thu Oct 15 10:07:55 2015

@author: Dominik
"""
import numpy as _np
import matplotlib.pylab as _plt


 
def _medianFilter(data, windowLength): 
    """Calculate the the median filtered wave with defined window length."""
    if (windowLength < len(data) and data.ndim == 1):
         # Creating an array where the filtered values will be saved in.
        tempret = _np.zeros(len(data) - windowLength + 1) 
        # Check if the window length is odd or even because with 
        # even window length we get an unsynchrone filtered wave.                     
        if windowLength % 2 == 0:                                            
            for c in range(0, len(tempret)):
                # Write the values of the median filtered wave in tempret, 
                # calculate the median of all values in the window.
                tempret[c] = _np.median(data[c: c + windowLength + 1]) 
            return tempret
        else:
            for c in range(0, len(tempret)):
                tempret[c] = _np.median(data[c: c + windowLength])
            return tempret
    else:
         raise ValueError("windowLength must be smaller " + 
                          "than len(data) and data must be a 1D array")

def _medianFilterPlotterImpl(data, windowLength):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength) 
    # Slice the data array to synchronize both waves           
    data = data[windowLength/2 : -windowLength] 
    # Cut the filtered wave to the same length as the data wave            
    datafiltered = datafiltered[:len(data)]                   
    _plt.plot(data)
    _plt.plot(datafiltered)
    _plt.plot(data - datafiltered)

def medianSinPlot(waveNumber, windowLength):
    """ Plot a sine wave, the  medain filtered and the difference between
    sine and median filtered wave.
    """ 
    # Creating an array with sine waves.
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /128*2*_np.pi*waveNumber),
                            (128 + windowLength/2, ))   
    _medianFilterPlotterImpl(data,windowLength) 
        
def medianSinPlotNoised(waveNumber, windowLength):
    """ Plot a noised sine wave, the  medain filtered and the difference
    between sine and median filtered wave.
    """ 
    data = _np.fromfunction(lambda x: _np.sin((x-windowLength / 2)
                            /128*2*_np.pi*waveNumber),
                            (128 + windowLength / 2, ))
    noise = _np.random.normal(0,0.2,(128 + windowLength/2))
    data = data + noise
    _medianFilterPlotterImpl(data,windowLength)
       
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

def _windowErrorPlotterImpl(data,windowLength):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength) 
    # Slice the data array to synchronize both waves.
    data = data[ windowLength / 2 : - windowLength ]
    # Cut the filtered wave to the same length as the data wave.
    datafiltered = datafiltered[ : len(data) ]
    # Calculate the error with the ErrorRate function.
    error = _ErrorRateWindow(data,datafiltered,windowLength) 
    _plt.axis([0, windowLength+1, 0, 1.2])
    _plt.xlabel('Window Length', fontsize = 20)
    _plt.ylabel('Error rate', fontsize = 20)
    _plt.scatter(*error)

def ErrorPlotWindow(waveNumber,windowLength):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /128*2*_np.pi*waveNumber), 
                            (128 + windowLength/2,))
    _windowErrorPlotterImpl(data,windowLength)
    
def ErrorPlotWindowNoised( waveNumber,windowLength ):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number,
    sine wave is noised
    """
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)
                             /128 * 2 * _np.pi * waveNumber),
                             (128 + windowLength / 2, ) )
    noise =_np.random.normal(0,0.5,(128 + windowLength / 2))
    data = data + noise
    _windowErrorPlotterImpl(data,windowLength)
     
      
def _ErrorRateWave(data,datafiltered, waveNumber):
    """Calculate the error rate of the filtered wave
    with different wave number and defined window length
    """
    errorrate = data-datafiltered                   
    error = []                                       
    errorrate = _np.abs(errorrate)
    error.append([waveNumber ,_np.mean(errorrate)])
    error = zip(*error)                             
    return error   
     
def _waveErrorPlotterImpl(data,waveNumber,windowLength):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)                  
    data = data[ windowLength / 2 : - windowLength ]
    datafiltered = datafiltered[ : len(data) ]  
    # Calculate the error with the ErrorRate function.                      
    error = _ErrorRateWave(data,datafiltered,waveNumber)
    _plt.axis([0, waveNumber+1, 0, 1.2])
    _plt.xlabel('Wave number', fontsize = 20)
    _plt.ylabel('Error rate', fontsize = 20)
    _plt.scatter(*error)
         
def ErrorPlotWave(waveNumber,windowLength):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /128* 2*_np.pi*waveNumber),
                            (128 + windowLength/2,))
    _waveErrorPlotterImpl(data,waveNumber,windowLength)
         
def ErrorplotWaveNoised(waveNumber, windowLength):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length,
    sine wave is noised
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /128*2*_np.pi*waveNumber),
                            (128 + windowLength/2,))
    noise = _np.random.normal(0, 0.5, (128 + windowLength/2))
    data = data + noise
    _waveErrorPlotterImpl(data,waveNumber)


#Because of problems with the low number of samples, 
# I define the same functions with 1024 samples instead of 128.
  
            
def medianSinPlot1024( waveNumber, windowLength ):
    """ Plot a sine wave, the  medain filtered and the difference
    between sine and median filtered wave with 1024 samples.
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /1024*2*_np.pi*waveNumber), 
                            (1024 + windowLength/2,))
    _medianFilterPlotterImpl(data,windowLength)

def medianSinPlotNoised1024(waveNumber, windowLength):
    """ Plot a noised sine wave, the  medain filtered and the difference
    between sine and median filtered wave with 1024 samples.
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /1024*2*_np.pi*waveNumber),
                            (1024 + windowLength/2,))
    # Creating the noise as an array, filled with random numbers,
    # with the same length as the data array.
    noise = _np.random.normal(0, 0.2, (1024 + windowLength/2)) 
    # Generate the noised signal.      
    data = data + noise                                               
    _medianFilterPlotterImpl(data,windowLength)

def ErrorPlotWindow1024( waveNumber,windowLength ):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number,
    the waves are plotted with 1024 samples.
    """
    data = _np.fromfunction(lambda x: _np.sin((x - windowLength/2)
                            /1024*2*_np.pi*waveNumber),
                            (1024 + windowLength/2,))
    _windowErrorPlotterImpl(data, windowLength)
              
def ErrorPlotWave1024(waveNumber,windowLength):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length,
    the waves are plotted with 1024 samples
    """
    data = _np.fromfunction( lambda x: _np.sin((x - windowLength/2)
                            /1024*2*_np.pi*waveNumber),
                            (1024 + windowLength/2,))
    _waveErrorPlotterImpl(data, waveNumber, windowLength)