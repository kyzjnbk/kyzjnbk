# Python Examples for Beginners

这是一个为初学者准备的Python示例代码集合，涵盖了科研中常用的数据处理、绘图和数值计算技巧。

## 📁 文件说明

### 数据拟合与分析

- **`nonlinear_fit.py`** - 非线性拟合示例
  - 使用 `lsqfit` 库进行非线性最小二乘拟合
  - 演示如何使用 `gvar` 处理带误差的数据
  - 包含 bootstrap 重采样方法

- **`plot_and_fit.py`** - 数据绘图与多项式拟合
  - 使用 `matplotlib` 进行数据可视化
  - 多项式拟合 (`numpy.polyfit`)
  - 两种不同的绘图风格示例

- **`three_point_correlation_fit.py`** - 三点关联函数拟合
  - 联合拟合多组数据（2pt, ratio, fh）
  - 先验概率设置与贝叶斯推断
  - 适用于格点QCD等领域的数据分析

### 数据处理

- **`bootstrap.py`** - Bootstrap 重采样方法
  - 从相关数据生成独立样本
  - 误差估计与统计分析

- **`resampling_and_error_estimation.py`** - 重采样与误差估计
  - 多种重采样技术对比
  - 系统误差与统计误差的处理

- **`gvar_to_samples.py`** - gvar 数据格式转换
  - 将高斯分布变量转换为样本数据
  - 用于蒙特卡洛模拟

### 绘图示例

- **`errorbar_plot_example.py`** - 误差棒绘图
  - 专业的误差图绘制方法
  - 适合论文发表的图表格式

- **`head_for_plot.py`** - 绘图模板与样式设置
  - 标准化的绘图参数配置
  - 符合学术出版要求的图表格式

- **`3d_plot_example.py`** - 三维数据可视化
  - 使用 `matplotlib` 绘制3D图形
  - 曲面图、等高线图等

### 数值计算

- **`Monte_Carlo.py`** - 蒙特卡洛方法
  - 随机采样与数值积分
  - 统计模拟基础

- **`FT_fast.py`** - 快速傅里叶变换
  - 使用 `numpy.fft` 进行频谱分析
  - 信号处理基础

- **`correlation_in_nonlinear_fit.py`** - 关联数据的非线性拟合
  - 处理数据点之间的关联性
  - 协方差矩阵的应用

### 其他工具

- **`calc_class.py`** - 计算器类示例
  - 面向对象编程入门
  - 类的定义与使用

- **`vmgirls.py`** - 网页爬虫示例
  - 图片下载与批量处理
  - 实用的爬虫技巧

## 🔧 依赖库

大多数示例需要以下Python库：

```bash
pip install numpy matplotlib scipy gvar lsqfit
```

## 📚 学习路径建议

### 初学者路径
1. 从 `plot_and_fit.py` 开始学习基本的数据绘图
2. 学习 `calc_class.py` 了解面向对象编程
3. 尝试 `Monte_Carlo.py` 理解随机模拟

### 进阶路径
1. 学习 `bootstrap.py` 掌握重采样技术
2. 研究 `nonlinear_fit.py` 学习专业数据拟合
3. 挑战 `three_point_correlation_fit.py` 处理复杂数据分析

## 💡 使用建议

- 每个脚本都可以独立运行，建议逐个学习
- 修改代码中的参数，观察结果变化来加深理解
- 将这些示例代码改编用于自己的科研项目
- 遇到不懂的函数，查阅官方文档深入学习

## 🔗 相关资源

- [NumPy 官方文档](https://numpy.org/doc/)
- [Matplotlib 官方文档](https://matplotlib.org/)
- [lsqfit 文档](https://lsqfit.readthedocs.io/)
- [gvar 文档](https://gvar.readthedocs.io/)

## 📝 参考文献

在科研论文中使用这些方法时，建议引用相关的软件包：

- G.P. Lepage, "gvar: A Python package for uncertain variables", DOI: 10.5281/zenodo.1037448
- G.P. Lepage, "lsqfit: Nonlinear least-squares fitting", DOI: 10.5281/zenodo.1037449
