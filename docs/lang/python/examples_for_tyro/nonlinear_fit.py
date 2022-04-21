# %%

'''
An example of non-linear fit
'''

import numpy as np
import gvar as gv
import lsqfit as lsf
import matplotlib.pyplot as plt

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

# %%
data = np.random.normal(loc=1, size=(20,20)) # 随机生成的数据
data_bs = bootstrap(data, 500) # more steps, better independence 通过 bootstrap 让随机数据变为独立样本
data_avg = gv.dataset.avg_data(data_bs, bstrap=True) # gvar list，带误差的一组数据

def fcn(x, p):
    return p['a'] + p['b'] * x + p['c'] * x**2

priors = gv.BufferDict()
priors['a'] = gv.gvar(1, 10)
priors['b'] = gv.gvar(1, 10)
priors['c'] = gv.gvar(1, 10)

x = np.arange(1, 21)
y = data_avg

res = lsf.nonlinear_fit(data=(x, y), prior=priors, fcn=fcn, maxit=10000, svdcut=1e-100, fitter='scipy_least_squares')
print(res.format(100))

# %%
print(fcn(x, res.p))

plt.figure()
plt.errorbar(x, [val.mean for val in y], yerr=[val.sdev for val in y], label='data')
plt.fill_between(x, [val.mean + val.sdev for val in fcn(x, res.p)], [val.mean - val.sdev for val in fcn(x, res.p)], alpha=0.3, color='r', label='fit')
plt.legend()
plt.show()
# %%
