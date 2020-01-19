from unittest import TestCase, main
import pandas as pd
import math

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