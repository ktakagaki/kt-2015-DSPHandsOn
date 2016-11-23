# -*- coding: utf-8 -*-
"""
Common functions for analysis of median filter characteristics
Created on Thu Oct 15 10:07:55 2015

@author: Dominik
"""
import numpy as _np
import matplotlib.pylab as _plt
import scipy.signal as _sps
from decimal import Decimal as _Decimal


def _medianFilter(data, windowLength):
    """Calculate the the median filtered wave with defined window length."""
    if windowLength < len(data) and data.ndim == 1:
        # Creating an array where the filtered values will be saved in.
        tempret = _np.zeros(len(data))
        # Check if the window length is odd or even because with
        # even window length we get an unsynchrone filtered wave.
        if windowLength % 2 == 1:
            tempret = _sps.medfilt(data, windowLength)
            return tempret
        else:
            raise ValueError('Window length  should be odd')

    else:
        raise ValueError('windowLength must be smaller ' +
                         'than len(data) and data must be a 1D array')


def _medianFilterPlotterImpl(data, windowLength, waveNumber, samples,
                             plotStart, plotEnd):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)
    data = data[plotStart: plotEnd]
    datafiltered = datafiltered[plotStart: plotEnd]
    ax = _plt.subplot()
    xticks = _np.arange(0, len(data)+1, samples/waveNumber)
    ax.set_xticks(xticks)
    x_label = [r"${%s\pi}$" % (2*w) for w in range(0, len(xticks))]
    ax.set_xticklabels(x_label)
    _plt.axis([0, len(data), -1.5, 1.5])
    _plt.plot(data, color = 'cornflowerblue', lw = 1.0)
    _plt.plot(data - datafiltered, color = 'r', lw = 1.5)
    _plt.plot(datafiltered, color = 'g', lw = 1.0)
    

def medianSinPlot(waveNumber, windowLength, samples=128,
                  plotStart=0, plotEnd=-1):
    """ Plot a sine wave, the  medain filtered and the difference between
    sine and median filtered wave.
    """
    time = _np.linspace(0, 2, samples)
    # Creating an array with sine waves.
    data = _np.sin(_np.pi*time*waveNumber)
    _medianFilterPlotterImpl(data, windowLength, waveNumber, samples, plotStart, plotEnd)


def medianSinPlotNoised(waveNumber, windowLength, samples=128,
                        plotStart=0, plotEnd=-1):
    """ Plot a noised sine wave, the  medain filtered and the difference
    between sine and median filtered wave.
    """
    time = _np.linspace(0, 2, samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise = _np.random.normal(0, 0.7069341/_np.sqrt(2), len(data))
    data = data + noise
    _medianFilterPlotterImpl(data, windowLength, waveNumber, samples,
                             plotStart, plotEnd)


def _ErrorRateWindow(data, datafiltered, windowLength):
    """Calculate the error rate of the filtered wave
    with different windowLength and defined wave number.
    """
    # Calculate the difference between the sine wave and the filtered wave.
    errorrate = data-datafiltered
    error = []
    errorrate = _np.abs(errorrate)
    # Fill the list with the errorrate and corresponding wave number.
    error.append([windowLength, _np.mean(errorrate)])
    # Zip the error ([1,1],[2,2],[3,3]) = ([1,2,3],[1,2,3]).
    error = zip(*error)
    return error


def _windowErrorPlotterImpl(data, windowLength, waveNumber, samples):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)
    error = _ErrorRateWindow(data, datafiltered, windowLength)
    error = _np.asarray(error)
    error[1:] = error[1:]/0.63662
    ax = _plt.subplot()
    _plt.axis([0, windowLength+1, 0, 1.5])
    xticks = _np.arange(0, windowLength + 1, samples/waveNumber)
    ax.set_xticks(xticks)
    x_label = [r"${%s\pi}$" % (2*w) for w in range(0, len(xticks))]
    ax.set_xticklabels(x_label)
    _plt.scatter(*error, c='red', lw=0)
    _plt.hlines(1, 0, windowLength, color='b', linestyle='--')


def ErrorPlotWindow(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number
    """
    time = _np.linspace(0, 2, samples)
    data = _np.sin(_np.pi*time*waveNumber)
    _windowErrorPlotterImpl(data, windowLength, waveNumber, samples)


def ErrorPlotWindowNoised(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different window lengths and fixed wave number,
    sine wave is noised
    """
    time = _np.linspace(0, 2, samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise = _np.random.normal(0, 0.4, len(data))
    data = data + noise
    _windowErrorPlotterImpl(data, windowLength, waveNumber, samples)


def _ErrorRateWave(data, datafiltered, waveNumber):
    """Calculate the error rate of the filtered wave
    with different wave number and defined window length
    """
    errorrate = data - datafiltered
    error = []
    errorrate = _np.abs(errorrate)
    error.append([waveNumber, _np.mean(errorrate)])
    error = zip(*error)
    return error


def _waveErrorPlotterImpl(data, waveNumber, windowLength):
    # Calculate the filtered wave with the medianFiltered function.
    datafiltered = _medianFilter(data, windowLength)
    # Calculate the error with the ErrorRate function.
    error = _ErrorRateWave(data, datafiltered, waveNumber)
    _plt.axis([0, waveNumber + 1, 0, 1.2])
    _plt.xlabel('Wave number', fontsize=13)
    _plt.ylabel('resolution', fontsize=13)
    _plt.scatter(*error)


def ErrorPlotWave(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length
    """
    time = _np.linspace(0, 2, samples)
    data = _np.sin(_np.pi*time*waveNumber)
    _waveErrorPlotterImpl(data, waveNumber, windowLength)


def ErrorplotWaveNoised(waveNumber, windowLength, samples=128):
    """ Plot the Errror(mean of the absolute from sine wave - filtered wave)
    of the median filter, with different wave number and fixed window length,
    sine wave is noised
    """
    time = _np.linspace(0, 2, samples)
    data = _np.sin(_np.pi*time*waveNumber)
    noise = _np.random.normal(0, 0.2, len(data))
    data = data + noise
    _waveErrorPlotterImpl(data, waveNumber, windowLength)


class similarity:

    def euclideanDistance(self, x, y):

        if len(x) != len(y):
            raise ValueError("all the input array dimensions must match exactly")
        # Number rounded to 3 digits from the decimal point.
        dist = round(_np.sqrt(sum(_np.power(a - b, 2) for a, b in zip(x, y))), 3)
        return dist

    def manhattanDistance(self, x, y):

        if len(x) != len(y):
            raise ValueError("all the input array dimensions must match exactly")
        dist = round(sum(abs(a - b) for a, b in zip(x, y)), 3)
        return dist

    def cosineSimilarity(self, x, y):

        def _square_rooted( x):
            temp = round(_np.sqrt(sum(a * a for a in x)), 3)
            return temp

        if len(x) != len(y):
            raise ValueError("all the input array dimensions must match exactly")
        num = sum(a * b for a, b in zip(x, y))
        denom = _square_rooted(self, x) * _square_rooted(y)
        sim = round(num / float(denom), 3)

        return sim

    def jaccardSimilarity(self, x, y):

        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        sim = intersection_cardinality / float(union_cardinality)
        return sim

    def minkowskiDistance(self, x, y, p_val):

        def _nth_root(value, n_root):
            root_value = 1 / float(n_root)
            temp = round(_Decimal(value) ** _Decimal(root_value), 3)
            return temp

        if len(x) != len((y)):
            raise ValueError("all the input array dimensions must match exactly")
        dist = _nth_root(sum(_np.power(abs(a - b), p_val) for a, b in zip(x, y)), p_val)
        return dist
