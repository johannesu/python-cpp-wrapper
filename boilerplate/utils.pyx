# cython: boundscheck=False, wraparound=False
# distutils: language = c++
# distutils: sources = boilerplate/src/unique.cpp
# distutils: include_dirs = boilerplate/include
# distutils: extra_compile_args=['-std=c++11']

import numpy as np
cimport numpy as np
from libcpp.vector cimport vector

ctypedef fused supported_types:
    np.float64_t
    np.int64_t

cdef extern from "include/unique.h":
    vector[T] uniqueValues[T](vector[T] values);

def unique(np.ndarray[supported_types] values):
    """ Return unique values in a np.ndarray

    Arguments:
        values:
            type: np.ndarray
            dtype: np.float64_t or np.integer64_t

    Returns:
        unique_values:
            type: np.ndarray
            dtype: same as input
    """

    if supported_types is np.float64_t:
        return uniqueValues[np.float64_t](values)
    elif supported_types is np.int64_t:
        return uniqueValues[np.int64_t](values)
