# -*- coding: utf-8 -*-
"""
Common functions for analysis of median filter characteristics
Created on Thu Oct 15 10:07:55 2015

@author: Dominik
"""
import numpy as _np
import matplotlib.pylab as _plt





#Calculate the the median filtered wave with defined window length 
def _medianFilter( data, windowLength ): 
    if (windowLength < len(data)and data.ndim == 1):
        tempret = _np.zeros(len(data)-windowLength+1)                      # creating an array where the filtered values will be saved in
        if windowLength % 2 ==0:                                            # check if the window length is odd or even because with even window length we get an unsynchrone filtered wave 
            for c in range(0, len(tempret)):
                tempret[c] = _np.median( data[ c : c + windowLength +1 ] ) # write the values of the median filtered wave in tempret, calculate the median of all values in the window
            return tempret
        else:
            for c in range(0, len(tempret)):
                tempret[c] = _np.median( data[ c : c + windowLength ] )
            return tempret
    else:
         raise ValueError("windowLength must be smaller than len(data) and data must be a 1D array")

#
def _medianFilterPlotterImpl( data, windowLength ):
    datafiltered = _medianFilter(data, windowLength)            #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ]             # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]                   # cut the filtered wave to the same length as the data wave
    _plt.plot( data )
    _plt.plot( datafiltered )
    _plt.plot( data-datafiltered )


#Plot all calculated waves, the sine wave, the filtered wave and the difference between bot waves  
def medianSinPlot( waveNumber, windowLength ):
    """ Plots a sine wave, the  medain filtered and the difference between sine and median filtered wave """   
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )   #creating an array with a sine wave
    _medianFilterPlotterImpl(data,windowLength) 
    
    
#Plot all calculated waves, the sine wave, the filtered wave and the difference between bot waves  
def medianSinPlotNoised( waveNumber, windowLength ):
    """ Plots a noised sine wave, the  medain filtered and the difference between sine and median filtered wave """ 
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )   #creating an array with a sine wave
    noise = _np.random.normal(0,0.2,(128 + windowLength / 2))
    data = data + noise
    _medianFilterPlotterImpl(data,windowLength)


#Calculate the error rate of the filtered wave  with different windowLength and defined wave number       
def _ErrorRateWindow(data, datafiltered, windowLength):
    errorrate = data-datafiltered                     #calculate the difference between the sine wave and the filtered wave
    error = []                                        #creating a list and save the error rate with the matching wavenumber in it 
    errorrate = _np.abs(errorrate)
    error.append([windowLength ,_np.mean(errorrate)])# fill the list with the errorrate and corresponding wave number
    error = zip(*error)                               #zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3])
    return error


def _windowErrorPlotterImpl(data,windowLength):
    datafiltered = _medianFilter(data, windowLength)         #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ]          # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]                # cut the filtered wave to the same length as the data wave
    error = _ErrorRateWindow(data,datafiltered,windowLength) #calculate the error with the ErrorRate function
    _plt.axis([0, windowLength + 1, 0, 1.2])
    _plt.xlabel('Window Length', fontsize = 20)
    _plt.ylabel('Error rate', fontsize = 20)
    _plt.scatter(*error)


#Plots the error of the median filter with different windowLength and a defined wave number
def ErrorPlotWindow( waveNumber,windowLength ):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different window lengths and fixed wave number"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )    #creating an array with a sine wave
    _windowErrorPlotterImpl(data,windowLength)
    

def ErrorPlotWindowNoised( waveNumber,windowLength ):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different window lengths and fixed wave number, sine wave is noised"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )
    noise =_np.random.normal(0,0.5,(128 + windowLength / 2))
    data = data + noise
    _windowErrorPlotterImpl(data,windowLength)
    
 
#Calculate the error rate of the filtered wave  with different wave number and defined window length      
def _ErrorRateWave(data,datafiltered, waveNumber):
    errorrate = data-datafiltered                   #calculate the difference between the sine wave and the filtered wave
    error = []                                      #creating a list and save the error rate with the matching wave number in it 
    errorrate = _np.abs(errorrate)
    error.append([waveNumber ,_np.mean(errorrate)])# fill the list with the errorrate and corresponding wave number
    error = zip(*error)                             #zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3])
    return error   
    
 
def _waveErrorPlotterImpl(data,waveNumber,windowLength):
    datafiltered = _medianFilter(data, windowLength)                  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ]                   # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]                         # cut the filtered wave to the same length as the data wave
    error = _ErrorRateWave(data,datafiltered,waveNumber) #calculate the error with the ErrorRate function
    _plt.axis([0, waveNumber + 1, 0, 1.2])
    _plt.xlabel('Wave number', fontsize = 20)
    _plt.ylabel('Error rate', fontsize = 20)
    _plt.scatter(*error)
  
  
#Plots the error  of the median filter with different wave number and a defined window length      
def ErrorPlotWave(waveNumber,windowLength):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different wave number and fixed window length"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )    #creating an array with a sine wave
    _waveErrorPlotterImpl(data,waveNumber,windowLength)

    
#Plots the error  of the median filtered, noised with different wave number and a defined window length     
def ErrorplotWaveNoised( waveNumber, windowLength ):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different wave number and fixed window length, sine wave is noised"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/128 * 2 * _np.pi * waveNumber), (128 + windowLength / 2, ) )
    noise = _np.random.normal(0,0.5,(128 + windowLength / 2))
    data = data + noise
    _waveErrorPlotterImpl(data,waveNumber)
        


#def filterResidual(data, dataSlidingMedian):
#    dataMedianFiltered = data - dataSlidingMedian
#    return np.mean( np.abs(dataMedianFiltered) )

 

    
"""Because of problems with the low number of samples, I define the same functions with 1024 samples instead of 128."""
              
#Plot all calculated waves, the sine wave, the filtered wave and the difference between bot waves  
def medianSinPlot1024( waveNumber, windowLength ):
    """ Plots a sine wave, the  medain filtered and the difference between sine and median filtered wave with 1024 samples """
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/1024 * 2 * _np.pi * waveNumber), (1024 + windowLength / 2, ) )   #creating an array with a sine wave
    _medianFilterPlotterImpl(data,windowLength)


#Calculate a noised sine wave to get a more realistic wave
def medianSinPlotNoised1024( waveNumber, windowLength ):
    """ Plots a noised sine wave, the  medain filtered and the difference between sine and median filtered wave with 1024 samples"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/1024 * 2 * _np.pi * waveNumber), (1024 + windowLength / 2, ) ) #creating an array with a sine wave
    noise = _np.random.normal(0,0.2,(1024 + windowLength / 2))       # creating the noise as an array, filled with random numbers, with the same length as the data array
    data = data + noise                                               # generate the noised signal
    _medianFilterPlotterImpl(data,windowLength)


#Plots the error of the median filter with different windowLength and a defined wave number
def ErrorPlotWindow1024( waveNumber,windowLength ):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different window lengths and fixed wave number, the waves are plotted with 1024"""
    data = _np.fromfunction(lambda x: _np.sin((x-windowLength / 2)/1024 * 2 * _np.pi * waveNumber), (1024 + windowLength / 2, ))    #creating an array with a sine wave
    _windowErrorPlotterImpl(data,windowLength)
    
      
#Plots the error  of the median filter with different wave number and a defined window length      
def ErrorPlotWave1024(waveNumber,windowLength):
    """ Plots the Errror(mean of the absolute from sine wave - filtered wave) of the median filter, with different wave number and fixed window length, the waves are plotted with 1024"""
    data = _np.fromfunction( lambda x: _np.sin((x-windowLength / 2)/1024 * 2 * _np.pi * waveNumber), (1024 + windowLength / 2, ) )    #creating an array with a sine wave
    _waveErrorPlotterImpl(data,waveNumber,windowLength)
  
