from pandas import DataFrame
from unittest import TestCase, main
import numpy as np
import pandas as pd

class PandasSeriesTest(TestCase):
    def test1_series_dropna(self):
        ## Case for float-element series and inplace=True
        srs1_1 = pd.Series([1.0, 2.0, 3.0, np.nan, 4.0, np.nan])
        srs1_1.dropna(inplace=True)
        expec1_1 = pd.Series([1.0, 2.0, 3.0, 4.0])
        expec1_1.index = [0, 1, 2, 4]
        self.assertTrue(srs1_1.equals(expec1_1))


        ## Case for object-element series and inplace=False
        srs1_2 = pd.Series(['1', '2', '3', None, '4', None])
        srs1_2.describe()
        result = srs1_2.dropna(inplace=False)
        expec1_2 = pd.Series(['1', '2', '3', '4'])
        expec1_2.index = [0, 1, 2, 4]
        self.assertTrue(result.equals(expec1_2))
        self.assertFalse(srs1_2.equals(expec1_2))

    def test2_dataframe_dropna(self):
        df = pd.DataFrame([[None, 2.0, 3.0, 4.0], [None, 6.0, 7.0, 8.0], [None, None, 11.0, 12.0],
                            [None, None, None, None]], columns=['a', 'b', 'c', 'd'])
        ## case for axis=0, thresh=1, inplace=False, subset=['b', 'd'], how='any'
        result = df.dropna(axis = 0, thresh=1, inplace=False, subset=['b', 'd'], how='any')
        expec2_1 = pd.DataFrame([[None, 2.0, 3.0, 4.0], [None, 6.0, 7.0, 8.0],
                                 [None, None, 11.0, 12.0]], columns=['a', 'b', 'c', 'd'], index = [0, 1, 2])
        self.assertTrue(result.equals(expec2_1))
        self.assertFalse(df.equals(expec2_1))

        ## case for axis=1, thresh=None, inplace=True, subset=None, how='all'
        df.dropna(axis=1, inplace=True, how='all')
        expec2_2 = pd.DataFrame([[2.0, 3.0, 4.0], [6.0, 7.0, 8.0],
                      [None, 11.0, 12.0], [None, None, None]],
                     columns=['b', 'c', 'd'], index=[0, 1, 2, 3])
        self.assertTrue(df.equals(expec2_2))


if __name__ == '__main__':
    main()
