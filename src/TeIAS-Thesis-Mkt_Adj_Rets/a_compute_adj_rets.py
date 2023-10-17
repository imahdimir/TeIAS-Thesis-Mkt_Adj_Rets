"""

    """

from mirutil.df import save_df_as_prq
from u_d_adj_ret.a_compute_adj_rets import find_first_and_last_day_for_each_firm
from u_d_adj_ret.a_compute_adj_rets import gen_1_workday_filled_return
from u_d_adj_ret.a_compute_adj_rets import gen_is_tic_open_col
from u_d_adj_ret.a_compute_adj_rets import gen_linearly_filled_adj_close
from u_d_adj_ret.a_compute_adj_rets import get_adj_prices
from u_d_adj_ret.a_compute_adj_rets import get_tse_work_days
from u_d_adj_ret.a_compute_adj_rets import keep_only_large_enough_prices
from u_d_adj_ret.a_compute_adj_rets import keep_only_open_dates_of_tse
from u_d_adj_ret.a_compute_adj_rets import keep_relevant_cols
from u_d_adj_ret.a_compute_adj_rets import \
    make_all_days_for_each_ticker_if_mkt_open

from main import *

def main() :
    pass

    ##

    dfp = get_adj_prices()
    dfp = keep_relevant_cols(dfp)
    dfp = keep_only_large_enough_prices(dfp)

    ##

    dfw = get_tse_work_days()
    dfw = keep_only_open_dates_of_tse(dfw)

    ##

    dfp = find_first_and_last_day_for_each_firm(dfp)
    df = make_all_days_for_each_ticker_if_mkt_open(dfp , dfw)

    ##

    df = gen_is_tic_open_col(df)

    ##

    df = gen_linearly_filled_adj_close(df)
    df = gen_1_workday_filled_return(df)

    ##

    save_df_as_prq(df , fpn.t0)

##
if __name__ == "__main__" :
    main()
