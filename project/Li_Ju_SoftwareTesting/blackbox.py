from pandas import DataFrame
from unittest import TestCase, main
import numpy as np
import pandas as pd

'''
Author: Li Ju
For Course: Software Testing
Date: 01/12/2019

In the script, a bunch of black box testing cases for method dropna() for both Series and DataFrame in python library Pandas are
conducted. The method dropna() aims to remove null values from series or data frame. 

To make proper black box testing, input domain modelling is used. 

Firstly, the parameters of the input are specified. The parameters for method series.dropna() include [self, inplace(default False), 
**kwargs].

 
 while parameters for method data.frame.dropna() include [self, axis(default 0), how(default "any"),
thresh(default None), subset(default None), inplace(default False)]. 

Then To model the input domain, we use interface-based approach, developing characteristics of parameters directly from
individual parameters. 
1. for dropna method of series, input value could be objects or numbers. Besides itself, it has one parameter, inplace, 
which is a boolean value, indicating where the operation is done inplace or return a copy. 

2. for dropna method of data.frame, it has 5 parameters. Their value domain and explanation are shown below: 
        
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Determine if rows or columns which contain missing values are
            removed.

            * 0, or 'index' : Drop rows which contain missing values.
            * 1, or 'columns' : Drop columns which contain missing value.

            .. deprecated:: 0.23.0

               Pass tuple or list to drop on multiple axes.
               Only a single axis is allowed.

        how : {'any', 'all'}, default 'any'
            Determine if row or column is removed from DataFrame, when we have
            at least one NA or all NA.

            * 'any' : If any NA values are present, drop that row or column.
            * 'all' : If all values are NA, drop that row or column.

        thresh : int, optional
            Require that many non-NA values.
        subset : array-like, optional
            Labels along other axis to consider, e.g. if you are dropping rows
            these would be a list of columns to include.
        inplace : bool, default False
            If True, do operation inplace and return None.

Here is our testing situation, axis could be divided as 0 and non-zero values, how could be binary "any" and "all", 
thresh could be default None and other numbers, inplace could be true and false, and subset could be default None and other
possible subsets. 

After binary parameters have been binary divided, we need to combine these possible values to get several disjoint partitions. 
Here we use EACH CHOICE approach, which required that each value from each block must be chosen at least once. The as-designed
testing cases are shown as following. 
'''

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

'''
The pandas methods dropna() for both series and data frame objects have passed all the testing cases above, 
indicating that there are no bugs existing in the source code.  
'''