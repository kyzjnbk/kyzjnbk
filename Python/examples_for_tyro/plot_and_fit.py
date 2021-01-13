# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# data

num = 100 # number of data points

x = np.random.rand(num) * 10 + 1 
x = np.array(sorted(x))
y = 1.0/x

# %%
# plot

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

f = np.polyfit(x, y, n)
print(f)
p = np.poly1d(f)
print("fit func is \n", p)

fit = f[n]

for i in range(n):
    fit += f[i] * x**(n-i)

# %%
# plot fit on data

plt.figure()
plt.scatter(x, y, c='blue', marker='x')
plt.plot(x, fit, 'r-')
plt.grid()
plt.minorticks_on()
plt.xlabel('t')
plt.ylabel('meff')
plt.ylim([0,1])
plt.xlim([0,11])
plt.legend()
plt.show()
