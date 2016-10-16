#include "unique.h"

#include <vector>
#include <algorithm>
#include <iterator>

template<typename T>
std::vector<T> uniqueValues(std::vector<T> values) {
    std::vector<T> output;
    std::unique_copy(values.begin(), values.end(), std::back_inserter(output));

    return output;
}

// Explicit instantiation needed to link with Cython
template std::vector<double> uniqueValues(std::vector<double> values);
template std::vector<int64_t> uniqueValues(std::vector<int64_t> values);
