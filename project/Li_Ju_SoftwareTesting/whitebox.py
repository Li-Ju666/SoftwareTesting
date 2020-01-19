from unittest import TestCase, main
import pandas as pd
import math
'''
Author: Li Ju
For Course: Software Testing
Date: 17/01/2020

In the script, a bunch of white box testing cases for function describe() in python library Pandas are conducted. Function
describe() aims to generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's 
distribution, excluding NaN values. It can analyze both numeric and object series, as well as DataFrame column sets of 
mixed data types. The output will vary depending on what is provided. 

Parameters
    ----------
    percentiles : list-like of numbers, optional
        The percentiles to include in the output. All should
        fall between 0 and 1. The default is
        ``[.25, .5, .75]``, which returns the 25th, 50th, and
        75th percentiles.
    include : 'all', list-like of dtypes or None (default), optional
        A white list of data types to include in the result. Ignored
        for ``Series``. Here are the options:

        - 'all' : All columns of the input will be included in the output.
        - A list-like of dtypes : Limits the results to the
          provided data types.
          To limit the result to numeric types submit
          ``numpy.number``. To limit it instead to object columns submit
          the ``numpy.object`` data type. Strings
          can also be used in the style of
          ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
          select pandas categorical columns, use ``'category'``
        - None (default) : The result will include all numeric columns.
    exclude : list-like of dtypes or None (default), optional,
        A black list of data types to omit from the result. Ignored
        for ``Series``. Here are the options:

        - A list-like of dtypes : Excludes the provided data types
          from the result. To exclude numeric types submit
          ``numpy.number``. To exclude object columns submit the data
          type ``numpy.object``. Strings can also be used in the style of
          ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
          exclude pandas categorical columns, use ``'category'``
        - None (default) : The result will exclude nothing.

To design white box testing, firstly a control flow graph is drawn as control graph.png attached. 

Then, for the Test Requirement, we apply edge coverage. Here are our as-designed test paths: 
test paths: 
[(1, 2), (1, 3, 4, 5, 6, 7, 9, 10), (1, 3, 4, 5, 7, 9, 10), (1, 3, 8, 9, 11, 12), (1, 3, 8, 9, 11, 13, 18, 19, 20), 
(1, 3, 8, 9, 11, 13, 19, 20), (1, 3, 8, 9, 11, 14, 15), (1, 3, 8, 9, 11, 14, 17, 20), (1, 3, 8, 9, 11, 16, 20)]

With as-designed test paths, we constructed following testing cases. 
'''
class PandasSeriesTest(TestCase):
    def test1(self):
        ## Case for path (1, 2)
        data = pd.DataFrame([], [])
        self.assertRaises(ValueError, data.describe)

    def test2(self):
        ## case for path (1, 3, 4, 5, 6, 7, 9, 10)
        data = pd.Series([1, 2, 3, 4, 5])
        self.assertRaises(ValueError, data.describe, percentiles=[0, 0.1, 0.8, 0.8])

    def test3(self):
        ## case for path (1, 3, 4, 5, 7, 9, 10)
        data = pd.Series([1, 2, 3, 4, 5])
        self.assertRaises(ValueError, data.describe, percentiles=[0, 0.1, 0.5, 0.8, 0.8])

    def test4(self):
        ## case for path (1, 3, 8, 9, 11, 12)
        data = pd.Series([0, 2.5, 5, 7.5, 10])
        result = data.describe()
        self.assertTrue(result[0] == pd.Series.count(data))
        self.assertTrue(result[1] == pd.Series.mean(data))
        self.assertTrue(result[2] == pd.Series.std(data))
        self.assertTrue(result[3] == 0)
        self.assertTrue(result[4] == 2.5)
        self.assertTrue(result[5] == 5)
        self.assertTrue(result[6] == 7.5)
        self.assertTrue(result[7] == 10)

    def test5(self):
        ## case for path (1, 3, 8, 9, 11, 13, 18, 19, 20)
        data = pd.DataFrame([['a', 'b',], ['a', 'b']])
        result = data.describe()
        self.assertTrue(result[0][0] == 2)
        self.assertTrue(result[0][1] == 1)
        self.assertTrue(result[0][2] == 'a')
        self.assertTrue(result[0][3] == 2)
        self.assertTrue(result[1][0] == 2)
        self.assertTrue(result[1][1] == 1)
        self.assertTrue(result[1][2] == 'b')
        self.assertTrue(result[1][3] == 2)

    def test6(self):
        ## case for path (1, 3, 8, 9, 11, 13, 19, 20)
        data = pd.DataFrame([['a', 0], ['b', 2.5], ['c', 5], ['d', 7.5], ['e', 10]])
        result = data.describe()
        self.assertTrue(result[1][0] == 5)
        self.assertTrue(result[1][1] == 5)
        self.assertTrue(result[1][2] == pd.Series.std(data[1]))
        self.assertTrue(result[1][3] == 0)
        self.assertTrue(result[1][4] == 2.5)
        self.assertTrue(result[1][5] == 5)
        self.assertTrue(result[1][6] == 7.5)
        self.assertTrue(result[1][7] == 10)

    def test7(self):
        ## case for path (1, 3, 8, 9, 11, 14, 15)
        data = pd.DataFrame({
            'letter': ['a', 'b', 'c'],
            'number': [1, 2, 3]})
        self.assertRaises(ValueError, data.describe, include='all', exclude='letter')

    def test8(self):
        ## case for path (1, 3, 8, 9, 11, 14, 17, 20)
        data = pd.DataFrame({
            'letter': ['a', 'a', 'c'],
            'number': [1, 2, 3]})
        result = data.describe(include='all')
        self.assertTrue(result['letter'][0] == 3)
        self.assertTrue(result['letter'][1] == 2)
        self.assertTrue(result['letter'][2] == 'a')
        self.assertTrue(result['letter'][3] == 2)
        self.assertTrue(math.isnan(result['letter'][4]))
        self.assertTrue(math.isnan(result['letter'][5]))
        self.assertTrue(math.isnan(result['letter'][6]))
        self.assertTrue(math.isnan(result['letter'][7]))
        self.assertTrue(math.isnan(result['letter'][8]))
        self.assertTrue(math.isnan(result['letter'][9]))
        self.assertTrue(math.isnan(result['letter'][10]))
        self.assertTrue(result['number'][0] == 3)
        self.assertTrue(math.isnan(result['number'][1]))
        self.assertTrue(math.isnan(result['number'][2]))
        self.assertTrue(math.isnan(result['number'][3]))
        self.assertTrue(result['number'][4] == 2)
        self.assertTrue(result['number'][5] == 1)
        self.assertTrue(result['number'][6] == 1)
        self.assertTrue(result['number'][7] == 1.5)
        self.assertTrue(result['number'][8] == 2)
        self.assertTrue(result['number'][9] == 2.5)
        self.assertTrue(result['number'][10] == 3)

    def test9(self):
        ## case for path (1, 3, 8, 9, 11, 16, 20)
        data = pd.DataFrame({
            'letter': ['a', 'a', 'c'],
            'number': [1, 2, 3]})
        result = data.describe(exclude='number')
        print(result)
        self.assertTrue(result['letter'][0] == 3)
        self.assertTrue(result['letter'][1] == 2)
        self.assertTrue(result['letter'][2] == 'a')
        self.assertTrue(result['letter'][3] == 2)

if __name__ == '__main__':
    main()

'''
The pandas function describe() have passed all the testing cases above, indicating that there are no
bugs existing in the source code.  
'''