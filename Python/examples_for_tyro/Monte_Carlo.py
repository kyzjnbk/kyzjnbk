# %%
import numpy as np
import matplotlib.pyplot as plt 

# %%
n = 10000 # num of throw

# def a circle
r = 1 # radius
a = 0 # center
b = 0


# def a rectangular
x_min, x_max = a-r, a+r
y_min, y_max = b-r, b+r

# random throw in the rectangular
x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

# calc distance between throw and center of the circle
d = np.sqrt((x-a)**2 + (y-b)**2)

# num of throw in the circle

############## method 1 ###############
#res = sum(np.where(d<r, 1, 0))

#######################################
############## method 2 ###############
res=0

for i in range(len(d)):
    if d[i] < r:
        res += 1

#######################################

# calc value of pi
pi = 4 * res / n
print('approximate value of pi: ', pi)

# %%
plt.figure()
plt.plot(x, y, 'ro', markersize=1)
plt.axis('equal')

x_c = np.linspace(-r, r, 1000)
y_c = (r**2 - x_c**2)**(0.5)
plt.plot(x_c, y_c, 'b-')
plt.plot(x_c, -y_c, 'b-')

plt.show()