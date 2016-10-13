#include "unique.h"

#include <vector>
#include <algorithm>
#include <iterator>

std::vector<double> uniqueValues(std::vector<double> values) {
    std::vector<double> output;
    std::unique_copy(values.begin(), values.end(), std::back_inserter(output));

    return output;
}
