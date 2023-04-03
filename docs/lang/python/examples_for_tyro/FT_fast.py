# %%
'''
Fourior transformation and its inverse transformation
'''
import numpy as np

#! this is a slow method 
def sum_ft_slow(x_ls, fx_ls, delta_x, output_k): # coordinate to momentum   ## 19 mins
    ls = []
    for idx in range(len(x_ls)):
        ls.append( delta_x/(2*np.pi) * np.exp(1j * x_ls[idx] * output_k) * fx_ls[idx] )
    val = np.sum(np.array(ls))
    return val

#! fast
def sum_ft(x_ls, fx_ls, delta_x, output_k): # coordinate to momentum    ## 2.5 mins
    x_ls = np.array(x_ls)
    fx_ls = np.array(fx_ls)
    val = delta_x/(2*np.pi) * np.sum( np.exp(1j * x_ls * output_k) * fx_ls )
    return val

#! fast
def sum_ft_inv(k_ls, fk_ls, delta_k, output_x): # momentum to coordinate
    k_ls = np.array(k_ls)
    fk_ls = np.array(fk_ls)
    val = delta_k * np.sum( np.exp(-1j * k_ls * output_x) * fk_ls )

    return val