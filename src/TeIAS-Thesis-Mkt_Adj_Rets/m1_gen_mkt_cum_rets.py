"""

    """

import pandas as pd
from githubdata import get_data_wo_double_clone
from mirutil.df import save_df_as_prq

from a_main import *

shifters = {
        1   : None ,
        2   : None ,
        5   : None ,
        27  : None ,
        119 : None ,
        }

def get_overall_index() :
    df = get_data_wo_double_clone(gdu.mkt_indx_s)
    return df

def sort_on_date(df) :
    df[c.d] = pd.to_datetime(df[c.d])
    df = df.sort_values(by = c.d)
    df[c.d] = df[c.d].dt.strftime('%Y-%m-%d')
    return df

def convert_to_float(df) :
    df[c.tedpix_close] = df[c.tedpix_close].astype(float)
    return df

def gen_shifted_tedpix(df , shift_val) :
    nc = c.tedpix_close + f'-m{shift_val}'
    df[nc] = df[c.tedpix_close].shift(shift_val)
    return df

def gen_all_shifted_tedpix(df) :
    for shift_val in shifters.keys() :
        df = gen_shifted_tedpix(df , shift_val)
    return df

def gen_cum_ret_in_a_window(df , win_start , win_end) :
    cst = c.tedpix_close + f'-m{win_start}'
    ced = c.tedpix_close + f'-m{win_end}'
    nc = f'M-m{win_start}m{win_end}'

    # get cumulative return
    df[nc] = df[ced] / df[cst] - 1

    return df

def gen_cum_rets_in_all_windows(df) :
    winds = {
            2   : 1 ,
            5   : 2 ,
            27  : 5 ,
            119 : 27 ,
            }

    for ws , we in winds.items() :
        df = gen_cum_ret_in_a_window(df , ws , we)

    return df

def keep_some_cols(df) :
    cols = {
            c.d         : None ,
            c.jd        : None ,
            'M-m2m1'    : None ,
            'M-m5m2'    : None ,
            'M-m27m5'   : None ,
            'M-m119m27' : None ,
            }

    return df[list(cols.keys())]

def main() :
    pass

    ##

    df = get_overall_index()
    df = sort_on_date(df)
    df = convert_to_float(df)
    df = gen_all_shifted_tedpix(df)

    ##

    df = gen_cum_rets_in_all_windows(df)

    ##

    df = keep_some_cols(df)

    ##

    save_df_as_prq(df , fp.t1)

##
if __name__ == "__main__" :
    main()
