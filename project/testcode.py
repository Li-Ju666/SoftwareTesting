from pandas import DataFrame
from unittest import TestCase, main
import numpy as np
import pandas as pd

'''
Author: Li Ju
For Course: Software Testing
Date: 01/12/2019

In the script, a bunch of testing cases for method dropna() for both Series and DataFrame in python library Pandas are
conducted. 

'''

class PandasSeriesTest(TestCase):
    def test1_series_float(self):
        ## Case for float-element series
        srs1_1 = pd.Series([1.0, 2.0, 3.0, np.nan, 4.0, np.nan])
        result = srs1_1.dropna()
        expec1_1 = pd.Series([1.0, 2.0, 3.0, 4.0])
        expec1_1.index = [0, 1, 2, 4]
        self.assertTrue(result.equals(expec1_1))
        self.assertFalse(srs1_1.equals(expec1_1))

        ## subcase for inplace dropna
        srs1_1.dropna(inplace = True)
        self.assertTrue(srs1_1.equals(expec1_1))

        ## subcase for series with no NAN values
        srs1_2 = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        expec1_2 = srs1_2.dropna()
        result = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertTrue(result.equals(expec1_2))

    def test2_series_obj(self):
        ## Case for object-element series
        srs2 = pd.Series(['1', '2', '3', None, '4', None])
        result = srs2.dropna()
        expec = pd.Series(['1', '2', '3', '4'])
        expec.index = [0, 1, 2, 4]
        self.assertTrue(result.equals(expec))
        self.assertFalse(srs2.equals(expec))

        ## subcase for inplace dropna
        result = srs2.dropna(inplace = True)
        self.assertTrue(srs2.equals(expec))

    def test3_df_axis(self):
        df1 = pd.DataFrame([[1.0, 2.0, None], [4.0, None, 6.0], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'])
        ## subcase for row_directed NAN removal
        result = df1.dropna(axis = 0)
        expec1_1 = pd.DataFrame([[7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [2])
        self.assertTrue(result.equals(expec1_1))

        ## subcase for column_directed NAN removal
        result = df1.dropna(axis=1)
        expec1_2 = pd.DataFrame([1.0, 4.0, 7.0], columns=['a'], index=[0, 1, 2])
        self.assertTrue(result.equals(expec1_2))

    def test4_df_how(self):
        df2 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'])
        ## subcase for how='any'
        result = df2.dropna(how = 'any')
        expec2_1 = pd.DataFrame([[7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [2])
        self.assertTrue(result.equals(expec2_1))

        ## subcase for how = 'all'
        result = df2.dropna(how = 'all')
        expec2_2 = pd.DataFrame([[1.0, 2.0, None], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [0, 2])
        self.assertTrue(result.equals(expec2_2))

    def test5_df_thresh(self):
        ## Test case when only whose number of NANs is greater than thresh may be removed
        df3 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, None, None]], columns=['a', 'b', 'c'])
        result = df3.dropna(thresh=2)
        expec3 = pd.DataFrame([[1.0, 2.0, None]], columns=['a', 'b', 'c'], index = [0])
        self.assertTrue(result.equals(expec3))

    def test6_df_subset(self):
        ## Test case when choosing a subset of columns when droping NANs
        df4 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, None, None]], columns=['a', 'b', 'c'])
        result = df4.dropna(subset=['a', 'b'])
        expec4 = pd.DataFrame([[1.0, 2.0, None]], columns=['a', 'b', 'c'], index=[0])
        self.assertTrue(result.equals(expec4))

    def test7_df_inplace(self):
        ## subcase for inplace is False (default)
        df5 = pd.DataFrame([[1.0, 2.0, None], [4.0, None, 6.0], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'])
        result = df5.dropna()
        expec5_1 = pd.DataFrame([[7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [2])
        self.assertTrue(result.equals(expec5_1))

        ## subcase for inplace is True
        df5.dropna(inplace = True)
        self.assertTrue(result.equals(df5))


if __name__ == '__main__':
    main()
