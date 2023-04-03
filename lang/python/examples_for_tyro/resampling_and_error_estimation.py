# %%
'''
Functions to realize bootstrap and jackknife resampling
Functions to do the sample average
'''

import numpy as np
import gvar as gv

def bootstrap(conf_ls):
    '''
    make sure conf_ls.shape = (N_conf, N_point)
    '''
    # return conf_ls

    conf_re = []
    bs_ls = gv.load('bs_ls_500')

    for times in range(len(bs_ls)):
        idx_ls = bs_ls[times]
        # idx_ls = np.random.randint(len(conf_ls), size=len(conf_ls)) ## do not use a fixed bs_ls
        temp = []
        for idx in idx_ls:
            temp.append(conf_ls[idx])

        conf_re.append( np.average(temp, axis=0) )

    return np.array(conf_re)

def jackknife(data): #data shape: (n_conf * n_t)
    nf, nt = data.shape #data shape: (n nf * n_t)
    cv = np.mean(data, 0) #将所有组态平均，cv shape: (1 * nt)
    cv = np.broadcast_to(cv, (nf, nt)) #将 cv 重新扩充为 data shape(n_cnf* n_t)
    jac = (nf * cv - data) / nf #(mean[N,:]*n_conf - data[N,:])/(n_conf-1) 等价于每次抽出 1 个数做平均 
    return jac #jac shape: (n_conf * n_t)

def jk_conf_avg(conf_ls):
    N_conf = len(conf_ls)
    mean = np.mean(conf_ls, axis=0)
    cov = np.cov(conf_ls, rowvar=False) * (N_conf - 1)

    return gv.gvar(mean, cov)

def jk_dic_avg(dic):
    l_dic = {}
    for key in dic:
        l_dic[key] = len(dic[key][0])

    conf_ls = []
    for n_conf in range(len(dic[key])):
        temp = []
        for key in dic:
            temp.append(list(dic[key][n_conf]))

        conf_ls.append( sum(temp, []) ) ## flat

    gv_ls = list(jk_conf_avg(conf_ls))
    
    gv_dic = {}
    for key in l_dic:
        gv_dic[key] = []
        for i in range(l_dic[key]):
            temp = gv_ls.pop(0)
            gv_dic[key].append(temp)

    return gv_dic