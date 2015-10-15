# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:07:55 2015

@author: Dominik
"""
import numpy as np
import matplotlib.pylab as plt



#Plots the error of the median filter with different windowLength and a defined wave number
def ErrorPlotWindow( waveNumber,windowLength ):
        data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) )    #creating an array with a sine wave
        datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
        data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
        datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
        error = ErrorRateWindow(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
        plt.axis([0, windowLength + 1, 0, 1.2])
        plt.xlabel('Window Length', fontsize = 20)
        plt.ylabel('Error rate', fontsize = 20)
        plt.scatter(*error)
    

def ErrorPlotWindowNoised( waveNumber,windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) )
    noise = np.random.normal(0,0.5,(128 + windowLength / 2))
    data = data + noise
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    error = ErrorRateWindow(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
    plt.axis([0, windowLength + 1, 0, 1.2])
    plt.xlabel('Window Length', fontsize = 20)
    plt.ylabel('Error rate', fontsize = 20)
    plt.scatter(*error)

    
    
    
    
#Plots the error  of the median filter with different wave number and a defined window length      
def ErrorPlotWave(waveNumber,windowLength):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) )    #creating an array with a sine wave
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    error = ErrorRateWave(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
    plt.axis([0, waveNumber + 1, 0, 1.2])
    plt.xlabel('Wave number', fontsize = 20)
    plt.ylabel('Error rate', fontsize = 20)
    plt.scatter(*error)

    
#Plots the error  of the median filtered, noised with different wave number and a defined window length     
def ErrorplotWaveNoised( waveNumber, windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) )
    noise = np.random.normal(0,0.5,(128 + windowLength / 2))
    data = data + noise
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    error = ErrorRateWave(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
    plt.axis([0, waveNumber + 1, 0, 1.2])
    plt.xlabel('Wave number', fontsize = 20)
    plt.ylabel('Error rate', fontsize = 20)
    plt.scatter(*error)
        
        
        
        
#Calculate the error rate of the filtered wave  with different wave number and defined window length      
def ErrorRateWave(data,datafiltered,windowLength, waveNumber):
    errorrate = data-datafiltered  #calculate the difference between the sine wave and the filtered wave
    error = [] #creating a list and save the error rate with the matching wave number in it 
    errorrate = np.abs(errorrate)
    error.append([waveNumber ,np.mean(errorrate)])# fill the list with the errorrate and corresponding wave number
    error = zip(*error) #zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3])
    return error



#Calculate the error rate of the filtered wave  with different windowLength and defined wave number       
def ErrorRateWindow(data,datafiltered,windowLength, waveNumber):
    errorrate = data-datafiltered  #calculate the difference between the sine wave and the filtered wave
    error = [] #creating a list and save the error rate with the matching wavenumber in it 
    errorrate = np.abs(errorrate)
    error.append([windowLength ,np.mean(errorrate)])# fill the list with the errorrate and corresponding wave number
    error = zip(*error) #zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3])
    return error





#Calculate the the median filtered wave with defined window length 
def medianFilter( data, windowLength ): 
    if (windowLength < len(data)and data.ndim == 1):
        tempret = np.zeros(len(data)-windowLength+1)  # creating an array where the filtered values will be saved in
        if windowLength % 2 ==0:                      # check if the window length is odd or even because with even window length we get an unsynchrone filtered wave 
            for c in range(0, len(tempret)):
                tempret[c] = np.median( data[ c : c + windowLength +1 ] ) # write the values of the median filtered wave in tempret, calculate the median of all values in the window
            return tempret
        else:
            for c in range(0, len(tempret)):
                tempret[c] = np.median( data[ c : c + windowLength ] )
            return tempret
    else:
         raise ValueError("windowLength must be smaller than len(data) and data must be a 1D array")
         


        
        
        

#Plot all calculated waves, the sine wave, the filtered wave and the difference between bot waves  
def medianSinPlot( waveNumber, windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) )   #creating an array with a sine wave
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : -windowLength  ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    plt.plot( data )
    plt.plot( datafiltered )
    plt.plot( data-datafiltered ) 
    
    
    
    

    
    
    
#Calculate a noised sine wave to get a more realistic wave
def medianSinPlotNoised( waveNumber, windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/128 * 2 * np.pi * waveNumber), (128 + windowLength / 2, ) ) #creating an array with a sine wave
    noise = np.random.normal(0,0.2,(128 + windowLength / 2))       # creating the noise as an array, filled with random numbers, with the same length as the data array
    signal = data + noise                                          # generate the noised signal
    datafiltered = medianFilter(signal, windowLength)              #calculate the filtered wave with the medianFiltered function
    signal = signal[ windowLength / 2 : - windowLength ]           # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(signal) ]                   # cut the filtered wave to the same length as the data wave
    plt.plot( signal )
    plt.plot( datafiltered )
    plt.plot( signal-datafiltered )
    
    
    
    
    
    
    
    
"""Because of problems with the low number of samples, I define the same functions with 1024 samples instead of 128."""

#Plots the error of the median filter with different windowLength and a defined wave number
def ErrorPlotWindow1024( waveNumber,windowLength ):
        data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/1024 * 2 * np.pi * waveNumber), (1024 + windowLength / 2, ) )    #creating an array with a sine wave
        datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
        data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
        datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
        error = ErrorRateWindow(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
        plt.axis([0, windowLength + 1, 0, 1.2])
        plt.xlabel('Window Length', fontsize = 20)
        plt.ylabel('Error rate', fontsize = 20)
        plt.scatter(*error)
    
    

    
    
    
    
#Plots the error  of the median filter with different wave number and a defined window length      
def ErrorPlotWave1024(waveNumber,windowLength):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/1024 * 2 * np.pi * waveNumber), (1024 + windowLength / 2, ) )    #creating an array with a sine wave
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : - windowLength ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    error = ErrorRateWave(data,datafiltered,windowLength,waveNumber) #calculate the error with the ErrorRate function
    plt.axis([0, waveNumber + 1, 0, 1.2])
    plt.xlabel('Wave number', fontsize = 20)
    plt.ylabel('Error rate', fontsize = 20)
    plt.scatter(*error)
        
                
#Plot all calculated waves, the sine wave, the filtered wave and the difference between bot waves  
def medianSinPlot1024( waveNumber, windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/1024 * 2 * np.pi * waveNumber), (1024 + windowLength / 2, ) )   #creating an array with a sine wave
    datafiltered = medianFilter(data, windowLength)  #calculate the filtered wave with the medianFiltered function
    data = data[ windowLength / 2 : -windowLength  ] # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(data) ]       # cut the filtered wave to the same length as the data wave
    plt.plot( data )
    plt.plot( datafiltered )
    plt.plot( data-datafiltered ) 
    
    
    
    

    
    
    
#Calculate a noised sine wave to get a more realistic wave
def medianSinPlotNoised1024( waveNumber, windowLength ):
    data = np.fromfunction( lambda x: np.sin((x-windowLength / 2)/1024 * 2 * np.pi * waveNumber), (1024 + windowLength / 2, ) ) #creating an array with a sine wave
    noise = np.random.normal(0,0.2,(128 + windowLength / 2))       # creating the noise as an array, filled with random numbers, with the same length as the data array
    signal = data + noise                                          # generate the noised signal
    datafiltered = medianFilter(signal, windowLength)              #calculate the filtered wave with the medianFiltered function
    signal = signal[ windowLength / 2 : - windowLength ]           # slice the data array to synchronize both waves
    datafiltered = datafiltered[ : len(signal) ]                   # cut the filtered wave to the same length as the data wave
    plt.plot( signal )
    plt.plot( datafiltered )
    plt.plot( signal-datafiltered )