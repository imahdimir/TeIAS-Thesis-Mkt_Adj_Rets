"""

    """

import pandas as pd
from githubdata import clone_overwrite_a_repo__ret_gdr_obj
from githubdata import make_data_fn
from githubdata import upload_2_github

from a_main import c
from a_main import fp
from a_main import gdu

def ret_data_fn(df) :
    ld = df[c.d].max()
    dn = gdu.thesis_mkt_adj_rets.split('/')[1]
    fn = make_data_fn(dn , ld)
    return fn

def clone_the_data_repo() :
    return clone_overwrite_a_repo__ret_gdr_obj(gdu.thesis_mkt_adj_rets)

def main() :
    pass

    ##

    df = pd.read_parquet(fp.t2)

    ##

    fn = ret_data_fn(df)

    ##

    gd = clone_the_data_repo()

    ##

    upload_2_github(gd , df , fn)

##
if __name__ == "__main__" :
    main()
