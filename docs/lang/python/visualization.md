# 数据可视化指南

数据可视化是科研工作中的重要环节，好的图表能够清晰地传达研究结果。本指南介绍使用Python进行科学数据可视化的最佳实践。

## Matplotlib 基础

### 基本绘图流程

```python
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制数据
ax.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# 设置标签和标题
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Simple Plot Example', fontsize=16)

# 添加图例和网格
ax.legend()
ax.grid(True, alpha=0.3)

# 保存和显示
plt.tight_layout()
plt.savefig('plot.pdf', dpi=300, bbox_inches='tight')
plt.show()
```

### 图形元素说明

- **Figure (图形):** 整个图像窗口
- **Axes (坐标轴):** 图中的一个绘图区域
- **Axis (轴):** 坐标轴（x轴、y轴）
- **Artist:** 图中所有可见元素的基类

## 常用图表类型

### 1. 折线图 (Line Plot)

适用于展示连续变化的数据：

```python
fig, ax = plt.subplots()

# 多条曲线
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2, linestyle='--')

# 样式选项
# 线型: '-' (实线), '--' (虚线), '-.' (点划线), ':' (点线)
# 标记: 'o' (圆圈), 's' (方块), '^' (三角), 'D' (菱形)
ax.plot(x, np.tan(x), 'r:', marker='o', markersize=3, 
        markevery=10, label='tan(x)')

ax.legend()
plt.show()
```

### 2. 散点图 (Scatter Plot)

适用于展示两个变量之间的关系：

```python
# 生成随机数据
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

fig, ax = plt.subplots()

# 基本散点图
ax.scatter(x, y, alpha=0.6, edgecolors='k', linewidth=0.5)

# 带颜色和大小映射的散点图
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

plt.colorbar(ax.collections[0], label='Color value')
plt.show()
```

### 3. 误差棒图 (Error Bar Plot)

科研中最常用的图表类型，用于展示带误差的数据：

```python
x = np.arange(0, 10, 1)
y = np.exp(-x/5.0)
yerr = 0.1 + 0.1 * np.random.rand(len(x))

fig, ax = plt.subplots()

# 对称误差棒
ax.errorbar(x, y, yerr=yerr, fmt='o-', capsize=5, 
            capthick=2, label='Data with error')

# 非对称误差棒
yerr_lower = 0.05 + 0.05 * np.random.rand(len(x))
yerr_upper = 0.1 + 0.1 * np.random.rand(len(x))
ax.errorbar(x, y*0.8, yerr=[yerr_lower, yerr_upper], 
            fmt='s--', capsize=5, label='Asymmetric error')

ax.legend()
plt.show()
```

### 4. 柱状图 (Bar Chart)

适用于比较不同类别的数据：

```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 45]
errors = [3, 5, 4, 6, 5]

fig, ax = plt.subplots()

# 垂直柱状图
bars = ax.bar(categories, values, yerr=errors, 
              capsize=5, alpha=0.7, color='skyblue', 
              edgecolor='navy')

# 水平柱状图
# ax.barh(categories, values, xerr=errors)

ax.set_ylabel('Value')
ax.set_title('Bar Chart Example')
plt.show()
```

### 5. 直方图 (Histogram)

适用于展示数据的分布：

```python
# 生成正态分布数据
data = np.random.normal(0, 1, 1000)

fig, ax = plt.subplots()

# 绘制直方图
n, bins, patches = ax.hist(data, bins=30, alpha=0.7, 
                           color='skyblue', edgecolor='black')

# 添加拟合曲线
from scipy import stats
mu, sigma = stats.norm.fit(data)
x = np.linspace(data.min(), data.max(), 100)
ax.plot(x, stats.norm.pdf(x, mu, sigma) * len(data) * (bins[1] - bins[0]),
        'r-', linewidth=2, label=f'Normal fit: μ={mu:.2f}, σ={sigma:.2f}')

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()
plt.show()
```

### 6. 箱线图 (Box Plot)

适用于展示数据的分布和异常值：

```python
# 生成多组数据
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

fig, ax = plt.subplots()

# 绘制箱线图
bp = ax.boxplot(data, labels=['A', 'B', 'C', 'D'],
                patch_artist=True, notch=True)

# 自定义颜色
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')

ax.set_ylabel('Values')
plt.show()
```

### 7. 热图 (Heatmap)

适用于展示矩阵数据：

```python
# 生成相关系数矩阵
data = np.random.rand(10, 10)
corr = np.corrcoef(data)

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制热图
im = ax.imshow(corr, cmap='coolwarm', aspect='auto',
               vmin=-1, vmax=1)

# 添加颜色条
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Correlation', rotation=270, labelpad=15)

# 添加数值标注
for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        text = ax.text(j, i, f'{corr[i, j]:.2f}',
                      ha="center", va="center", color="black", fontsize=8)

ax.set_title('Correlation Matrix')
plt.show()
```

### 8. 等高线图 (Contour Plot)

适用于展示三维数据在二维平面的投影：

```python
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 填充等高线图
cs1 = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(cs1, ax=ax1)
ax1.set_title('Filled Contour')

# 线条等高线图
cs2 = ax2.contour(X, Y, Z, levels=10, colors='black')
ax2.clabel(cs2, inline=True, fontsize=8)
ax2.set_title('Line Contour')

plt.show()
```

## 发表级图表设置

### 标准配置模板

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

# 全局设置
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 6

# 刻度设置
mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.major.width'] = 1.5
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['xtick.minor.width'] = 1
mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.major.width'] = 1.5
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['ytick.minor.width'] = 1

# 图例设置
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['legend.fontsize'] = 10

# 图形尺寸 (符合期刊要求)
# 单栏图: 3.5 inches (89 mm)
# 双栏图: 7.0 inches (178 mm)
fig_width_single = 3.5
fig_width_double = 7.0
golden_ratio = 1.618

fig, ax = plt.subplots(figsize=(fig_width_double, fig_width_double/golden_ratio))
```

### 颜色方案

```python
# 色盲友好的配色方案
color_blind_friendly = [
    '#0173B2',  # 蓝色
    '#DE8F05',  # 橙色
    '#029E73',  # 绿色
    '#CC78BC',  # 粉色
    '#CA9161',  # 棕色
    '#949494',  # 灰色
]

# 使用示例
for i, color in enumerate(color_blind_friendly):
    ax.plot(x, y + i, color=color, label=f'Line {i+1}')
```

### 保存高质量图片

```python
# 矢量格式 (推荐用于论文)
plt.savefig('figure.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.savefig('figure.eps', format='eps', dpi=300, bbox_inches='tight')

# 位图格式 (用于演示文稿)
plt.savefig('figure.png', format='png', dpi=300, bbox_inches='tight', transparent=True)

# 压缩PDF (减小文件大小)
plt.savefig('figure.pdf', format='pdf', dpi=300, bbox_inches='tight',
            metadata={'Creator': '', 'Producer': '', 'CreationDate': None})
```

## 子图布局

### 规则网格

```python
# 方法1: plt.subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for i, ax in enumerate(axes.flat):
    ax.plot(x, np.sin(x + i))
    ax.set_title(f'Subplot {i+1}')
    
plt.tight_layout()
```

### 不规则网格

```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(3, 3)

# 占据不同大小的区域
ax1 = fig.add_subplot(gs[0, :])  # 第一行，全部列
ax2 = fig.add_subplot(gs[1:, 0]) # 第二、三行，第一列
ax3 = fig.add_subplot(gs[1:, 1:])# 第二、三行，第二、三列

ax1.plot(x, y)
ax2.plot(x, y)
ax3.plot(x, y)

plt.tight_layout()
```

## 进阶技巧

### 双Y轴

```python
fig, ax1 = plt.subplots()

# 第一个Y轴
color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color=color)
ax1.plot(x, np.sin(x), color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 第二个Y轴
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('exp(x)', color=color)
ax2.plot(x, np.exp(x/5), color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.tight_layout()
plt.show()
```

### 插图 (Inset)

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots()
ax.plot(x, y)

# 创建插图
axins = inset_axes(ax, width="40%", height="40%", loc='upper right')
axins.plot(x, y)
axins.set_xlim(2, 4)
axins.set_ylim(-0.5, 0.5)
```

### 注释和箭头

```python
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))

# 添加文本注释
ax.text(5, 0.5, 'Peak', fontsize=12)

# 添加箭头注释
ax.annotate('Local maximum', 
            xy=(np.pi/2, 1), xytext=(3, 1.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2',
                          facecolor='black', shrink=0.05),
            fontsize=12, ha='center')

plt.show()
```

### 对数坐标

```python
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(16, 4))

x = np.logspace(0, 3, 50)
y = x**2

ax1.plot(x, y)
ax1.set_title('Linear scale')

ax2.plot(x, y)
ax2.set_xscale('log')
ax2.set_title('Log x scale')

ax3.plot(x, y)
ax3.set_yscale('log')
ax3.set_title('Log y scale')

ax4.plot(x, y)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.set_title('Log-log scale')

plt.tight_layout()
```

## 动画

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x + i/10)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                    frames=100, interval=50, blit=True)

# 保存为GIF
anim.save('animation.gif', writer='pillow', fps=20)
plt.show()
```

## Seaborn 高级可视化

Seaborn是基于Matplotlib的统计绘图库，提供了更美观的默认样式：

```python
import seaborn as sns

# 设置样式
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.5)

# 配对图 (适合多变量分析)
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species')

# 小提琴图
fig, ax = plt.subplots()
sns.violinplot(data=iris, x='species', y='sepal_length', ax=ax)

# 热图
corr = iris.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
```

## 实用资源

- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Python Graph Gallery](https://python-graph-gallery.com/)
- [科学配色方案](https://www.fabiocrameri.ch/colourmaps/)

## 常见错误及解决方案

### 中文显示问题

```python
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
```

### 图例遮挡数据

```python
# 将图例放在图外
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 或使用最佳位置
ax.legend(loc='best')
```

### 保存后图片被裁剪

```python
# 使用 bbox_inches='tight'
plt.savefig('figure.pdf', bbox_inches='tight')
```
