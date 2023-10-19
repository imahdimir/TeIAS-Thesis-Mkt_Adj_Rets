"""

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

def get_all_work_days_and_sort(df) :
    df = df[[c.d]].drop_duplicates()
    df[c.d] = pd.to_datetime(df[c.d])
    df = df.sort_values(c.d)
    df[c.d] = df[c.d].dt.strftime('%Y-%m-%d')
    return df

def gen_shifted_date(df , shift_val) :
    nc = c.d + f'-m{shift_val}'
    df[nc] = df[c.d].shift(shift_val)
    return df

def gen_all_shifted_dates(df) :
    for shift_val in shifters.keys() :
        df = gen_shifted_date(df , shift_val)
    return df

def main() :
    pass

    ##

    df = get_lin_filled_adj_price_data()
    df = keep_relevant_cols(df)

    ##

    dfd = get_all_work_days_and_sort(df)

    ##

    dfd = gen_all_shifted_dates(dfd)

    ##

    # merge shifted dates to the main dataframe
    df = df.merge(dfd , how = 'left' , on = c.d)

    ##

    dfp = df[[c.ftic , c.d , c.aclose_lin]]

    ##
    dfp = dfp.rename(columns = {
            c.aclose_lin : c.aclose_lin + '-m1'
            })

    df = df.merge(dfp ,
                  how = 'left' ,
                  left_on = [c.ftic , c.d + '-m1'] ,
                  right_on = [c.ftic , c.d])

    ##

    ##

    ##

    dfv = df.head()
    dfpv = dfp.head()

    ##

    ##

##
if __name__ == "__main__" :
    main()
