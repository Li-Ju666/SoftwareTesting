from pandas import DataFrame
from unittest import TestCase, main
import numpy as np
import pandas as pd

'''
Author: Li Ju
For Course: Software Testing
Date: 01/12/2019

In the script, a bunch of black box testing cases for method dropna() for both Series and DataFrame in python library Pandas are
conducted.

To make proper black box testing, input domain modelling is used. 

Firstly, the parameters of the input are specified. The parameters for method series.dropna() include [self, inplace(default False), 
**kwargs], while parameters for method data.frame.dropna() include [self, axis(default 0), how(default "any"),
thresh(default None), subset(default None), inplace(default False)]. 

Then To model the input domain, we use interface-based approach, developing characteristics of parameters directly from
individual parameters. 
1. for dropna method of series, input value could be objects or numbers, inplace could be false and true, **kwargs
are useless for the methods. 
2. for dropna method of data.frame, axis could also be divided as 0 and non-zero values, how could be binary "any" and "all", 
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

    #
    # def test4_df_how(self):
    #     df2 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'])
    #     ## subcase for how='any'
    #     result = df2.dropna(how = 'any')
    #     expec2_1 = pd.DataFrame([[7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [2])
    #     self.assertTrue(result.equals(expec2_1))
    #
    #     ## subcase for how = 'all'
    #     result = df2.dropna(how = 'all')
    #     expec2_2 = pd.DataFrame([[1.0, 2.0, None], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [0, 2])
    #     self.assertTrue(result.equals(expec2_2))
    #
    # def test5_df_thresh(self):
    #     ## Test case when only whose number of NANs is greater than thresh may be removed
    #     df3 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, None, None]], columns=['a', 'b', 'c'])
    #     result = df3.dropna(thresh=0)
    #     result1 = df3.dropna(thresh=2)
    #     expec3 = pd.DataFrame([[1.0, 2.0, None]], columns=['a', 'b', 'c'], index = [0])
    #     self.assertTrue(result.equals(expec3))
    #
    # def test6_df_subset(self):
    #     ## Test case when choosing a subset of columns when droping NANs
    #     df4 = pd.DataFrame([[1.0, 2.0, None], [None, None, None], [7.0, None, None]], columns=['a', 'b', 'c'])
    #     result = df4.dropna(subset=['a', 'b'])
    #     expec4 = pd.DataFrame([[1.0, 2.0, None]], columns=['a', 'b', 'c'], index=[0])
    #     self.assertTrue(result.equals(expec4))
    #
    # def test7_df_inplace(self):
    #     ## subcase for inplace is False (default)
    #     df5 = pd.DataFrame([[1.0, 2.0, None], [4.0, None, 6.0], [7.0, 8.0, 9.0]], columns=['a', 'b', 'c'])
    #     result = df5.dropna()
    #     expec5_1 = pd.DataFrame([[7.0, 8.0, 9.0]], columns=['a', 'b', 'c'], index = [2])
    #     self.assertTrue(result.equals(expec5_1))
    #
    #     ## subcase for inplace is True
    #     df5.dropna(inplace = True)
    #     self.assertTrue(result.equals(df5))
    #

if __name__ == '__main__':
    main()

#
# def describe(self, percentiles=None, include=None, exclude=None):
#     """
#     Generate descriptive statistics that summarize the central tendency,
#     dispersion and shape of a dataset's distribution, excluding
#     ``NaN`` values.
#
#     Analyzes both numeric and object series, as well
#     as ``DataFrame`` column sets of mixed data types. The output
#     will vary depending on what is provided. Refer to the notes
#     below for more detail.
#
#     Parameters
#     ----------
#     percentiles : list-like of numbers, optional
#         The percentiles to include in the output. All should
#         fall between 0 and 1. The default is
#         ``[.25, .5, .75]``, which returns the 25th, 50th, and
#         75th percentiles.
#     include : 'all', list-like of dtypes or None (default), optional
#         A white list of data types to include in the result. Ignored
#         for ``Series``. Here are the options:
#
#         - 'all' : All columns of the input will be included in the output.
#         - A list-like of dtypes : Limits the results to the
#           provided data types.
#           To limit the result to numeric types submit
#           ``numpy.number``. To limit it instead to object columns submit
#           the ``numpy.object`` data type. Strings
#           can also be used in the style of
#           ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
#           select pandas categorical columns, use ``'category'``
#         - None (default) : The result will include all numeric columns.
#     exclude : list-like of dtypes or None (default), optional,
#         A black list of data types to omit from the result. Ignored
#         for ``Series``. Here are the options:
#
#         - A list-like of dtypes : Excludes the provided data types
#           from the result. To exclude numeric types submit
#           ``numpy.number``. To exclude object columns submit the data
#           type ``numpy.object``. Strings can also be used in the style of
#           ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
#           exclude pandas categorical columns, use ``'category'``
#         - None (default) : The result will exclude nothing.
#
#     Returns
#     -------
#     Series or DataFrame
#         Summary statistics of the Series or Dataframe provided.
#
#     See Also
#     --------
#     DataFrame.count: Count number of non-NA/null observations.
#     DataFrame.max: Maximum of the values in the object.
#     DataFrame.min: Minimum of the values in the object.
#     DataFrame.mean: Mean of the values.
#     DataFrame.std: Standard deviation of the observations.
#     DataFrame.select_dtypes: Subset of a DataFrame including/excluding
#         columns based on their dtype.
#
#     Notes
#     -----
#     For numeric data, the result's index will include ``count``,
#     ``mean``, ``std``, ``min``, ``max`` as well as lower, ``50`` and
#     upper percentiles. By default the lower percentile is ``25`` and the
#     upper percentile is ``75``. The ``50`` percentile is the
#     same as the median.
#
#     For object data (e.g. strings or timestamps), the result's index
#     will include ``count``, ``unique``, ``top``, and ``freq``. The ``top``
#     is the most common value. The ``freq`` is the most common value's
#     frequency. Timestamps also include the ``first`` and ``last`` items.
#
#     If multiple object values have the highest count, then the
#     ``count`` and ``top`` results will be arbitrarily chosen from
#     among those with the highest count.
#
#     For mixed data types provided via a ``DataFrame``, the default is to
#     return only an analysis of numeric columns. If the dataframe consists
#     only of object and categorical data without any numeric columns, the
#     default is to return an analysis of both the object and categorical
#     columns. If ``include='all'`` is provided as an option, the result
#     will include a union of attributes of each type.
#
#     The `include` and `exclude` parameters can be used to limit
#     which columns in a ``DataFrame`` are analyzed for the output.
#     The parameters are ignored when analyzing a ``Series``.
#
#     Examples
#     --------
#     Describing a numeric ``Series``.
#
#     >>> s = pd.Series([1, 2, 3])
#     >>> s.describe()
#     count    3.0
#     mean     2.0
#     std      1.0
#     min      1.0
#     25%      1.5
#     50%      2.0
#     75%      2.5
#     max      3.0
#     dtype: float64
#
#     Describing a categorical ``Series``.
#
#     >>> s = pd.Series(['a', 'a', 'b', 'c'])
#     >>> s.describe()
#     count     4
#     unique    3
#     top       a
#     freq      2
#     dtype: object
#
#     Describing a timestamp ``Series``.
#
#     >>> s = pd.Series([
#     ...   np.datetime64("2000-01-01"),
#     ...   np.datetime64("2010-01-01"),
#     ...   np.datetime64("2010-01-01")
#     ... ])
#     >>> s.describe()
#     count                       3
#     unique                      2
#     top       2010-01-01 00:00:00
#     freq                        2
#     first     2000-01-01 00:00:00
#     last      2010-01-01 00:00:00
#     dtype: object
#
#     Describing a ``DataFrame``. By default only numeric fields
#     are returned.
#
#     >>> df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
#     ...                    'numeric': [1, 2, 3],
#     ...                    'object': ['a', 'b', 'c']
#     ...                   })
#     >>> df.describe()
#            numeric
#     count      3.0
#     mean       2.0
#     std        1.0
#     min        1.0
#     25%        1.5
#     50%        2.0
#     75%        2.5
#     max        3.0
#
#     Describing all columns of a ``DataFrame`` regardless of data type.
#
#     >>> df.describe(include='all')
#             categorical  numeric object
#     count            3      3.0      3
#     unique           3      NaN      3
#     top              f      NaN      c
#     freq             1      NaN      1
#     mean           NaN      2.0    NaN
#     std            NaN      1.0    NaN
#     min            NaN      1.0    NaN
#     25%            NaN      1.5    NaN
#     50%            NaN      2.0    NaN
#     75%            NaN      2.5    NaN
#     max            NaN      3.0    NaN
#
#     Describing a column from a ``DataFrame`` by accessing it as
#     an attribute.
#
#     >>> df.numeric.describe()
#     count    3.0
#     mean     2.0
#     std      1.0
#     min      1.0
#     25%      1.5
#     50%      2.0
#     75%      2.5
#     max      3.0
#     Name: numeric, dtype: float64
#
#     Including only numeric columns in a ``DataFrame`` description.
#
#     >>> df.describe(include=[np.number])
#            numeric
#     count      3.0
#     mean       2.0
#     std        1.0
#     min        1.0
#     25%        1.5
#     50%        2.0
#     75%        2.5
#     max        3.0
#
#     Including only string columns in a ``DataFrame`` description.
#
#     >>> df.describe(include=[np.object])
#            object
#     count       3
#     unique      3
#     top         c
#     freq        1
#
#     Including only categorical columns from a ``DataFrame`` description.
#
#     >>> df.describe(include=['category'])
#            categorical
#     count            3
#     unique           3
#     top              f
#     freq             1
#
#     Excluding numeric columns from a ``DataFrame`` description.
#
#     >>> df.describe(exclude=[np.number])
#            categorical object
#     count            3      3
#     unique           3      3
#     top              f      c
#     freq             1      1
#
#     Excluding object columns from a ``DataFrame`` description.
#
#     >>> df.describe(exclude=[np.object])
#            categorical  numeric
#     count            3      3.0
#     unique           3      NaN
#     top              f      NaN
#     freq             1      NaN
#     mean           NaN      2.0
#     std            NaN      1.0
#     min            NaN      1.0
#     25%            NaN      1.5
#     50%            NaN      2.0
#     75%            NaN      2.5
#     max            NaN      3.0
#
#     describe(self, percentiles=None, include=None, exclude=None)
#
#     """
#     if self.ndim == 2 and self.columns.size == 0:
#         raise ValueError("Cannot describe a DataFrame without columns")
#
#     if percentiles is not None:
#         # explicit conversion of `percentiles` to list
#         percentiles = list(percentiles)
#
#         # get them all to be in [0, 1]
#         self._check_percentile(percentiles)
#
#         # median should always be included
#         if 0.5 not in percentiles:
#             percentiles.append(0.5)
#         percentiles = np.asarray(percentiles)
#     else:
#         percentiles = np.array([0.25, 0.5, 0.75])
#
#     # sort and check for duplicates
#     unique_pcts = np.unique(percentiles)
#     if len(unique_pcts) < len(percentiles):
#         raise ValueError("percentiles cannot contain duplicates")
#     percentiles = unique_pcts
#
#     formatted_percentiles = format_percentiles(percentiles)
#
#     def describe_numeric_1d(series):
#         stat_index = (
#             ["count", "mean", "std", "min"] + formatted_percentiles + ["max"]
#         )
#         d = (
#             [series.count(), series.mean(), series.std(), series.min()]
#             + series.quantile(percentiles).tolist()
#             + [series.max()]
#         )
#         return pd.Series(d, index=stat_index, name=series.name)
#
#     def describe_categorical_1d(data):
#         names = ["count", "unique"]
#         objcounts = data.value_counts()
#         count_unique = len(objcounts[objcounts != 0])
#         result = [data.count(), count_unique]
#         dtype = None
#         if result[1] > 0:
#             top, freq = objcounts.index[0], objcounts.iloc[0]
#
#             if is_datetime64_any_dtype(data):
#                 tz = data.dt.tz
#                 asint = data.dropna().values.view("i8")
#                 top = Timestamp(top)
#                 if top.tzinfo is not None and tz is not None:
#                     # Don't tz_localize(None) if key is already tz-aware
#                     top = top.tz_convert(tz)
#                 else:
#                     top = top.tz_localize(tz)
#                 names += ["top", "freq", "first", "last"]
#                 result += [
#                     top,
#                     freq,
#                     Timestamp(asint.min(), tz=tz),
#                     Timestamp(asint.max(), tz=tz),
#                 ]
#             else:
#                 names += ["top", "freq"]
#                 result += [top, freq]
#
#         # If the DataFrame is empty, set 'top' and 'freq' to None
#         # to maintain output shape consistency
#         else:
#             names += ["top", "freq"]
#             result += [np.nan, np.nan]
#             dtype = "object"
#
#         return pd.Series(result, index=names, name=data.name, dtype=dtype)
#
#     def describe_1d(data):
#         if is_bool_dtype(data):
#             return describe_categorical_1d(data)
#         elif is_numeric_dtype(data):
#             return describe_numeric_1d(data)
#         elif is_timedelta64_dtype(data):
#             return describe_numeric_1d(data)
#         else:
#             return describe_categorical_1d(data)
#
#     if self.ndim == 1:
#         return describe_1d(self)
#     elif (include is None) and (exclude is None):
#         # when some numerics are found, keep only numerics
#         data = self.select_dtypes(include=[np.number])
#         if len(data.columns) == 0:
#             data = self
#     elif include == "all":
#         if exclude is not None:
#             msg = "exclude must be None when include is 'all'"
#             raise ValueError(msg)
#         data = self
#     else:
#         data = self.select_dtypes(include=include, exclude=exclude)
#
#     ldesc = [describe_1d(s) for _, s in data.items()]
#     # set a convenient order for rows
#     names = []
#     ldesc_indexes = sorted((x.index for x in ldesc), key=len)
#     for idxnames in ldesc_indexes:
#         for name in idxnames:
#             if name not in names:
#                 names.append(name)
#
#     d = pd.concat([x.reindex(names, copy=False) for x in ldesc], axis=1, sort=False)
#     d.columns = data.columns.copy()
#     return d
