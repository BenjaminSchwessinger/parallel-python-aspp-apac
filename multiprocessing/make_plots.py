import h5py
import numpy as np
import matplotlib.pyplot as plt

# load the data from weather.hdf5 here into a
# numpy array temps (temperatures)
temps = None  # edit this
years = None  # edit this


def make_plot(year):
    """Plot average temperature image i with interpolation 'lanczos' and
    save it to the corresponding {year}.png file.

    Hint: there are 8 years in the dataset, with 16 points per year.
    (ie 128 points total). Take the average or an arbitrary point for
    the year.

    Hint: use plt.imshow.
    """
    pass  # edit this


if __name__ == '__main__':
    for i, year in enumerate(years):
        make_plot(i)
