"""
    Assumption:
        - All working days have a linear filled adjusted price for each ticker
    """

from mirutil.df import save_df_as_prq
import pandas as pd
from githubdata import get_data_wo_double_clone

from a_main import *

shifters = {
        1   : None ,
        2   : None ,
        5   : None ,
        27  : None ,
        119 : None ,
        }

def get_lin_filled_adj_price_data() :
    df = get_data_wo_double_clone(gdu.tsetmc_adjclose_lin_s)
    return df

def keep_relevant_cols(df) :
    c2d = {
            c.aclose : None ,
            }
    df = df.drop(columns = c2d.keys())
    return df

def gen_shifted_filled_adj_prices(df , shift_val) :
    nc = c.aclose_lin + f'-m{shift_val}'
    df[nc] = df.groupby(c.ftic)[c.aclose_lin].shift(shift_val)
    return df

def gen_all_shifted_adj_prices(df) :
    for shift_val in shifters.keys() :
        df = gen_shifted_filled_adj_prices(df , shift_val)
    return df

def gen_cum_ret_in_a_window(df , win_start , win_end) :
    cst = c.aclose_lin + f'-m{win_start}'
    ced = c.aclose_lin + f'-m{win_end}'
    nc = f'R-m{win_start}m{win_end}'

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
            c.ftic        : None ,
            c.d           : None ,
            c.jd          : None ,
            c.wd          : None ,
            c.is_tic_open : None ,
            'R-m2m1'      : None ,
            'R-m5m2'      : None ,
            'R-m27m5'     : None ,
            'R-m119m27'   : None ,
            }

    return df[list(cols.keys())]

def rename_ret_cols(df) :
    winds = {
            (2 , 1)    : cn.cr1 ,
            (5 , 2)    : cn.cr2 ,
            (27 , 5)   : cn.cr6 ,
            (119 , 27) : cn.cr28 ,
            }

    for (ws , we) , nc in winds.items() :
        oc = f'R-m{ws}m{we}'
        df = df.rename(columns = {
                oc : nc
                })

    return df

def main() :
    pass

    ##

    df = get_lin_filled_adj_price_data()
    df = keep_relevant_cols(df)

    ##

    df = gen_all_shifted_adj_prices(df)

    ##

    df = gen_cum_rets_in_all_windows(df)

    ##

    df = keep_some_cols(df)

    ##

    save_df_as_prq(df , fp.t0)
    
##
if __name__ == "__main__" :
    main()
