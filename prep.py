import numpy as np
from scipy import ndimage as ndi
from skimage.transform import rescale
import glob
import h5py

data_list = []
for filename in sorted(glob.glob('raw_data/*csv'))[1:]:
    # upscale 10x
    tmp = rescale(np.loadtxt(filename, delimiter=','), 10, mode='reflect')
    data_list.append(tmp)

data = np.array(data_list)

# interpolate time dimension
t = np.linspace(0, 7, 128, endpoint=False).reshape((-1, 1, 1))
row_coord, col_coord = np.indices(data.shape[1:])
indices = np.broadcast_arrays(t, row_coord, col_coord)
full_data = ndi.map_coordinates(data, indices, mode='nearest')

f = h5py.File('weather.hdf5', 'w')
f.create_dataset("temperature", data=full_data)
