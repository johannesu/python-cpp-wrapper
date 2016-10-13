from libcpp.vector cimport vector

cdef extern from "include/unique.h":
    vector[double] uniqueValues(vector[double] values);