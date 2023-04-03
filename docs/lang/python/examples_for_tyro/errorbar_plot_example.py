# %%
from head_for_plot import *

### data
x = np.random.rand(100) * 10 + 1 
x = np.array(sorted(x)) # sort

y1 = 1.0/x
y1_err = np.random.rand(len(x))/10

y2 = 2.0/x
y2_err = np.random.rand(len(x))/5

y_ls = [y1, y2]
yerr_ls = [y1_err, y2_err]
label_ls = [r'P_z = 1', r'P_z = 2']

### labels
x_label = r"${\rm \lambda = z P_z}$"
m_label = r"$m_{\rm eff}$"

### plot
fig = plt.figure(figsize=fig_size)
ax = plt.axes(plt_axes)

for i in range(2):
    ax.errorbar(x, y_ls[i], yerr=yerr_ls[i], color=color_list[i], marker=fmt_ls[i], label=label_ls[i], **errorb)
ax.axvline(5, 0.1, 0.4, color='b', linestyle='dashdot', label='v line') # 竖直线
ax.axhline(0.1, color=grey, lw=0.5) # 水平线, lw 是粗细

ax.set_yticks([-0.5, 0, 0.5, 1]) # y 轴显示哪些刻度

ax.set_ylabel(m_label, **fs_p)
ax.set_xlabel(x_label, **fs_p)
ax.set_title('Plot test', font) # font 里设置了字体 Times New Roman
ax.set_ylim([-0.6, 1.2])
ax.legend(loc='upper right')

ax.tick_params(direction='in', top='on', right='on', **ls_p) # direction='in' 表示刻度线朝内, top='on', right='on' 表示上侧和右侧也显示刻度线

ax.grid(linestyle=':')
# plt.savefig('test.pdf' , transparent=True) ### save the plot locally
plt.show()

# %%
