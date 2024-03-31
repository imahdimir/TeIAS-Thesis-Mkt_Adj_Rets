"""

    """

import numpy as np
import pandas as pd
from mirutil.df import save_df_as_prq
from scipy import stats

from a_main import *

def read_stocks_cum_rets() :
    return pd.read_parquet(fp.t0)

def read_mkt_cum_rets() :
    return pd.read_parquet(fp.t1)

def merge_mkt_cum_ret(df , dfm) :
    return df.merge(dfm , on = [c.d , c.jd] , how = 'left')

def gen_mkt_adj_rets(df , win_start , win_end , col_name) :
    c1 = f'R-m{win_start}m{win_end}'
    c2 = f'M-m{win_start}m{win_end}'
    df[col_name] = df[c1] - df[c2]
    return df

def gen_all_mkt_adj_rets(df) :
    winds = {
            (2 , 1)    : cn.r1 ,
            (5 , 2)    : cn.r2 ,
            (27 , 5)   : cn.r6 ,
            (119 , 27) : cn.r28 ,
            }

    for (ws , we) , coln in winds.items() :
        df = gen_mkt_adj_rets(df , ws , we , coln)

    return df

def keep_some_cols(df) :
    cols = {
            c.ftic        : None ,
            c.d           : None ,
            c.jd          : None ,
            c.wd          : None ,
            c.is_tic_open : None ,
            cn.r1         : None ,
            cn.r2         : None ,
            cn.r6         : None ,
            cn.r28        : None ,
            }

    return df[list(cols.keys())]

def rep_inf_values_with_nan(df) :
    df = df.replace(np.inf , np.nan)
    return df

def rep_outliers_beyond_k_std_with_nan(df , coln , k) :
    z = stats.zscore(df[coln] , nan_policy = 'omit')
    abs_z = np.abs(z)
    msk = abs_z > k
    df.loc[msk , coln] = np.nan
    return df

def rep_all_outliers_in_all_mkt_adj_rets_with_nan(df) :
    for coln in [cn.r1 , cn.r2 , cn.r6 , cn.r28] :
        df = rep_outliers_beyond_k_std_with_nan(df , coln , 2)
    return df

def main() :
    pass

    ##

    df = read_stocks_cum_rets()
    dfm = read_mkt_cum_rets()

    ##

    df = merge_mkt_cum_ret(df , dfm)

    ##

    df = gen_all_mkt_adj_rets(df)

    ##

    df = keep_some_cols(df)

    ##

    df = rep_inf_values_with_nan(df)
    df = rep_all_outliers_in_all_mkt_adj_rets_with_nan(df)

    ##
    df1 = df.describe()
    df1

    ##

    save_df_as_prq(df , fp.t2)

##
if __name__ == "__main__" :
    main()
