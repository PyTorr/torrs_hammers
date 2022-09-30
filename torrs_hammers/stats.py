import pandas as pd
from scipy import stats

def calculate_corr_with_pvalues(df, method = 'pearsonr'):
    '''
    Calculate the correlation between the columns of dataframe and return values with stars.
    :param df: dataframe
    :param method: pearsonr/ spearman
    :return: pvalues, corr_with_stars
    '''
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')

    rho = df.corr()

    for r in df.columns:
        for c in df.columns:
            if method == 'pearsonr':
                pvalues[r][c] = round(stats.pearsonr(df[r], df[c])[1], 4)
            elif method == 'spearman':
                pvalues[r][c] = round(stats.spearmanr(df[r], df[c])[1], 4)
            elif method == 'reg':
                slope, intercept, rho[r][c], pvalues[r][c], std_err = stats.linregress(x=df[r],y= df[c])

    rho = rho.round(2)
    pval = pvalues
    # create three masks
    r1 = rho.applymap(lambda x: '{}*'.format(x))
    r2 = rho.applymap(lambda x: '{}**'.format(x))
    r3 = rho.applymap(lambda x: '{}***'.format(x))
    # apply them where appropriate
    rho = rho.mask(pval <= 0.05, r1)
    rho = rho.mask(pval <= 0.01, r2)
    rho = rho.mask(pval <= 0.001, r3)

    return pvalues, rho

def ttest_or_mannwhitney(y1,y2):
    '''
    Check if y1 and y2 stand the assumptions for ttest and if not preform mannwhitney
    :param y1: 1st sample
    :param y2: 2nd sample
    :return: s, pvalue, ttest - True/False
    '''
    ttest = False

    # assumptions for t-test
    # https://pythonfordatascience.org/independent-t-test-python/#t_test-assumptions
    ns1, np1 = stats.shapiro(y1)  # test normality of the data
    ns2, np2 = stats.shapiro(y2)  # test noramlity of the data
    ls, lp = stats.levene(y1, y2)  # test that the variance behave the same
    if (lp > .05) & (np1 > .05) & (np2 > .05):
        ttest = True
        s, p = stats.ttest_ind(y1, y2)
    else:
        s, p = stats.mannwhitneyu(y1, y2)

    return s, p, ttest