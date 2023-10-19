"""

    """

from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu
from run_py import DefaultDirs

class GDU :
    g = tgdu.GitHubDataUrl()

    tsetmc_adjclose_lin_s = g.tsetmc_adjclose_lin
    mkt_indx_s = g.mkt_indx

class Dirs :
    dd = DefaultDirs(make_default_dirs = True)

    gd = dd.gd
    t = dd.t

class FPN :
    dyr = Dirs()

    # temp data files
    t0 = dyr.t / '0_stocks_cum_rets.prq'
    t1 = dyr.t / '1_market_cum_rets.prq'

class ColName :
    pass

# class instances %%
c = tse_ns.Col()  # namespace
gdu = GDU()
dyr = Dirs()
fp = FPN()
cn = ColName()

##
