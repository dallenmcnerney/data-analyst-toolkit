import numpy as np


# Run mean normalization over data
def mean_normalization(data):
    normalized_data = (data - np.mean(data, axis=0))/(np.max(data, axis=0) - np.min(data, axis=0))
    return normalized_data
