class DataFrame:
    def aggregate(self, func: Union[Callable, _str], axis: AxisType = ..., **kwargs) -> Series[Dtype]:
        """Aggregate using one or more operations over the specified axis.

.. versionadded:: 0.20.0

Parameters
----------
func : function, str, list or dict
    Function to use for aggregating the data. If a function, must either
    work when passed a DataFrame or when passed to DataFrame.apply.

    Accepted combinations are:

    - function
    - string function name
    - list of functions and/or function names, e.g. ``[np.sum, 'mean']``
    - dict of axis labels -> functions, function names or list of such.
axis : {0 or 'index', 1 or 'columns'}, default 0
        If 0 or 'index': apply function to each column.
        If 1 or 'columns': apply function to each row.
*args
    Positional arguments to pass to `func`.
**kwargs
    Keyword arguments to pass to `func`.

Returns
-------
scalar, Series or DataFrame

    The return can be:

    * scalar : when Series.agg is called with single function
    * Series : when DataFrame.agg is called with a single function
    * DataFrame : when DataFrame.agg is called with several functions

    Return scalar, Series or DataFrame.

The aggregation operations are always performed over an axis, either the
index (default) or the column axis. This behavior is different from
`numpy` aggregation functions (`mean`, `median`, `prod`, `sum`, `std`,
`var`), where the default is to compute the aggregation of the flattened
array, e.g., ``numpy.mean(arr_2d)`` as opposed to
``numpy.mean(arr_2d, axis=0)``.

`agg` is an alias for `aggregate`. Use the alias.

See Also
--------
DataFrame.apply : Perform any type of operations.
DataFrame.transform : Perform transformation type operations.
core.groupby.GroupBy : Perform operations over groups.
core.resample.Resampler : Perform operations over resampled bins.
core.window.Rolling : Perform operations over rolling window.
core.window.Expanding : Perform operations over expanding window.
core.window.EWM : Perform operation over exponential weighted
    window.

Notes
-----
`agg` is an alias for `aggregate`. Use the alias.

A passed user-defined-function will be passed a Series for evaluation.

Examples
--------
>>> df = pd.DataFrame([[1, 2, 3],
...                    [4, 5, 6],
...                    [7, 8, 9],
...                    [np.nan, np.nan, np.nan]],
...                   columns=['A', 'B', 'C'])

Aggregate these functions over the rows.

>>> df.agg(['sum', 'min'])
        A     B     C
sum  12.0  15.0  18.0
min   1.0   2.0   3.0

Different aggregations per column.

>>> df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
        A    B
max   NaN  8.0
min   1.0  2.0
sum  12.0  NaN

Aggregate over the columns.

>>> df.agg("mean", axis="columns")
0    2.0
1    5.0
2    8.0
3    NaN
dtype: float64
"""
        pass
    def align(
        self,
        other: Union[DataFrame, Series[Dtype]],
        join: Union[_str, Literal["inner", "outer", "left", "right"]] = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        fill_value = ...,
        method: Optional[Union[_str, Literal["backfill", "bfill", "pad", "ffill"]]] = ...,
        limit: Optional[int] = ...,
        fill_axis: AxisType = ...,
        broadcast_axis: Optional[AxisType] = ...,
    ) -> DataFrame:
        """Align two objects on their axes with the specified join method.

Join method is specified for each axis Index.

Parameters
----------
other : DataFrame or Series
join : {'outer', 'inner', 'left', 'right'}, default 'outer'
axis : allowed axis of the other object, default None
    Align on index (0), columns (1), or both (None).
level : int or level name, default None
    Broadcast across a level, matching Index values on the
    passed MultiIndex level.
copy : bool, default True
    Always returns new objects. If copy=False and no reindexing is
    required then original objects are returned.
fill_value : scalar, default np.NaN
    Value to use for missing values. Defaults to NaN, but can be any
    "compatible" value.
method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
    Method to use for filling holes in reindexed Series:

    - pad / ffill: propagate last valid observation forward to next valid.
    - backfill / bfill: use NEXT valid observation to fill gap.

limit : int, default None
    If method is specified, this is the maximum number of consecutive
    NaN values to forward/backward fill. In other words, if there is
    a gap with more than this number of consecutive NaNs, it will only
    be partially filled. If method is not specified, this is the
    maximum number of entries along the entire axis where NaNs will be
    filled. Must be greater than 0 if not None.
fill_axis : {0 or 'index', 1 or 'columns'}, default 0
    Filling axis, method and limit.
broadcast_axis : {0 or 'index', 1 or 'columns'}, default None
    Broadcast values along this axis, if aligning two objects of
    different dimensions.

Returns
-------
(left, right) : (DataFrame, type of other)
    Aligned objects.
"""
        pass
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None:
        """Fill NA/NaN values using the specified method.

Parameters
----------
value : scalar, dict, Series, or DataFrame
    Value to use to fill holes (e.g. 0), alternately a
    dict/Series/DataFrame of values specifying which value to use for
    each index (for a Series) or column (for a DataFrame).  Values not
    in the dict/Series/DataFrame will not be filled. This value cannot
    be a list.
method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
    Method to use for filling holes in reindexed Series
    pad / ffill: propagate last valid observation forward to next valid
    backfill / bfill: use next valid observation to fill gap.
axis : {0 or 'index', 1 or 'columns'}
    Axis along which to fill missing values.
inplace : bool, default False
    If True, fill in-place. Note: this will modify any
    other views on this object (e.g., a no-copy slice for a column in a
    DataFrame).
limit : int, default None
    If method is specified, this is the maximum number of consecutive
    NaN values to forward/backward fill. In other words, if there is
    a gap with more than this number of consecutive NaNs, it will only
    be partially filled. If method is not specified, this is the
    maximum number of entries along the entire axis where NaNs will be
    filled. Must be greater than 0 if not None.
downcast : dict, default is None
    A dict of item->dtype of what to downcast if possible,
    or the string 'infer' which will try to downcast to an appropriate
    equal type (e.g. float64 to int64 if possible).

Returns
-------
DataFrame or None
    Object with missing values filled or None if ``inplace=True``.

See Also
--------
interpolate : Fill NaN values using interpolation.
reindex : Conform object to new index.
asfreq : Convert TimeSeries to specified frequency.

Examples
--------
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
...                    [3, 4, np.nan, 1],
...                    [np.nan, np.nan, np.nan, 5],
...                    [np.nan, 3, np.nan, 4]],
...                   columns=list('ABCD'))
>>> df
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4

Replace all NaN elements with 0s.

>>> df.fillna(0)
    A   B   C   D
0   0.0 2.0 0.0 0
1   3.0 4.0 0.0 1
2   0.0 0.0 0.0 5
3   0.0 3.0 0.0 4

We can also propagate non-null values forward or backward.

>>> df.fillna(method='ffill')
    A   B   C   D
0   NaN 2.0 NaN 0
1   3.0 4.0 NaN 1
2   3.0 4.0 NaN 5
3   3.0 3.0 NaN 4

Replace all NaN elements in column 'A', 'B', 'C', and 'D', with 0, 1,
2, and 3 respectively.

>>> values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
>>> df.fillna(value=values)
    A   B   C   D
0   0.0 2.0 2.0 0
1   3.0 4.0 2.0 1
2   0.0 1.0 2.0 5
3   0.0 3.0 2.0 4

Only replace the first NaN element.

>>> df.fillna(value=values, limit=1)
    A   B   C   D
0   0.0 2.0 2.0 0
1   3.0 4.0 NaN 1
2   NaN 1.0 NaN 5
3   NaN 3.0 NaN 4
"""
        pass
    def groupby(
        self,
        by: Optional[Union[List[_str], _str]],
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> DataFrameGroupBy:
        """Group DataFrame using a mapper or by a Series of columns.

A groupby operation involves some combination of splitting the
object, applying a function, and combining the results. This can be
used to group large amounts of data and compute operations on these
groups.

Parameters
----------
by : mapping, function, label, or list of labels
    Used to determine the groups for the groupby.
    If ``by`` is a function, it's called on each value of the object's
    index. If a dict or Series is passed, the Series or dict VALUES
    will be used to determine the groups (the Series' values are first
    aligned; see ``.align()`` method). If an ndarray is passed, the
    values are used as-is determine the groups. A label or list of
    labels may be passed to group by the columns in ``self``. Notice
    that a tuple is interpreted as a (single) key.
axis : {0 or 'index', 1 or 'columns'}, default 0
    Split along rows (0) or columns (1).
level : int, level name, or sequence of such, default None
    If the axis is a MultiIndex (hierarchical), group by a particular
    level or levels.
as_index : bool, default True
    For aggregated output, return object with group labels as the
    index. Only relevant for DataFrame input. as_index=False is
    effectively "SQL-style" grouped output.
sort : bool, default True
    Sort group keys. Get better performance by turning this off.
    Note this does not influence the order of observations within each
    group. Groupby preserves the order of rows within each group.
group_keys : bool, default True
    When calling apply, add group keys to index to identify pieces.
squeeze : bool, default False
    Reduce the dimensionality of the return type if possible,
    otherwise return a consistent type.
observed : bool, default False
    This only applies if any of the groupers are Categoricals.
    If True: only show observed values for categorical groupers.
    If False: show all values for categorical groupers.

    .. versionadded:: 0.23.0

Returns
-------
DataFrameGroupBy
    Returns a groupby object that contains information about the groups.

See Also
--------
resample : Convenience method for frequency conversion and resampling
    of time series.

Notes
-----
See the `user guide
<https://pandas.pydata.org/pandas-docs/stable/groupby.html>`_ for more.

Examples
--------
>>> df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
...                               'Parrot', 'Parrot'],
...                    'Max Speed': [380., 370., 24., 26.]})
>>> df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0
>>> df.groupby(['Animal']).mean()
        Max Speed
Animal
Falcon      375.0
Parrot       25.0

**Hierarchical Indexes**

We can groupby different levels of a hierarchical index
using the `level` parameter:

>>> arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
...           ['Captive', 'Wild', 'Captive', 'Wild']]
>>> index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
>>> df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]},
...                   index=index)
>>> df
                Max Speed
Animal Type
Falcon Captive      390.0
       Wild         350.0
Parrot Captive       30.0
       Wild          20.0
>>> df.groupby(level=0).mean()
        Max Speed
Animal
Falcon      370.0
Parrot       25.0
>>> df.groupby(level="Type").mean()
         Max Speed
Type
Captive      210.0
Wild         185.0
"""
        pass
    def isna(self) -> DataFrame:
        """Detect missing values.

Return a boolean same-sized object indicating if the values are NA.
NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
values.
Everything else gets mapped to False values. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.isnull : Alias of isna.
DataFrame.notna : Boolean inverse of isna.
DataFrame.dropna : Omit axes labels with missing values.
isna : Top-level isna.

Examples
--------
Show which entries in a DataFrame are NA.

>>> df = pd.DataFrame({'age': [5, 6, np.NaN],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.isna()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

Show which entries in a Series are NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.isna()
0    False
1    False
2     True
dtype: bool
"""
        pass
    def isnull(self) -> DataFrame:
        """Detect missing values.

Return a boolean same-sized object indicating if the values are NA.
NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
values.
Everything else gets mapped to False values. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.isnull : Alias of isna.
DataFrame.notna : Boolean inverse of isna.
DataFrame.dropna : Omit axes labels with missing values.
isna : Top-level isna.

Examples
--------
Show which entries in a DataFrame are NA.

>>> df = pd.DataFrame({'age': [5, 6, np.NaN],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.isna()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

Show which entries in a Series are NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.isna()
0    False
1    False
2     True
dtype: bool
"""
        pass
    def items(self) -> Iterable[Tuple[Optional[Hashable], Series]]:
        """Iterate over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with
the column name and the content as a Series.

Yields
------
label : object
    The column names for the DataFrame being iterated over.
content : Series
    The column entries belonging to each label, as a Series.

See Also
--------
DataFrame.iterrows : Iterate over DataFrame rows as
    (index, Series) pairs.
DataFrame.itertuples : Iterate over DataFrame rows as namedtuples
    of the values.

Examples
--------
>>> df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                   'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'])
>>> df
        species   population
panda   bear      1864
polar   bear      22000
koala   marsupial 80000
>>> for label, content in df.items():
...     print('label:', label)
...     print('content:', content, sep='\n')
...
label: species
content:
panda         bear
polar         bear
koala    marsupial
Name: species, dtype: object
label: population
content:
panda     1864
polar    22000
koala    80000
Name: population, dtype: int64
"""
        pass
    def iteritems(self) -> Iterable[Tuple[Label, Series]]:
        """Iterate over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with
the column name and the content as a Series.

Yields
------
label : object
    The column names for the DataFrame being iterated over.
content : Series
    The column entries belonging to each label, as a Series.

See Also
--------
DataFrame.iterrows : Iterate over DataFrame rows as
    (index, Series) pairs.
DataFrame.itertuples : Iterate over DataFrame rows as namedtuples
    of the values.

Examples
--------
>>> df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                   'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'])
>>> df
        species   population
panda   bear      1864
polar   bear      22000
koala   marsupial 80000
>>> for label, content in df.items():
...     print('label:', label)
...     print('content:', content, sep='\n')
...
label: species
content:
panda         bear
polar         bear
koala    marsupial
Name: species, dtype: object
label: population
content:
panda     1864
polar    22000
koala    80000
Name: population, dtype: int64
"""
        pass
    def melt(
        self,
        id_vars: Optional[Tuple, Sequence, np.ndarray] = ...,
        value_vars: Optional[Tuple, Sequence, np.ndarray] = ...,
        var_name: Optional[Scalar] = ...,
        value_name: Scalar = ...,
        col_level: Optional[Union[int, _str]] = ...,
        ignore_index: _bool = ...
    ) -> DataFrame:
        """Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

This function is useful to massage a DataFrame into a format where one
or more columns are identifier variables (`id_vars`), while all other
columns, considered measured variables (`value_vars`), are "unpivoted" to
the row axis, leaving just two non-identifier columns, 'variable' and
'value'.
.. versionadded:: 0.20.0

Parameters
----------
id_vars : tuple, list, or ndarray, optional
    Column(s) to use as identifier variables.
value_vars : tuple, list, or ndarray, optional
    Column(s) to unpivot. If not specified, uses all columns that
    are not set as `id_vars`.
var_name : scalar
    Name to use for the 'variable' column. If None it uses
    ``frame.columns.name`` or 'variable'.
value_name : scalar, default 'value'
    Name to use for the 'value' column.
col_level : int or str, optional
    If columns are a MultiIndex then use this level to melt.

Returns
-------
DataFrame
    Unpivoted DataFrame.

See Also
--------
melt
pivot_table
DataFrame.pivot
Series.explode

Examples
--------
>>> df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
...                    'B': {0: 1, 1: 3, 2: 5},
...                    'C': {0: 2, 1: 4, 2: 6}})
>>> df
   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

>>> df.melt(id_vars=['A'], value_vars=['B'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

>>> df.melt(id_vars=['A'], value_vars=['B', 'C'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5
3  a        C      2
4  b        C      4
5  c        C      6

The names of 'variable' and 'value' columns can be customized:

>>> df.melt(id_vars=['A'], value_vars=['B'],
...         var_name='myVarname', value_name='myValname')
   A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5

If you have multi-index columns:

>>> df.columns = [list('ABC'), list('DEF')]
>>> df
   A  B  C
   D  E  F
0  a  1  2
1  b  3  4
2  c  5  6

>>> df.melt(col_level=0, id_vars=['A'], value_vars=['B'])
   A variable  value
0  a        B      1
1  b        B      3
2  c        B      5

>>> df.melt(id_vars=[('A', 'D')], value_vars=[('B', 'E')])
  (A, D) variable_0 variable_1  value
0      a          B          E      1
1      b          B          E      3
2      c          B          E      5
"""
        pass
    def merge(
        self,
        right: Union[DataFrame, Series[Dtype]],
        how: Union[_str, Literal["left", "right", "inner", "outer"]] = ...,
        on: Optional[Union[Level, List[Level]]] = ...,
        left_on: Optional[Union[Level, List[Level]]] = ...,
        right_on: Optional[Union[Level, List[Level]]] = ...,
        left_index: _bool = ...,
        right_index: _bool = ...,
        sort: _bool = ...,
        suffixes: Tuple[_str, _str] = ...,
        copy: _bool = ...,
        indicator: Union[_bool, _str] = ...,
        validate: Optional[_str] = ...,
    ) -> DataFrame:
        """Merge DataFrame or named Series objects with a database-style join.

The join is done on columns or indexes. If joining columns on
columns, the DataFrame indexes *will be ignored*. Otherwise if joining indexes
on indexes or indexes on a column or columns, the index will be passed on.

Parameters
----------
right : DataFrame or named Series
    Object to merge with.
how : {'left', 'right', 'outer', 'inner'}, default 'inner'
    Type of merge to be performed.

    * left: use only keys from left frame, similar to a SQL left outer join;
      preserve key order.
    * right: use only keys from right frame, similar to a SQL right outer join;
      preserve key order.
    * outer: use union of keys from both frames, similar to a SQL full outer
      join; sort keys lexicographically.
    * inner: use intersection of keys from both frames, similar to a SQL inner
      join; preserve the order of the left keys.
on : label or list
    Column or index level names to join on. These must be found in both
    DataFrames. If `on` is None and not merging on indexes then this defaults
    to the intersection of the columns in both DataFrames.
left_on : label or list, or array-like
    Column or index level names to join on in the left DataFrame. Can also
    be an array or list of arrays of the length of the left DataFrame.
    These arrays are treated as if they are columns.
right_on : label or list, or array-like
    Column or index level names to join on in the right DataFrame. Can also
    be an array or list of arrays of the length of the right DataFrame.
    These arrays are treated as if they are columns.
left_index : bool, default False
    Use the index from the left DataFrame as the join key(s). If it is a
    MultiIndex, the number of keys in the other DataFrame (either the index
    or a number of columns) must match the number of levels.
right_index : bool, default False
    Use the index from the right DataFrame as the join key. Same caveats as
    left_index.
sort : bool, default False
    Sort the join keys lexicographically in the result DataFrame. If False,
    the order of the join keys depends on the join type (how keyword).
suffixes : tuple of (str, str), default ('_x', '_y')
    Suffix to apply to overlapping column names in the left and right
    side, respectively. To raise an exception on overlapping columns use
    (False, False).
copy : bool, default True
    If False, avoid copy if possible.
indicator : bool or str, default False
    If True, adds a column to output DataFrame called "_merge" with
    information on the source of each row.
    If string, column with information on source of each row will be added to
    output DataFrame, and column will be named value of string.
    Information column is Categorical-type and takes on a value of "left_only"
    for observations whose merge key only appears in 'left' DataFrame,
    "right_only" for observations whose merge key only appears in 'right'
    DataFrame, and "both" if the observation's merge key is found in both.

validate : str, optional
    If specified, checks if merge is of specified type.

    * "one_to_one" or "1:1": check if merge keys are unique in both
      left and right datasets.
    * "one_to_many" or "1:m": check if merge keys are unique in left
      dataset.
    * "many_to_one" or "m:1": check if merge keys are unique in right
      dataset.
    * "many_to_many" or "m:m": allowed, but does not result in checks.

    .. versionadded:: 0.21.0

Returns
-------
DataFrame
    A DataFrame of the two merged objects.

See Also
--------
merge_ordered : Merge with optional filling/interpolation.
merge_asof : Merge on nearest keys.
DataFrame.join : Similar method using indices.

Notes
-----
Support for specifying index levels as the `on`, `left_on`, and
`right_on` parameters was added in version 0.23.0
Support for merging named Series objects was added in version 0.24.0

Examples
--------

>>> df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [1, 2, 3, 5]})
>>> df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [5, 6, 7, 8]})
>>> df1
    lkey value
0   foo      1
1   bar      2
2   baz      3
3   foo      5
>>> df2
    rkey value
0   foo      5
1   bar      6
2   baz      7
3   foo      8

Merge df1 and df2 on the lkey and rkey columns. The value columns have
the default suffixes, _x and _y, appended.

>>> df1.merge(df2, left_on='lkey', right_on='rkey')
  lkey  value_x rkey  value_y
0  foo        1  foo        5
1  foo        1  foo        8
2  foo        5  foo        5
3  foo        5  foo        8
4  bar        2  bar        6
5  baz        3  baz        7

Merge DataFrames df1 and df2 with specified left and right suffixes
appended to any overlapping columns.

>>> df1.merge(df2, left_on='lkey', right_on='rkey',
...           suffixes=('_left', '_right'))
  lkey  value_left rkey  value_right
0  foo           1  foo            5
1  foo           1  foo            8
2  foo           5  foo            5
3  foo           5  foo            8
4  bar           2  bar            6
5  baz           3  baz            7

Merge DataFrames df1 and df2, but raise an exception if the DataFrames have
any overlapping columns.

>>> df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False))
Traceback (most recent call last):
...
ValueError: columns overlap but no suffix specified:
    Index(['value'], dtype='object')
"""
        pass
    def notna(self) -> DataFrame:
        """Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA.
Non-missing values get mapped to True. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).
NA values, such as None or :attr:`numpy.NaN`, get mapped to False
values.

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.notnull : Alias of notna.
DataFrame.isna : Boolean inverse of notna.
DataFrame.dropna : Omit axes labels with missing values.
notna : Top-level notna.

Examples
--------
Show which entries in a DataFrame are not NA.

>>> df = pd.DataFrame({'age': [5, 6, np.NaN],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.notna()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

Show which entries in a Series are not NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.notna()
0     True
1     True
2    False
dtype: bool
"""
        pass
    def notnull(self) -> DataFrame:
        """Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA.
Non-missing values get mapped to True. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).
NA values, such as None or :attr:`numpy.NaN`, get mapped to False
values.

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is not an NA value.

See Also
--------
DataFrame.notnull : Alias of notna.
DataFrame.isna : Boolean inverse of notna.
DataFrame.dropna : Omit axes labels with missing values.
notna : Top-level notna.

Examples
--------
Show which entries in a DataFrame are not NA.

>>> df = pd.DataFrame({'age': [5, 6, np.NaN],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.notna()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

Show which entries in a Series are not NA.

>>> ser = pd.Series([5, 6, np.NaN])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

>>> ser.notna()
0     True
1     True
2    False
dtype: bool
"""
        pass
    def pivot(
        self, index = ..., columns = ..., values = ...,
    ) -> DataFrame
        """Return reshaped DataFrame organized by given index / column values.

Reshape data (produce a "pivot" table) based on column values. Uses
unique values from specified `index` / `columns` to form axes of the
resulting DataFrame. This function does not support data
aggregation, multiple values will result in a MultiIndex in the
columns. See the :ref:`User Guide <reshaping>` for more on reshaping.

Parameters
----------
index : str or object, optional
    Column to use to make new frame's index. If None, uses
    existing index.
columns : str or object
    Column to use to make new frame's columns.
values : str, object or a list of the previous, optional
    Column(s) to use for populating new frame's values. If not
    specified, all remaining columns will be used and the result will
    have hierarchically indexed columns.

    .. versionchanged:: 0.23.0
       Also accept list of column names.

Returns
-------
DataFrame
    Returns reshaped DataFrame.

Raises
------
ValueError:
    When there are any `index`, `columns` combinations with multiple
    values. `DataFrame.pivot_table` when you need to aggregate.

See Also
--------
DataFrame.pivot_table : Generalization of pivot that can handle
    duplicate values for one index/column pair.
DataFrame.unstack : Pivot based on the index values instead of a
    column.

Notes
-----
For finer-tuned control, see hierarchical indexing documentation along
with the related stack/unstack methods.

Examples
--------
>>> df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
...                            'two'],
...                    'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
...                    'baz': [1, 2, 3, 4, 5, 6],
...                    'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
>>> df
    foo   bar  baz  zoo
0   one   A    1    x
1   one   B    2    y
2   one   C    3    z
3   two   A    4    q
4   two   B    5    w
5   two   C    6    t

>>> df.pivot(index='foo', columns='bar', values='baz')
bar  A   B   C
foo
one  1   2   3
two  4   5   6

>>> df.pivot(index='foo', columns='bar')['baz']
bar  A   B   C
foo
one  1   2   3
two  4   5   6

>>> df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
      baz       zoo
bar   A  B  C   A  B  C
foo
one   1  2  3   x  y  z
two   4  5  6   q  w  t

A ValueError is raised if there are any duplicates.

>>> df = pd.DataFrame({"foo": ['one', 'one', 'two', 'two'],
...                    "bar": ['A', 'A', 'B', 'C'],
...                    "baz": [1, 2, 3, 4]})
>>> df
   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4

Notice that the first two rows are the same for our `index`
and `columns` arguments.

>>> df.pivot(index='foo', columns='bar', values='baz')
Traceback (most recent call last):
   ...
ValueError: Index contains duplicate entries, cannot reshape
"""
        pass
    def pivot_table(
        self,
        values: Optional[_str] = ...,
        index: Optional[_str, Grouper, Sequence] = ...,
        columns: Optional[_str, Grouper, Sequence] = ...,
        aggfunc = ...,
        fill_value: Optional[Scalar] = ...,
        margins: _bool = ...,
        dropna: _bool = ...,
        margins_name: _str = ...,
        observed: _bool = ...,
    ) -> DataFrame:
        """Create a spreadsheet-style pivot table as a DataFrame.

The levels in the pivot table will be stored in MultiIndex objects
(hierarchical indexes) on the index and columns of the result DataFrame.

Parameters
----------
values : column to aggregate, optional
index : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The
    list can contain any of the other types (except list).
    Keys to group by on the pivot table index.  If an array is passed,
    it is being used as the same manner as column values.
columns : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The
    list can contain any of the other types (except list).
    Keys to group by on the pivot table column.  If an array is passed,
    it is being used as the same manner as column values.
aggfunc : function, list of functions, dict, default numpy.mean
    If list of functions passed, the resulting pivot table will have
    hierarchical columns whose top level are the function names
    (inferred from the function objects themselves)
    If dict is passed, the key is column to aggregate and value
    is function or list of functions.
fill_value : scalar, default None
    Value to replace missing values with.
margins : bool, default False
    Add all row / columns (e.g. for subtotal / grand totals).
dropna : bool, default True
    Do not include columns whose entries are all NaN.
margins_name : str, default 'All'
    Name of the row / column that will contain the totals
    when margins is True.
observed : bool, default False
    This only applies if any of the groupers are Categoricals.
    If True: only show observed values for categorical groupers.
    If False: show all values for categorical groupers.

    .. versionchanged:: 0.25.0

Returns
-------
DataFrame
    An Excel style pivot table.

See Also
--------
DataFrame.pivot : Pivot without aggregation that can handle
    non-numeric data.

Examples
--------
>>> df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
...                          "bar", "bar", "bar", "bar"],
...                    "B": ["one", "one", "one", "two", "two",
...                          "one", "one", "two", "two"],
...                    "C": ["small", "large", "large", "small",
...                          "small", "large", "small", "small",
...                          "large"],
...                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
...                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
>>> df
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9

This first example aggregates values by taking the sum.

>>> table = pd.pivot_table(df, values='D', index=['A', 'B'],
...                     columns=['C'], aggfunc=np.sum)
>>> table
C        large  small
A   B
bar one    4.0    5.0
    two    7.0    6.0
foo one    4.0    1.0
    two    NaN    6.0

We can also fill missing values using the `fill_value` parameter.

>>> table = pd.pivot_table(df, values='D', index=['A', 'B'],
...                     columns=['C'], aggfunc=np.sum, fill_value=0)
>>> table
C        large  small
A   B
bar one      4      5
    two      7      6
foo one      4      1
    two      0      6

The next example aggregates by taking the mean across multiple columns.

>>> table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
...                     aggfunc={'D': np.mean,
...                              'E': np.mean})
>>> table
                D         E
A   C
bar large  5.500000  7.500000
    small  5.500000  8.500000
foo large  2.000000  4.500000
    small  2.333333  4.333333

We can also calculate multiple types of aggregations for any given
value column.

>>> table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
...                     aggfunc={'D': np.mean,
...                              'E': [min, max, np.mean]})
>>> table
                D    E
            mean  max      mean  min
A   C
bar large  5.500000  9.0  7.500000  6.0
    small  5.500000  9.0  8.500000  8.0
foo large  2.000000  5.0  4.500000  4.0
    small  2.333333  6.0  4.333333  2.0
"""
        pass
    def reindex(**kwargs) -> DataFrame:
        """Conform DataFrame to new index with optional filling logic.

Places NA/NaN in locations having no value in the previous index. A new object
is produced unless the new index is equivalent to the current one and
``copy=False``.

Parameters
----------
labels : array-like, optional
            New labels / index to conform the axis specified by 'axis' to.
index, columns : array-like, optional
    New labels / index to conform to, should be specified using
    keywords. Preferably an Index object to avoid duplicating data.
axis : int or str, optional
            Axis to target. Can be either the axis name ('index', 'columns')
            or number (0, 1).
method : {None, 'backfill'/'bfill', 'pad'/'ffill', 'nearest'}
    Method to use for filling holes in reindexed DataFrame.
    Please note: this is only applicable to DataFrames/Series with a
    monotonically increasing/decreasing index.

    * None (default): don't fill gaps
    * pad / ffill: Propagate last valid observation forward to next
      valid.
    * backfill / bfill: Use next valid observation to fill gap.
    * nearest: Use nearest valid observations to fill gap.

copy : bool, default True
    Return a new object, even if the passed indexes are the same.
level : int or name
    Broadcast across a level, matching Index values on the
    passed MultiIndex level.
fill_value : scalar, default np.NaN
    Value to use for missing values. Defaults to NaN, but can be any
    "compatible" value.
limit : int, default None
    Maximum number of consecutive elements to forward or backward fill.
tolerance : optional
    Maximum distance between original and new labels for inexact
    matches. The values of the index at the matching locations most
    satisfy the equation ``abs(index[indexer] - target) <= tolerance``.

    Tolerance may be a scalar value, which applies the same tolerance
    to all values, or list-like, which applies variable tolerance per
    element. List-like includes list, tuple, array, Series, and must be
    the same size as the index and its dtype must exactly match the
    index's type.

    .. versionadded:: 0.21.0 (list-like tolerance)

Returns
-------
DataFrame with changed index.

See Also
--------
DataFrame.set_index : Set row labels.
DataFrame.reset_index : Remove row labels or move them to new columns.
DataFrame.reindex_like : Change to same indices as other DataFrame.

Examples
--------

``DataFrame.reindex`` supports two calling conventions

* ``(index=index_labels, columns=column_labels, ...)``
* ``(labels, axis={'index', 'columns'}, ...)``

We *highly* recommend using keyword arguments to clarify your
intent.

Create a dataframe with some fictional data.

>>> index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
>>> df = pd.DataFrame({'http_status': [200, 200, 404, 404, 301],
...                   'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
...                   index=index)
>>> df
           http_status  response_time
Firefox            200           0.04
Chrome             200           0.02
Safari             404           0.07
IE10               404           0.08
Konqueror          301           1.00

Create a new index and reindex the dataframe. By default
values in the new index that do not have corresponding
records in the dataframe are assigned ``NaN``.

>>> new_index = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10',
...              'Chrome']
>>> df.reindex(new_index)
               http_status  response_time
Safari               404.0           0.07
Iceweasel              NaN            NaN
Comodo Dragon          NaN            NaN
IE10                 404.0           0.08
Chrome               200.0           0.02

We can fill in the missing values by passing a value to
the keyword ``fill_value``. Because the index is not monotonically
increasing or decreasing, we cannot use arguments to the keyword
``method`` to fill the ``NaN`` values.

>>> df.reindex(new_index, fill_value=0)
               http_status  response_time
Safari                 404           0.07
Iceweasel                0           0.00
Comodo Dragon            0           0.00
IE10                   404           0.08
Chrome                 200           0.02

>>> df.reindex(new_index, fill_value='missing')
              http_status response_time
Safari                404          0.07
Iceweasel         missing       missing
Comodo Dragon     missing       missing
IE10                  404          0.08
Chrome                200          0.02

We can also reindex the columns.

>>> df.reindex(columns=['http_status', 'user_agent'])
           http_status  user_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

Or we can use "axis-style" keyword arguments

>>> df.reindex(['http_status', 'user_agent'], axis="columns")
           http_status  user_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

To further illustrate the filling functionality in
``reindex``, we will create a dataframe with a
monotonically increasing index (for example, a sequence
of dates).

>>> date_index = pd.date_range('1/1/2010', periods=6, freq='D')
>>> df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
...                    index=date_index)
>>> df2
            prices
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0

Suppose we decide to expand the dataframe to cover a wider
date range.

>>> date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
>>> df2.reindex(date_index2)
            prices
2009-12-29     NaN
2009-12-30     NaN
2009-12-31     NaN
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

The index entries that did not have a value in the original data frame
(for example, '2009-12-29') are by default filled with ``NaN``.
If desired, we can fill in the missing values using one of several
options.

For example, to back-propagate the last valid value to fill the ``NaN``
values, pass ``bfill`` as an argument to the ``method`` keyword.

>>> df2.reindex(date_index2, method='bfill')
            prices
2009-12-29   100.0
2009-12-30   100.0
2009-12-31   100.0
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

Please note that the ``NaN`` value present in the original dataframe
(at index value 2010-01-03) will not be filled by any of the
value propagation schemes. This is because filling while reindexing
does not look at dataframe values, but only compares the original and
desired indexes. If you do want to fill in the ``NaN`` values present
in the original dataframe, use the ``fillna()`` method.

See the :ref:`user guide <basics.reindexing>` for more.
        """
        pass
    def replace(
        self,
        to_replace = ...,
        value: Optional[Union[Scalar, Sequence, Mapping, Pattern]] = ...,
        limit: Optional[int] = ...,
        regex = ...,
        method: Optional[_str] = ...,
        *,
        inplace: Literal[True]
    ) -> None:
        """Replace values given in `to_replace` with `value`.

Values of the DataFrame are replaced with other values dynamically.
This differs from updating with ``.loc`` or ``.iloc``, which require
you to specify a location to update with some value.

Parameters
----------
to_replace : str, regex, list, dict, Series, int, float, or None
    How to find the values that will be replaced.

    * numeric, str or regex:

        - numeric: numeric values equal to `to_replace` will be
          replaced with `value`
        - str: string exactly matching `to_replace` will be replaced
          with `value`
        - regex: regexs matching `to_replace` will be replaced with
          `value`

    * list of str, regex, or numeric:

        - First, if `to_replace` and `value` are both lists, they
          **must** be the same length.
        - Second, if ``regex=True`` then all of the strings in **both**
          lists will be interpreted as regexs otherwise they will match
          directly. This doesn't matter much for `value` since there
          are only a few possible substitution regexes you can use.
        - str, regex and numeric rules apply as above.

    * dict:

        - Dicts can be used to specify different replacement values
          for different existing values. For example,
          ``{'a': 'b', 'y': 'z'}`` replaces the value 'a' with 'b' and
          'y' with 'z'. To use a dict in this way the `value`
          parameter should be `None`.
        - For a DataFrame a dict can specify that different values
          should be replaced in different columns. For example,
          ``{'a': 1, 'b': 'z'}`` looks for the value 1 in column 'a'
          and the value 'z' in column 'b' and replaces these values
          with whatever is specified in `value`. The `value` parameter
          should not be ``None`` in this case. You can treat this as a
          special case of passing two lists except that you are
          specifying the column to search in.
        - For a DataFrame nested dictionaries, e.g.,
          ``{'a': {'b': np.nan}}``, are read as follows: look in column
          'a' for the value 'b' and replace it with NaN. The `value`
          parameter should be ``None`` to use a nested dict in this
          way. You can nest regular expressions as well. Note that
          column names (the top-level dictionary keys in a nested
          dictionary) **cannot** be regular expressions.

    * None:

        - This means that the `regex` argument must be a string,
          compiled regular expression, or list, dict, ndarray or
          Series of such elements. If `value` is also ``None`` then
          this **must** be a nested dictionary or Series.

    See the examples section for examples of each of these.
value : scalar, dict, list, str, regex, default None
    Value to replace any values matching `to_replace` with.
    For a DataFrame a dict of values can be used to specify which
    value to use for each column (columns not in the dict will not be
    filled). Regular expressions, strings and lists or dicts of such
    objects are also allowed.
inplace : bool, default False
    If True, in place. Note: this will modify any
    other views on this object (e.g. a column from a DataFrame).
    Returns the caller if this is True.
limit : int, default None
    Maximum size gap to forward or backward fill.
regex : bool or same types as `to_replace`, default False
    Whether to interpret `to_replace` and/or `value` as regular
    expressions. If this is ``True`` then `to_replace` *must* be a
    string. Alternatively, this could be a regular expression or a
    list, dict, or array of regular expressions in which case
    `to_replace` must be ``None``.
method : {'pad', 'ffill', 'bfill', `None`}
    The method to use when for replacement, when `to_replace` is a
    scalar, list or tuple and `value` is ``None``.

    .. versionchanged:: 0.23.0
        Added to DataFrame.

Returns
-------
DataFrame
    Object after replacement.

Raises
------
AssertionError
    * If `regex` is not a ``bool`` and `to_replace` is not
      ``None``.
TypeError
    * If `to_replace` is a ``dict`` and `value` is not a ``list``,
      ``dict``, ``ndarray``, or ``Series``
    * If `to_replace` is ``None`` and `regex` is not compilable
      into a regular expression or is a list, dict, ndarray, or
      Series.
    * When replacing multiple ``bool`` or ``datetime64`` objects and
      the arguments to `to_replace` does not match the type of the
      value being replaced
ValueError
    * If a ``list`` or an ``ndarray`` is passed to `to_replace` and
      `value` but they are not the same length.

See Also
--------
DataFrame.fillna : Fill NA values.
DataFrame.where : Replace values based on boolean condition.
Series.str.replace : Simple string replacement.

Notes
-----
* Regex substitution is performed under the hood with ``re.sub``. The
  rules for substitution for ``re.sub`` are the same.
* Regular expressions will only substitute on strings, meaning you
  cannot provide, for example, a regular expression matching floating
  point numbers and expect the columns in your frame that have a
  numeric dtype to be matched. However, if those floating point
  numbers *are* strings, then you can do this.
* This method has *a lot* of options. You are encouraged to experiment
  and play with this method to gain intuition about how it works.
* When dict is used as the `to_replace` value, it is like
  key(s) in the dict are the to_replace part and
  value(s) in the dict are the value parameter.

Examples
--------

**Scalar `to_replace` and `value`**

>>> s = pd.Series([0, 1, 2, 3, 4])
>>> s.replace(0, 5)
0    5
1    1
2    2
3    3
4    4
dtype: int64

>>> df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
...                    'B': [5, 6, 7, 8, 9],
...                    'C': ['a', 'b', 'c', 'd', 'e']})
>>> df.replace(0, 5)
   A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e

**List-like `to_replace`**

>>> df.replace([0, 1, 2, 3], 4)
   A  B  C
0  4  5  a
1  4  6  b
2  4  7  c
3  4  8  d
4  4  9  e

>>> df.replace([0, 1, 2, 3], [4, 3, 2, 1])
   A  B  C
0  4  5  a
1  3  6  b
2  2  7  c
3  1  8  d
4  4  9  e

>>> s.replace([1, 2], method='bfill')
0    0
1    3
2    3
3    3
4    4
dtype: int64

**dict-like `to_replace`**

>>> df.replace({0: 10, 1: 100})
     A  B  C
0   10  5  a
1  100  6  b
2    2  7  c
3    3  8  d
4    4  9  e

>>> df.replace({'A': 0, 'B': 5}, 100)
     A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
4    4    9  e

>>> df.replace({'A': {0: 100, 4: 400}})
     A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e

**Regular expression `to_replace`**

>>> df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
...                    'B': ['abc', 'bar', 'xyz']})
>>> df.replace(to_replace=r'^ba.$', value='new', regex=True)
      A    B
0   new  abc
1   foo  new
2  bait  xyz

>>> df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)
      A    B
0   new  abc
1   foo  bar
2  bait  xyz

>>> df.replace(regex=r'^ba.$', value='new')
      A    B
0   new  abc
1   foo  new
2  bait  xyz

>>> df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})
      A    B
0   new  abc
1   xyz  new
2  bait  xyz

>>> df.replace(regex=[r'^ba.$', 'foo'], value='new')
      A    B
0   new  abc
1   new  new
2  bait  xyz

Note that when replacing multiple ``bool`` or ``datetime64`` objects,
the data types in the `to_replace` parameter must match the data
type of the value being replaced:

>>> df = pd.DataFrame({'A': [True, False, True],
...                    'B': [False, True, False]})
>>> df.replace({'a string': 'new value', True: False})  # raises
Traceback (most recent call last):
    ...
TypeError: Cannot compare types 'ndarray(dtype=bool)' and 'str'

This raises a ``TypeError`` because one of the ``dict`` keys is not of
the correct type for replacement.

Compare the behavior of ``s.replace({'a': None})`` and
``s.replace('a', None)`` to understand the peculiarities
of the `to_replace` parameter:

>>> s = pd.Series([10, 'a', 'a', 'b', 'a'])

When one uses a dict as the `to_replace` value, it is like the
value(s) in the dict are equal to the `value` parameter.
``s.replace({'a': None})`` is equivalent to
``s.replace(to_replace={'a': None}, value=None, method=None)``:

>>> s.replace({'a': None})
0      10
1    None
2    None
3       b
4    None
dtype: object

When ``value=None`` and `to_replace` is a scalar, list or
tuple, `replace` uses the method parameter (default 'pad') to do the
replacement. So this is why the 'a' values are being replaced by 10
in rows 1 and 2 and 'b' in row 4 in this case.
The command ``s.replace('a', None)`` is actually equivalent to
``s.replace(to_replace='a', value=None, method='pad')``:

>>> s.replace('a', None)
0    10
1    10
2    10
3     b
4     b
dtype: object
"""
        pass
    def shift(
        self,
        periods: int = ...,
        freq = ...,
        axis: AxisType = ...,
        fill_value: Optional[Hashable] = ...,
    ) -> DataFrame:
        """Shift index by desired number of periods with an optional time `freq`.

When `freq` is not passed, shift the index without realigning the data.
If `freq` is passed (in this case, the index must be date or datetime,
or it will raise a `NotImplementedError`), the index will be
increased using the periods and the `freq`.

Parameters
----------
periods : int
    Number of periods to shift. Can be positive or negative.
freq : DateOffset, tseries.offsets, timedelta, or str, optional
    Offset to use from the tseries module or time rule (e.g. 'EOM').
    If `freq` is specified then the index values are shifted but the
    data is not realigned. That is, use `freq` if you would like to
    extend the index when shifting and preserve the original data.
axis : {0 or 'index', 1 or 'columns', None}, default None
    Shift direction.
fill_value : object, optional
    The scalar value to use for newly introduced missing values.
    the default depends on the dtype of `self`.
    For numeric data, ``np.nan`` is used.
    For datetime, timedelta, or period data, etc. :attr:`NaT` is used.
    For extension dtypes, ``self.dtype.na_value`` is used.

    .. versionchanged:: 0.24.0

Returns
-------
DataFrame
    Copy of input object, shifted.

See Also
--------
Index.shift : Shift values of Index.
DatetimeIndex.shift : Shift values of DatetimeIndex.
PeriodIndex.shift : Shift values of PeriodIndex.
tshift : Shift the time index, using the index's frequency if
    available.

Examples
--------
>>> df = pd.DataFrame({'Col1': [10, 20, 15, 30, 45],
...                    'Col2': [13, 23, 18, 33, 48],
...                    'Col3': [17, 27, 22, 37, 52]})

>>> df.shift(periods=3)
   Col1  Col2  Col3
0   NaN   NaN   NaN
1   NaN   NaN   NaN
2   NaN   NaN   NaN
3  10.0  13.0  17.0
4  20.0  23.0  27.0

>>> df.shift(periods=1, axis='columns')
   Col1  Col2  Col3
0   NaN  10.0  13.0
1   NaN  20.0  23.0
2   NaN  15.0  18.0
3   NaN  30.0  33.0
4   NaN  45.0  48.0

>>> df.shift(periods=3, fill_value=0)
   Col1  Col2  Col3
0     0     0     0
1     0     0     0
2     0     0     0
3    10    13    17
4    20    23    27
"""
        pass
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        ascending: _bool = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None:
        """Sort object by labels (along an axis).

Parameters
----------
axis : {0 or 'index', 1 or 'columns'}, default 0
    The axis along which to sort.  The value 0 identifies the rows,
    and 1 identifies the columns.
level : int or level name or list of ints or list of level names
    If not None, sort on values in specified index level(s).
ascending : bool, default True
    Sort ascending vs. descending.
inplace : bool, default False
    If True, perform operation in-place.
kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
    Choice of sorting algorithm. See also ndarray.np.sort for more
    information.  `mergesort` is the only stable algorithm. For
    DataFrames, this option is only applied when sorting on a single
    column or label.
na_position : {'first', 'last'}, default 'last'
    Puts NaNs at the beginning if `first`; `last` puts NaNs at the end.
    Not implemented for MultiIndex.
sort_remaining : bool, default True
    If True and sorting by level and index is multilevel, sort by other
    levels too (in order) after sorting by specified level.
ignore_index : bool, default False
    If True, the resulting axis will be labeled 0, 1, …, n - 1.

    .. versionadded:: 1.0.0

Returns
-------
sorted_obj : DataFrame or None
    DataFrame with sorted index if inplace=False, None otherwise.
"""
        pass
    def sort_values(
        self,
        by: Union[_str, Sequence[_str]],
        axis: AxisType = ...,
        ascending: _bool = ...,
        kind: Union[_str, Literal["quicksort", "mergesort", "heapsort"]] = ...,
        na_position: Union[_str, Literal["first", "last"]] = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None:
        """Sort by the values along either axis.

Parameters
----------
        by : str or list of str
            Name or list of names to sort by.

            - if `axis` is 0 or `'index'` then `by` may contain index
              levels and/or column labels.
            - if `axis` is 1 or `'columns'` then `by` may contain column
              levels and/or index labels.

            .. versionchanged:: 0.23.0

               Allow specifying index or column level names.
axis : {0 or 'index', 1 or 'columns'}, default 0
     Axis to be sorted.
ascending : bool or list of bool, default True
     Sort ascending vs. descending. Specify list for multiple sort
     orders.  If this is a list of bools, must match the length of
     the by.
inplace : bool, default False
     If True, perform operation in-place.
kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
     Choice of sorting algorithm. See also ndarray.np.sort for more
     information.  `mergesort` is the only stable algorithm. For
     DataFrames, this option is only applied when sorting on a single
     column or label.
na_position : {'first', 'last'}, default 'last'
     Puts NaNs at the beginning if `first`; `last` puts NaNs at the
     end.
ignore_index : bool, default False
     If True, the resulting axis will be labeled 0, 1, …, n - 1.

     .. versionadded:: 1.0.0

Returns
-------
sorted_obj : DataFrame or None
    DataFrame with sorted values if inplace=False, None otherwise.

Examples
--------
>>> df = pd.DataFrame({
...     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
...     'col2': [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
... })
>>> df
    col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
3   NaN  8    4
4   D    7    2
5   C    4    3

Sort by col1

>>> df.sort_values(by=['col1'])
    col1 col2 col3
0   A    2    0
1   A    1    1
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4

Sort by multiple columns

>>> df.sort_values(by=['col1', 'col2'])
    col1 col2 col3
1   A    1    1
0   A    2    0
2   B    9    9
5   C    4    3
4   D    7    2
3   NaN  8    4

Sort Descending

>>> df.sort_values(by='col1', ascending=False)
    col1 col2 col3
4   D    7    2
5   C    4    3
2   B    9    9
0   A    2    0
1   A    1    1
3   NaN  8    4

Putting NAs first

>>> df.sort_values(by='col1', ascending=False, na_position='first')
    col1 col2 col3
3   NaN  8    4
4   D    7    2
5   C    4    3
2   B    9    9
0   A    2    0
1   A    1    1
"""
        pass
    def to_markdown(self, buf: Optional[FilePathOrBuffer], mode: Optional[_str] = ..., **kwargs) -> None:
        """Print DataFrame in Markdown-friendly format.

.. versionadded:: 1.0.0

Parameters
----------
buf : writable buffer, defaults to sys.stdout
    Where to send the output. By default, the output is printed to
    sys.stdout. Pass a writable buffer if you need to further process
    the output.
mode : str, optional
    Mode in which file is opened.
**kwargs
    These parameters will be passed to `tabulate`.

Returns
-------
str
    DataFrame in Markdown-friendly format.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     data={"animal_1": ["elk", "pig"], "animal_2": ["dog", "quetzal"]}
        ... )
        >>> print(df.to_markdown())
        |    | animal_1   | animal_2   |
        |---:|:-----------|:-----------|
        |  0 | elk        | dog        |
        |  1 | pig        | quetzal    |
"""
        pass
    def transform(self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ..., *args, **kwargs) -> DataFrame:
        """Call ``func`` on self producing a DataFrame with transformed values.

Produced DataFrame will have same axis length as self.

Parameters
----------
func : function, str, list or dict
    Function to use for transforming the data. If a function, must either
    work when passed a DataFrame or when passed to DataFrame.apply.

    Accepted combinations are:

    - function
    - string function name
    - list of functions and/or function names, e.g. ``[np.exp. 'sqrt']``
    - dict of axis labels -> functions, function names or list of such.
axis : {0 or 'index', 1 or 'columns'}, default 0
    If 0 or 'index': apply function to each column.
    If 1 or 'columns': apply function to each row.
*args
    Positional arguments to pass to `func`.
**kwargs
    Keyword arguments to pass to `func`.

Returns
-------
DataFrame
    A DataFrame that must have the same length as self.

Raises
------
ValueError : If the returned DataFrame has a different length than self.

See Also
--------
DataFrame.agg : Only perform aggregating type operations.
DataFrame.apply : Invoke function on a DataFrame.

Examples
--------
>>> df = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
>>> df
   A  B
0  0  1
1  1  2
2  2  3
>>> df.transform(lambda x: x + 1)
   A  B
0  1  2
1  2  3
2  3  4

Even though the resulting DataFrame must have the same length as the
input DataFrame, it is possible to provide several input functions:

>>> s = pd.Series(range(3))
>>> s
0    0
1    1
2    2
dtype: int64
>>> s.transform([np.sqrt, np.exp])
       sqrt        exp
0  0.000000   1.000000
1  1.000000   2.718282
2  1.414214   7.389056
"""
        pass

