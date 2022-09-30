import pandas as pd

def choose_multiple_values_in_column(df, colName, values):
    '''
    Return the dataframe (df) with selected string (values) in colName
    @param df: pandas dataframe
    @param colName: which column
    @param values: what are the values of intrest
    @return: dataframe (df) with selected string (values) in colName
    '''
    return df[df[colName].str.contains('|'.join(values))]

def sclmns(df, s, not_in=False):
    '''
    Return all the columns that (not) contain the names in s.
    :param df: pandas dataframe.
    :param s: string(s) the column(s) contains.
    :param not_in: all columns except the ones selected.
    :return: list of columns.
    '''
    clmns = []
    if not_in:
        # all_clmns = list(df.columns)
        all_clmns = df.columns
        for i in s:
            # all_clmns.remove(i)
            # all_clmns = [x for x in all_clmns if not x.__contains__(i)]
            all_clmns = all_clmns[~all_clmns.str.contains(i)]
        clmns = list(all_clmns)
        # clmns = all_clmns.copy()
    else:
        for i in s:
            clmns = clmns + list(df.columns[df.columns.str.contains(i)])
    return clmns

def save_latex(data_path, df, fn, ix = True):
    '''
    Save dataframe with latex file
    :param data_path: were to open the .tex file
    :param df: pandas dataframe
    :param fn: filename
    :param ix: save index
    :return:
    '''
    with open(data_path + '%s.tex' %fn, 'w') as tf:
        if type(df) != pd.core.frame.DataFrame:
            df = pd.DataFrame(df)
        tf.write(df.to_latex(float_format=lambda x: '%.3f' % x, index=ix))
        df.to_csv(data_path + '%s.csv' % fn)
