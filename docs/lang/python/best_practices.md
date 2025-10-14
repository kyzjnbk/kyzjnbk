# Python 最佳实践

本文总结了科研编程中的Python最佳实践，帮助你写出更清晰、更高效、更易维护的代码。

## 代码风格

### 遵循 PEP 8 规范

PEP 8 是Python的官方代码风格指南，遵循它可以让你的代码更易读。

```python
# 好的风格
def calculate_average(data_list):
    """计算列表的平均值"""
    if not data_list:
        return 0
    return sum(data_list) / len(data_list)

# 不好的风格
def calcAvg(d):
    return sum(d)/len(d)
```

**关键规则：**
- 使用4个空格缩进（不要用Tab）
- 每行代码不超过79个字符
- 函数名使用小写字母加下划线
- 类名使用驼峰命名法
- 常量使用全大写

### 添加文档字符串

为函数和类添加文档字符串，说明功能、参数和返回值：

```python
def fit_data(x, y, degree=2):
    """
    对数据进行多项式拟合
    
    Parameters
    ----------
    x : array_like
        自变量数据
    y : array_like
        因变量数据
    degree : int, optional
        多项式的阶数，默认为2
        
    Returns
    -------
    coefficients : ndarray
        拟合系数，从高次到低次排列
        
    Examples
    --------
    >>> x = np.array([1, 2, 3, 4])
    >>> y = np.array([1, 4, 9, 16])
    >>> fit_data(x, y, degree=2)
    array([1., 0., 0.])
    """
    return np.polyfit(x, y, degree)
```

## 数据处理最佳实践

### 使用 NumPy 进行向量化操作

避免使用循环，使用NumPy的向量化操作提升性能：

```python
import numpy as np

# 慢速方法（使用循环）
result = []
for i in range(len(data)):
    result.append(data[i] ** 2)

# 快速方法（向量化）
result = data ** 2
```

**性能对比：** 向量化操作通常比循环快10-100倍！

### 合理使用 Pandas

处理表格数据时，Pandas是最佳选择：

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')

# 数据清洗
df = df.dropna()  # 删除缺失值
df = df[df['value'] > 0]  # 过滤数据

# 分组统计
grouped = df.groupby('category').mean()

# 保存结果
df.to_csv('cleaned_data.csv', index=False)
```

### 错误处理

使用异常处理增强代码健壮性：

```python
def load_data(filename):
    """安全地加载数据文件"""
    try:
        data = np.loadtxt(filename)
        return data
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None
    except ValueError as e:
        print(f"错误：数据格式不正确 - {e}")
        return None
```

## 科学计算技巧

### 处理带误差的数据

使用 `gvar` 库处理带误差的物理量：

```python
import gvar as gv

# 创建带误差的变量
mass = gv.gvar(1.5, 0.1)  # 1.5 ± 0.1
energy = gv.gvar(2.0, 0.15)  # 2.0 ± 0.15

# 误差会自动传播
momentum = gv.sqrt(energy**2 - mass**2)
print(momentum)  # 输出包含误差的结果
```

### 数值拟合最佳实践

```python
import numpy as np
import lsqfit as lsf
import gvar as gv

def fit_with_priors(x, y, func):
    """
    使用先验信息进行贝叶斯拟合
    
    这种方法在数据点较少或噪声较大时特别有用
    """
    # 设置合理的先验
    prior = {
        'a': gv.gvar(0, 10),  # 参数a的先验：0 ± 10
        'b': gv.gvar(0, 10),  # 参数b的先验：0 ± 10
    }
    
    # 执行拟合
    fit = lsf.nonlinear_fit(data=(x, y), fcn=func, prior=prior)
    
    return fit

# 使用示例
def model(x, p):
    return p['a'] * x + p['b']

x = np.array([1, 2, 3, 4, 5])
y = gv.gvar([2.1, 3.9, 6.2, 7.8, 10.1], [0.3, 0.3, 0.3, 0.3, 0.3])
result = fit_with_priors(x, y, model)
print(result)
```

## 绘图技巧

### 制作发表级别的图表

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置全局参数
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['xtick.major.width'] = 1.5
plt.rcParams['ytick.major.width'] = 1.5

# 创建图形
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制数据
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

ax.plot(x, y1, 'o-', label='sin(x)', linewidth=2, markersize=4)
ax.plot(x, y2, 's--', label='cos(x)', linewidth=2, markersize=4)

# 设置标签和标题
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Trigonometric Functions', fontsize=16)

# 添加网格和图例
ax.grid(True, alpha=0.3)
ax.legend(frameon=False, fontsize=12)

# 调整布局并保存
plt.tight_layout()
plt.savefig('figure.pdf', dpi=300, bbox_inches='tight')
plt.show()
```

### 子图布局

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 展平axes数组便于迭代
axes = axes.flatten()

for i, ax in enumerate(axes):
    ax.plot(x, y[i])
    ax.set_title(f'Subplot {i+1}')
    
plt.tight_layout()
plt.savefig('subplots.pdf')
```

## 代码优化

### 使用生成器节省内存

处理大数据集时，使用生成器而不是列表：

```python
# 内存效率低
def read_all_data(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

# 内存效率高
def read_data_generator(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# 使用
for line in read_data_generator('large_file.txt'):
    process(line)
```

### 使用 Numba 加速计算

对于计算密集型循环，使用Numba JIT编译：

```python
from numba import jit
import numpy as np

@jit(nopython=True)
def monte_carlo_pi(n_samples):
    """使用蒙特卡洛方法估算π"""
    count = 0
    for i in range(n_samples):
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / n_samples

# 加速后的函数运行速度提升10-100倍
result = monte_carlo_pi(1000000)
```

## 项目组织

### 推荐的项目结构

```
my_research_project/
├── data/               # 原始数据
│   ├── raw/
│   └── processed/
├── notebooks/          # Jupyter notebooks
├── src/                # 源代码
│   ├── __init__.py
│   ├── data_processing.py
│   ├── analysis.py
│   └── plotting.py
├── tests/              # 测试代码
│   └── test_analysis.py
├── results/            # 结果输出
│   ├── figures/
│   └── tables/
├── requirements.txt    # 依赖列表
└── README.md          # 项目说明
```

### 使用虚拟环境

为每个项目创建独立的虚拟环境：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 导出当前环境的依赖
pip freeze > requirements.txt
```

## 版本控制

### Git 最佳实践

```bash
# 创建 .gitignore 文件
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore
echo "venv/" >> .gitignore
echo "data/raw/" >> .gitignore  # 不提交原始数据

# 有意义的提交信息
git commit -m "Add data preprocessing module"
git commit -m "Fix: Correct error in fit function"
git commit -m "Update: Improve plotting style"

# 使用分支进行开发
git checkout -b feature/new-analysis
```

## 测试

### 编写简单的测试

```python
# test_analysis.py
import numpy as np
from src.analysis import calculate_average

def test_calculate_average():
    """测试平均值计算函数"""
    data = np.array([1, 2, 3, 4, 5])
    result = calculate_average(data)
    expected = 3.0
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

def test_calculate_average_empty():
    """测试空列表的情况"""
    data = np.array([])
    result = calculate_average(data)
    assert result == 0, "Empty list should return 0"

# 运行测试
# pytest test_analysis.py
```

## 常见陷阱

### 1. 浮点数比较

```python
# 错误
if a == b:
    pass

# 正确
import numpy as np
if np.isclose(a, b):
    pass
```

### 2. 可变默认参数

```python
# 错误
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# 正确
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 3. 深拷贝 vs 浅拷贝

```python
import copy

# 浅拷贝 - 只复制引用
list2 = list1
list2[0] = 100  # list1 也会改变！

# 深拷贝 - 完全独立的副本
list2 = copy.deepcopy(list1)
list2[0] = 100  # list1 不受影响
```

## 参考资源

- [PEP 8 风格指南](https://www.python.org/dev/peps/pep-0008/)
- [Google Python 风格指南](https://google.github.io/styleguide/pyguide.html)
- [NumPy 文档](https://numpy.org/doc/)
- [SciPy 文档](https://docs.scipy.org/doc/scipy/)
- [Matplotlib 教程](https://matplotlib.org/stable/tutorials/index.html)

## 推荐工具

- **代码格式化:** `black`, `autopep8`
- **代码检查:** `pylint`, `flake8`
- **类型检查:** `mypy`
- **性能分析:** `cProfile`, `line_profiler`
- **交互式开发:** `IPython`, `Jupyter Lab`
