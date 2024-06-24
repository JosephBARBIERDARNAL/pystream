import numpy as np
import matplotlib.pyplot as plt
from .smoothing import smooth_data

def streamgraph(data, labels=None, colors=None, title="Streamgraph", xlabel="X-axis", ylabel="Y-axis", smoothing_method=None, window_size=5):
   """
   Create a streamgraph using matplotlib.
   
   Args:
   - data (list of lists): 2D list containing data for each stream.
   - labels (list): labels for each stream.
   - colors (list): colors for each stream.
   - title (str): title of the graph.
   - xlabel (str): label for the x-axis.
   - ylabel (str): label for the y-axis.
   - smoothing_method (str): method for smoothing data ('interpolation', 'moving_average', etc.)
   - window_size (int): window size for smoothing (applicable for moving average)
   
   Returns:
   - Matplotlib figure and axes of the streamgraph.
   """
   if smoothing_method:
      data = [smooth_data(stream, method=smoothing_method, window_size=window_size) for stream in data]
   
   fig, ax = plt.subplots(figsize=(10, 6))
   x = np.arange(len(data[0]))
   y = np.array(data)
   
   if colors is None:
      colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
   
   ax.stackplot(x, y, labels=labels, colors=colors)
   ax.set_title(title)
   ax.set_xlabel(xlabel)
   ax.set_ylabel(ylabel)
   ax.legend(loc='upper right')
   
   return fig, ax
