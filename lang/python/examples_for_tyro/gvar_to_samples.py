# %%
'''
transform gvar list to samples in gaussian distribution with/without correlation.
'''

import numpy as np
import gvar as gv

def gv_to_samples(gv_ls, N_samp):
    '''
    transform gvar to bs samples
    '''
    samp_ls = []
    for var in gv_ls:
        samp = np.random.normal(loc=var.mean, scale=var.sdev, size=N_samp)
        samp_ls.append(samp)

    samp_ls = np.array(samp_ls).T

    return samp_ls


def gv_to_samples_corr(gv_ls, N_samp):
    '''
    transform gvar to bs samples with correlation
    '''
    mean = [v.mean for v in gv_ls]
    cov_m = gv.evalcov(gv_ls)
    rng = np.random.default_rng()

    samp_ls = rng.multivariate_normal(mean, cov_m, size=N_samp)

    return samp_ls