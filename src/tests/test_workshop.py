import unittest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal

from workshop import multiply_by10


class TestWorkshop(unittest.TestCase):
    def test_multiply_by10(self):
        df = pd.DataFrame({"height": [1, 2, 3]})
        expected = pd.DataFrame({"height": [10, 20, 30]})
        assert_frame_equal(expected, multiply_by10(df))