# %%

'''
Correlation analysis in the lsqfit nonlinear fit.
'''

import gvar as gv
import numpy as np
import lsqfit as lsf

# %%
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

data = np.random.normal(loc=1, size=(5,5)) # 随机生成的数据

# %%
data_bs = bootstrap(data, 500) # more steps, better independence 通过 bootstrap 让随机数据变为独立样本

mean = np.mean(data_bs, axis=0) 
sdev = np.std(data_bs, axis=0) 
middle = np.median(data_bs, axis=0) 

data_avg = gv.dataset.avg_data(data_bs, bstrap=True) # gvar list
data_cov = gv.evalcov(data_avg) # 从 gvar 数组里抽取协方差矩阵
data_cov_np = np.cov(data_bs, rowvar=False) # 从数据样本里抽取协方差矩阵

def fcn(x, p):
    return p['a'] + p['b'] * x + p['c']

priors = gv.BufferDict()
priors['a'] = gv.gvar(1, 10)
priors['b'] = gv.gvar(1, 10)
priors['c'] = gv.gvar(1, 10)

x = np.arange(1, 6)
y1 = data_avg
y2 = gv.gvar(middle, data_cov)
y3 = gv.gvar(middle, data_cov_np)

res1 = lsf.nonlinear_fit(data=(x, y1), prior=priors, fcn=fcn, maxit=10000, svdcut=1e-100, fitter='scipy_least_squares') # 用 gvar(median, std) 做拟合

res2 = lsf.nonlinear_fit(data=(x, y2), prior=priors, fcn=fcn, maxit=10000, svdcut=1e-100, fitter='scipy_least_squares') # 用 gvar(median, 从 gvar 数组里抽取的协方差矩阵) 做拟合

res3 = lsf.nonlinear_fit(data=(x, y3), prior=priors, fcn=fcn, maxit=10000, svdcut=1e-100, fitter='scipy_least_squares') # 用 gvar(median, 从数据样本里抽取的协方差矩阵) 做拟合

print(res1.format(100))

print(res2.format(100)) # 和 res1 相同

print(res3.format(100)) # 和 res1, res2 有小的差别


# %%
# 从 gvar 数组里抽取的协方差矩阵和从数据样本里抽取的协方差矩阵有小的差异，原因是用 gv.evalcov() 从 gvar 数组里抽取协方差矩阵时，是将每个 gvar 元素当作一个高斯分布的独立变量，然后变量 A 和 变量 B 的协方差用 Cov(A, B) = ( mean(A*B) - mean(A)*mean(B) ) 来计算（如果 bstrap=False, 还要再除以 N）。下面的代码验证了这件事。

# 而我们这里生成的数据样本里，各个变量并不是高斯分布的，所以直接从数据样本里抽取的协方差矩阵和用 gv.evalcov() 从 gvar 数组里抽取的协方差矩阵不同。

a = np.random.normal(size=25)
b = np.random.normal(loc=1, size=25)
c = np.random.normal(loc=5, size=25)

data = {}
data['a'] = a
data['b'] = b
data['c'] = c

data_avg = gv.dataset.avg_data(data)
cov1 = gv.evalcov(data_avg)

sum = 0
for i in range(25):
    sum += a[i] * b[i]
covab = sum/25 - np.average(a) * np.average(b)

sum = 0
for i in range(25):
    sum += a[i] * c[i]
covac = sum/25 - np.average(a) * np.average(c)

# evalcov: Cov(X, Y) = ( mean(XY) - mean(X)*mean(Y) ) / N, divided by N is because bstrap=False
print(covab/25 - cov1['a', 'b']) 
print(covac/25 - cov1['a', 'c'])

# %%
