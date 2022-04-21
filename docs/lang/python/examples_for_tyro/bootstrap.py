# %%
'''
How to realize bootstrap resampling and related error estimation
'''


import gvar as gv
import numpy as np

def bootstrap(conf_ls, N_re): # used to make random numbers be configs
    N_conf = len(conf_ls)
    conf_re = []
    for times in range(N_re):
        idx_ls = np.random.randint(N_conf, size=N_conf)
        temp = []
        for idx in idx_ls:
            temp.append(conf_ls[idx])
        conf_re.append( np.average(temp, axis=0) )

    return np.array(conf_re)

N_conf = 100

data_1 = np.random.normal(loc=1, size=(N_conf)) # for example, C_2pt, 10 configs
data_2 = np.random.normal(loc=2, size=(N_conf)) # C_3pt, correlated with C_2pt, similar distribution

## we would like to calculate ratio = C_3pt/C_2pt in three methods ##

# %%
## method 1 ##            ## correct ##
N_re = 200

data_1_bs = bootstrap(data_1, N_re) # resampling for N_re times
data_2_bs = bootstrap(data_2, N_re)

ratio_ls = []
for n_re in range(N_re): # calculate ratio in each bs sample
    ratio_ls.append( data_2_bs[n_re] / data_1_bs[n_re] )

res1 = gv.dataset.avg_data(ratio_ls, bstrap=True)
resf = gv.dataset.avg_data(ratio_ls, bstrap=False)
print(res1)
print((res1.sdev / resf.sdev)**2) # should be about 200

# %%
## method 2 ## 
pt2_avg = gv.dataset.avg_data(data_1) # bstrap=False will make error 1/sqrt(N_re) 
pt3_avg = gv.dataset.avg_data(data_2)

res2 = pt3_avg / pt2_avg
print(res2)

# %%
## method 3 ##             ## wrong ##
ratio_ls = []
for n_conf in range(N_conf): # calculate ratio in each config
    ratio_ls.append( data_2[n_conf] / data_1[n_conf] )

res3 = gv.dataset.avg_data(ratio_ls)
print(res3)

# %%
