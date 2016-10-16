import context # pylint: disable=unused-import

import unittest
import numpy as np

from boilerplate.utils import unique

class TestUnique(unittest.TestCase):

    def test_no_replicate_values_doubles(self):
        values = np.array([1.0, 1.5, 1.5, 3.0, 4.0, 4.0])
        self.__test_array(values)

    def test_no_replicate_values_longs(self):
       values = np.array([1, 1, 2, 2])
       self.__test_array(values)

    def __test_array(self, values):
        np.testing.assert_array_equal(
            np.sort(unique(values)),
            np.sort(np.array(list(set(values))))
        )

if __name__ == '__main__':
    unittest.main()
