"""

    """

from namespace_mahdimir import tse as tse_ns
from namespace_mahdimir import tse_github_data_url as tgdu
from run_py import DefaultDirs

# namespace
c = tse_ns.Col()

class GDU :
    g = tgdu.GitHubDataUrl()


class Dirs :
    dd = DefaultDirs(make_default_dirs = True)

    gd = dd.gd
    t = dd.t

class FPN :
    dyr = Dirs()

    # temp data files
    t0 = dyr.t / 't0.prq'

class ColName :
    frst_d = "FirstDate"
    lst_d = "LastDate"
    lin_fill = "LinearlyFilledAdjClose"

# class instances   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
gdu = GDU()
dyr = Dirs()
fpn = FPN()
cn = ColName()
