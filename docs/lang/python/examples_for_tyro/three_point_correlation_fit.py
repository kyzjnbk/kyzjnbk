# %%
'''
Useful in lattice QCD research

Feynman-Hellmann method and ratio method to fit the ground state matrix element with three-point correlation function.
'''

import gvar as gv
import lsqfit as lsf
import numpy as np

class FIT():
    def __init__(self, fit_2pt, fit_ratio, fit_fh):
        '''
        三个变量控制 2pt，ratio，fh 是否纳入拟合，比如 fit_2pt=True, fit_fh=True 就是 2pt+fh 的 joint fit
        '''
        self.fit_2pt = fit_2pt
        self.fit_ratio = fit_ratio
        self.fit_fh = fit_fh
        return

    def main(self, pt2_t, ra_tseq, ra_t, fh_t1, fh_t2, pt2, ra_re, ra_im, fh_re, fh_im):
        '''
        pt2_t：2pt 的自变量
        ra_tseq：3pt 的 tseq
        ra_t：3pt 的插入流时间
        fh_t1 和 fh_t2：因为 FH 需要 ( sum(tseq=t2) - sum(tseq=t1) ) / (t2 - t1)，所以需要两组自变量，不过现在这个 fit function 用不到 fh_t2

        pt2：2pt 的因变量
        ra_re, ra_im：ratio 因变量的实虚部
        fh_re, fh_im：fh 因变量的实虚部
        '''

        priors = self.pri()

        x = {}
        y = gv.BufferDict()
        if self.fit_2pt == True:
            x['2pt'] = pt2_t
            y['2pt'] = pt2

        if self.fit_ratio == True:
            x['ra_re'] = [ra_tseq, ra_t]
            y['ra_re'] = ra_re
            x['ra_im'] = [ra_tseq, ra_t]
            y['ra_im'] = ra_im

        if self.fit_fh == True: 
            x['fh_re'] = fh_t1
            y['fh_re'] = fh_re
            x['fh_im'] = fh_t1
            y['fh_im'] = fh_im

        fit_result = lsf.nonlinear_fit(data=(x, y), prior=priors, fcn=self.fcn, maxit=10000, svdcut=1e-100, fitter='scipy_least_squares')

        return fit_result
    
    def pt2_fcn(self, pt2_t, p):
        e1 = p['E0'] + p['dE1']

        val = p['z0'] * p['z0'] * np.exp(-p['E0']*pt2_t)
        val += p['z1'] * p['z1'] * np.exp(-e1 * pt2_t)

        return val

    def ra_re_fcn(self, ra_tseq, ra_t, p):
        de = p['dE1']

        val = p['pdf_re'] + p['re_r1'] * ( np.exp( -de * (ra_tseq - ra_t) ) + np.exp( -de * ra_t ) ) + p['re_r2'] * np.exp(-de * ra_tseq)

        return val

    def ra_im_fcn(self, ra_tseq, ra_t, p):
        de = p['dE1']

        val = p['pdf_im'] + p['im_r1'] * ( np.exp( -de * (ra_tseq - ra_t) ) + np.exp( -de * ra_t ) ) + p['im_r2'] * np.exp(-de * ra_tseq)

        return val

    def fh_re_fcn(self, fh_t, p):
        de = p['dE1']

        val = p['pdf_re'] + p['re_f1'] * np.exp(-de * fh_t) + p['re_f2'] * fh_t * np.exp(-de * fh_t)

        return val

    def fh_im_fcn(self, fh_t, p):
        de = p['dE1']

        val = p['pdf_im'] + p['im_f1'] * np.exp(-de * fh_t) + p['im_f2'] * fh_t * np.exp(-de * fh_t)

        return val
        
    def pri(self):
        priors = gv.BufferDict()
        priors['E0'] = gv.gvar(1, 10)
        priors['log(dE1)'] = gv.gvar(0, 10)

        priors['z0'] = gv.gvar(1, 10)
        priors['z1'] = gv.gvar(1, 10)

        priors['pdf_re'] = gv.gvar(1, 10)
        priors['pdf_im'] = gv.gvar(1, 10)

        priors['re_r1'] = gv.gvar(1, 10)
        priors['re_r2'] = gv.gvar(1, 10)
        priors['im_r1'] = gv.gvar(1, 10)
        priors['im_r2'] = gv.gvar(1, 10)

        priors['re_f1'] = gv.gvar(1, 10)
        priors['re_f2'] = gv.gvar(1, 10)
        priors['im_f1'] = gv.gvar(1, 10)
        priors['im_f2'] = gv.gvar(1, 10)

        return priors

    def fcn(self, x, p):
        ## x 是 dict，x['ra_re'] = [tseq list, current_t list] ##

        val = {}
        ###
        if self.fit_2pt == True:
            val['2pt'] = self.pt2_fcn(x['2pt'], p)
        ###
        if self.fit_ratio == True:
            val['ra_re'] = []
            val['ra_im'] = []
            for idx in range(len(x['ra_re'][0])):
                tseq = x['ra_re'][0][idx] #! tseq
                tau = x['ra_re'][1][idx] #! 插入流时间
                val['ra_re'].append( self.ra_re_fcn(tseq, tau, p) )

                tseq = x['ra_im'][0][idx]
                tau = x['ra_im'][1][idx]
                val['ra_im'].append( self.ra_im_fcn(tseq, tau, p) )
        ###
        if self.fit_fh == True:
            val['fh_re'] = []
            val['fh_im'] = []
            for idx in range(len(x['fh_re'])):
                t1 = x['fh_re'][idx]
                val['fh_re'].append( self.fh_re_fcn(t1, p) )

                t1 = x['fh_im'][idx]
                val['fh_im'].append( self.fh_im_fcn(t1, p) )

        return val

if __name__ == '__main__':
    pass


fit = FIT(fit_2pt=True, fit_ratio=False, fit_fh=True) #! 2pt+fh joint fit

## 2pt ##
pt2_t = np.arange(1, 10)
pt2 = [gv.gvar(1, 0.5) for i in range(1, 10)] #! 输入数据

## ratio ##
ra_tseq = []
ra_t = []
ra_re = []
ra_im = []
for tseq in range(10):
    for t in range(1, tseq): # 插入流从 1 到 tseq-1
        ra_tseq.append(tseq)
        ra_t.append(t)
        val_re = gv.gvar(1, 0.5) #! 输入数据
        val_im = gv.gvar(1, 0.5) #! 输入数据
        ra_re.append(val_re)
        ra_im.append(val_im)

## fh ##
fh_t1 = np.arange(1, 8) # tseq 2~8 - tseq 1~7
fh_t2 = np.arange(2, 9)
fh_re = [gv.gvar(1, 0.5) for i in range(1, 8)] #! 输入数据
fh_im = [gv.gvar(1, 0.5) for i in range(1, 8)] #! 输入数据

fit_res = fit.main(pt2_t, ra_tseq, ra_t, fh_t1, fh_t2, pt2, ra_re, ra_im, fh_re, fh_im)
print(fit_res.format(100))