import context # pylint: disable=unused-import

import unittest
import numpy as np

from boilerplate.utils import unique

class TestUnique(unittest.TestCase):

    def test_no_replicate_values(self):
        values =([1.0, 1.0, 2.0, 3.0, 4.0, 4.0])

        np.testing.assert_array_equal(
            np.sort(unique(np.array(values))),
            np.sort(np.array(list(set(values))))
        )

if __name__ == '__main__':
    unittest.main()
