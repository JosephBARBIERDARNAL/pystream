import numpy as np
from scipy.interpolate import interp1d

def moving_average(data, window_size=5):
    """
    Smooth data using moving average.
    
    Args:
    - data (list or np.array): 1D list or array of data points.
    - window_size (int): window size for moving average.
    
    Returns:
    - np.array: Smoothed data.
    """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def interpolate(data):
    """
    Smooth data using interpolation.
    
    Args:
    - data (list or np.array): 1D list or array of data points.
    
    Returns:
    - np.array: Smoothed data.
    """
    x = np.arange(len(data))
    f = interp1d(x, data, kind='cubic')
    x_new = np.linspace(0, len(data) - 1, num=len(data) * 10)
    return f(x_new)

def smooth_data(data, method='moving_average', window_size=5):
    """
    Apply smoothing to data using the specified method.
    
    Args:
    - data (list or np.array): 1D list or array of data points.
    - method (str): Smoothing method ('moving_average', 'interpolation').
    - window_size (int): window size for moving average (if applicable).
    
    Returns:
    - np.array: Smoothed data.
    """
    if method == 'moving_average':
        return moving_average(data, window_size)
    elif method == 'interpolation':
        return interpolate(data)
    else:
        raise ValueError("Unknown smoothing method: {}".format(method))
