# cython: boundscheck=False, wraparound=False
# distutils: language = c++
# distutils: sources = boilerplate/src/unique.cpp
# distutils: include_dirs = boilerplate/include
# distutils: extra_compile_args=['-std=c++11']

import cython
import numpy as np
cimport numpy as np

def unique(np.ndarray[double] values):
    """ Return unique values in a np.ndarray

    Arguments:
        values:
            type: np.ndarray, dtype=np.float64

    Returns:
        unique_values:
            type: np.ndarray, dtype=np.float64
    """

    return uniqueValues(values)
