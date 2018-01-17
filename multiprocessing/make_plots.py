import h5py
import numpy as np
import matplotlib.pyplot as plt

def make_plot(i):
    """Plot temperature image i with interpolation 'lanczos' and
    save it to the corresponding {year}.png file.

    Hint: use plt.imshow.
    """
    pass  # edit this


if __name__ == '__main__':
    # load the data from weather.hdf5 here into a
    # numpy array temps (temperatures)
    temps = None  # edit this
    years = None  # edit this
    for i, year in enumerate(years):
        make_plot(i)
