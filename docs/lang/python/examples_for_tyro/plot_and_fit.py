# %%

'''
An example of poly fit and Two methods of plot
'''

import numpy as np
import matplotlib.pyplot as plt

# %%
# data

num = 100 # number of data points

x = np.random.rand(num) * 10 + 1 
x = np.array(sorted(x))
y = 1.0/x

print(np.random.rand(10)/100)

# %%
# data plot
## First method

plt.figure()
plt.scatter(x, y, color='blue')
plt.grid()
plt.minorticks_on()
plt.xlabel('t')
plt.ylabel('meff')
plt.ylim([0,1])
plt.xlim([0,11])
plt.legend()
plt.show()
# %%
# fit

n = 7 # order of ployfit

f = np.polyfit(x, y, n) # 系数列表
print(f)

p = np.poly1d(f)

print("fit func is \n", p)

fit = f[n] # res = c

for i in range(n):
    fit += f[i] * x**(n-i) # res = res + b * x; res = res + a * x**2

# %%
# plot fit on data
## Second method

### head
fig_width = 6.75 # in inches, 2x as wide as APS column
gr        = 1.618034333 # golden ratio
fig_size  = (fig_width, fig_width / gr)
plt_axes = [0.1,0.12,0.85,0.8]

errorb = {"markersize": 5, "mfc": "none", "linestyle": "none", "capsize": 3, "elinewidth": 1} # circle
errorl = {"markersize": 5, "mfc": "none", "capsize": 3, "elinewidth": 1} # circle with line
fs_p = {"fontsize": 13} # font size of text, label, ticks
ls_p = {"labelsize": 13}

grey = "#808080" 
red = "#FF6F6F" 
peach = "#FF9E6F" 
orange = "#FFBC6F" 
sunkist = "#FFDF6F"
yellow = "#FFEE6F"
lime = "#CBF169"
green = "#5CD25C" 
turquoise = "#4AAB89"
blue = "#508EAD" 
grape = "#635BB1"
violet = "#7C5AB8" 
fuschia = "#C3559F"

color_ls = ['orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green','orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green']
fmt_ls = ['o', 'D', 's', '^', 'x', '.']

#### labels
x_label = r"$x$"
m_label = r"$m_{\rm eff}$"


### plot
fig = plt.figure(figsize=fig_size)
ax = plt.axes(plt_axes)
my_err = np.random.rand(len(x))/100
ax.errorbar(x, y, yerr=my_err, color=color_ls[0], marker='D', label='data with err', **errorb)
ax.plot(x, fit, 'r-', label='fit')
ax.axvline(5, 0.1, 0.4, color='b', linestyle='dashdot', label='v line')
ax.set_xlabel(x_label, **fs_p)
ax.set_title('Plot test')
ax.set_ylim([0, 1])
ax.legend(loc='upper right')
ax.tick_params(direction='in', **ls_p)
ax.grid(linestyle=':')
# plt.savefig('test.pdf' , transparent=True) ### save the plot locally
plt.show()
# %%
