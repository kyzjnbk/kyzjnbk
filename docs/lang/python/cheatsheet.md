# Python 速查表

快速查找常用的Python语法和函数。

## 基础语法

### 变量与数据类型

```python
# 基本类型
integer = 42
floating = 3.14
string = "Hello"
boolean = True
none_type = None

# 类型检查和转换
type(42)           # <class 'int'>
isinstance(42, int)  # True
int("42")          # 42
float("3.14")      # 3.14
str(42)            # "42"
```

### 运算符

```python
# 算术运算符
+ - * / // % **

# 比较运算符
== != > < >= <=

# 逻辑运算符
and or not

# 成员运算符
in    # 在序列中
not in  # 不在序列中

# 身份运算符
is    # 是同一个对象
is not  # 不是同一个对象
```

### 字符串操作

```python
s = "Hello World"

# 常用方法
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.strip()           # 去除首尾空格
s.replace('o', '0') # "Hell0 W0rld"
s.split()           # ['Hello', 'World']
'_'.join(['a','b']) # "a_b"
s.startswith('He')  # True
s.endswith('ld')    # True
s.find('World')     # 6
s.count('l')        # 3

# 格式化
f"Value: {x}"       # f-string
"Value: {}".format(x)
"Value: %d" % x
```

## 数据结构

### 列表 (List)

```python
# 创建
lst = [1, 2, 3]
lst = list(range(5))

# 操作
lst.append(4)       # 添加元素
lst.extend([5, 6])  # 扩展列表
lst.insert(0, 0)    # 插入元素
lst.remove(3)       # 删除元素（按值）
lst.pop()           # 删除并返回最后一个元素
lst.pop(0)          # 删除并返回指定位置元素
lst.sort()          # 排序（就地）
sorted(lst)         # 排序（返回新列表）
lst.reverse()       # 反转（就地）
lst[::-1]           # 反转（返回新列表）
len(lst)            # 长度
lst.index(2)        # 查找元素索引
lst.count(3)        # 统计元素出现次数

# 切片
lst[1:4]   # 索引1到3
lst[:3]    # 前3个元素
lst[3:]    # 从索引3到末尾
lst[-3:]   # 最后3个元素
lst[::2]   # 每隔一个元素
lst[::-1]  # 反转
```

### 元组 (Tuple)

```python
# 创建（不可变）
tup = (1, 2, 3)
tup = 1, 2, 3
tup = tuple([1, 2, 3])

# 操作
len(tup)
tup[0]
tup.index(2)
tup.count(3)

# 解包
a, b, c = tup
```

### 字典 (Dict)

```python
# 创建
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)

# 操作
d['c'] = 3          # 添加/修改
del d['a']          # 删除
d.pop('b')          # 删除并返回值
d.get('a', default) # 获取值（带默认值）
d.keys()            # 所有键
d.values()          # 所有值
d.items()           # 所有键值对
d.update({'d': 4})  # 更新字典
'a' in d            # 检查键是否存在
len(d)              # 字典大小

# 遍历
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

### 集合 (Set)

```python
# 创建
s = {1, 2, 3}
s = set([1, 2, 3])

# 操作
s.add(4)            # 添加元素
s.remove(3)         # 删除元素（不存在会报错）
s.discard(3)        # 删除元素（不存在不报错）
s.pop()             # 删除并返回任意元素
s.clear()           # 清空集合
len(s)              # 集合大小

# 集合运算
a | b   # 并集
a & b   # 交集
a - b   # 差集
a ^ b   # 对称差集
```

## 控制流

### 条件语句

```python
if condition:
    pass
elif condition:
    pass
else:
    pass

# 三元运算符
result = value_if_true if condition else value_if_false
```

### 循环

```python
# for 循环
for item in iterable:
    pass

for i in range(10):
    pass

for i, item in enumerate(items):
    pass

# while 循环
while condition:
    pass

# 循环控制
break     # 跳出循环
continue  # 继续下一次迭代
else:     # 循环正常结束时执行
    pass
```

## 函数

```python
# 定义函数
def function_name(arg1, arg2, *args, **kwargs):
    """函数文档字符串"""
    return result

# lambda 函数
square = lambda x: x ** 2

# 默认参数
def func(x, y=10):
    pass

# 关键字参数
func(x=5, y=15)

# 可变参数
def func(*args):      # 位置参数元组
    pass

def func(**kwargs):   # 关键字参数字典
    pass
```

## 类

```python
class MyClass:
    # 类变量
    class_var = 0
    
    def __init__(self, x):
        # 实例变量
        self.x = x
    
    def method(self):
        return self.x
    
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    @staticmethod
    def static_method():
        return "static"
    
    def __str__(self):
        return f"MyClass({self.x})"
    
    def __repr__(self):
        return f"MyClass({self.x})"

# 继承
class Child(MyClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
```

## NumPy 速查

```python
import numpy as np

# 创建数组
np.array([1, 2, 3])
np.zeros((3, 3))
np.ones((3, 3))
np.eye(3)              # 单位矩阵
np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)   # [0, 0.25, 0.5, 0.75, 1]
np.random.rand(3, 3)   # 均匀分布随机数
np.random.randn(3, 3)  # 标准正态分布

# 数组属性
arr.shape    # 形状
arr.dtype    # 数据类型
arr.size     # 元素总数
arr.ndim     # 维度数

# 数组操作
arr.reshape(3, 3)
arr.flatten()
arr.transpose()
arr.T        # 转置

# 数学运算
np.sum(arr)
np.mean(arr)
np.std(arr)
np.min(arr)
np.max(arr)
np.sqrt(arr)
np.exp(arr)
np.log(arr)

# 线性代数
np.dot(a, b)         # 矩阵乘法
np.linalg.inv(A)     # 矩阵求逆
np.linalg.det(A)     # 行列式
np.linalg.eig(A)     # 特征值和特征向量
np.linalg.solve(A, b) # 求解线性方程组
```

## Pandas 速查

```python
import pandas as pd

# 创建
df = pd.DataFrame(data, columns=['A', 'B'])
s = pd.Series([1, 2, 3])

# 读取数据
pd.read_csv('file.csv')
pd.read_excel('file.xlsx')
pd.read_json('file.json')

# 查看数据
df.head()        # 前5行
df.tail()        # 后5行
df.info()        # 信息概要
df.describe()    # 统计描述
df.shape         # 形状
df.columns       # 列名
df.index         # 索引

# 选择数据
df['A']          # 选择列
df[['A', 'B']]   # 选择多列
df.loc[0]        # 按标签选择行
df.iloc[0]       # 按位置选择行
df.loc[0, 'A']   # 选择特定单元格

# 过滤数据
df[df['A'] > 0]
df.query('A > 0 and B < 10')

# 排序
df.sort_values('A')
df.sort_values(['A', 'B'], ascending=False)

# 分组聚合
df.groupby('A').mean()
df.groupby('A')['B'].sum()

# 合并数据
pd.concat([df1, df2])
pd.merge(df1, df2, on='key')

# 缺失值处理
df.dropna()           # 删除缺失值
df.fillna(0)          # 填充缺失值
df.isna()             # 检测缺失值

# 应用函数
df['A'].apply(lambda x: x**2)
df.apply(np.sum, axis=0)
```

## Matplotlib 速查

```python
import matplotlib.pyplot as plt

# 基本绘图
plt.plot(x, y)            # 折线图
plt.scatter(x, y)         # 散点图
plt.bar(x, y)             # 柱状图
plt.hist(data, bins=30)   # 直方图
plt.boxplot(data)         # 箱线图
plt.imshow(image)         # 图像显示

# 图形设置
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend()
plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 10)

# 子图
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax2.scatter(x, y)

# 保存和显示
plt.savefig('figure.pdf')
plt.show()
```

## 文件操作速查

```python
# 读取文件
with open('file.txt', 'r') as f:
    content = f.read()           # 读取全部
    lines = f.readlines()        # 读取所有行
    for line in f:               # 逐行读取
        pass

# 写入文件
with open('file.txt', 'w') as f:
    f.write('content')
    f.writelines(['line1\n', 'line2\n'])

# 文件模式
'r'   # 读取
'w'   # 写入（覆盖）
'a'   # 追加
'r+'  # 读写
'b'   # 二进制模式（如 'rb', 'wb'）
```

## 常用标准库

```python
# math
import math
math.sqrt(x)
math.sin(x)
math.cos(x)
math.pi
math.e

# random
import random
random.random()          # [0, 1)随机浮点数
random.randint(1, 10)    # 随机整数
random.choice([1,2,3])   # 随机选择
random.shuffle(lst)      # 随机打乱

# datetime
from datetime import datetime, timedelta
now = datetime.now()
date = datetime(2023, 1, 1)
delta = timedelta(days=7)
date_str = now.strftime('%Y-%m-%d')
date_obj = datetime.strptime('2023-01-01', '%Y-%m-%d')

# json
import json
json.dumps(obj)          # Python对象转JSON字符串
json.loads(json_str)     # JSON字符串转Python对象
json.dump(obj, file)     # 写入文件
json.load(file)          # 从文件读取

# re (正则表达式)
import re
re.search(pattern, string)
re.match(pattern, string)
re.findall(pattern, string)
re.sub(pattern, replacement, string)
```

## 异常处理

```python
try:
    # 可能出错的代码
    pass
except ValueError:
    # 处理特定异常
    pass
except (TypeError, KeyError):
    # 处理多个异常
    pass
except Exception as e:
    # 处理所有异常
    print(f"错误: {e}")
else:
    # 没有异常时执行
    pass
finally:
    # 总是执行
    pass

# 抛出异常
raise ValueError("错误信息")
```

## 常用内置函数

```python
abs(x)           # 绝对值
all(iterable)    # 所有元素为真
any(iterable)    # 任一元素为真
enumerate(lst)   # 返回索引和值
filter(func, lst) # 过滤
map(func, lst)   # 映射
max(lst)         # 最大值
min(lst)         # 最小值
range(n)         # 范围
reversed(lst)    # 反转
sorted(lst)      # 排序
sum(lst)         # 求和
zip(a, b)        # 打包
```

## 列表/字典推导式

```python
# 列表推导
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]

# 字典推导
{x: x**2 for x in range(5)}

# 集合推导
{x**2 for x in range(10)}

# 生成器表达式
(x**2 for x in range(10))
```

## 装饰器

```python
# 基本装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        # 前置处理
        result = func(*args, **kwargs)
        # 后置处理
        return result
    return wrapper

@decorator
def my_function():
    pass

# 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")
```

## 上下文管理器

```python
# 使用 with 语句
with open('file.txt') as f:
    content = f.read()

# 自定义上下文管理器
from contextlib import contextmanager

@contextmanager
def my_context():
    # 设置
    yield
    # 清理

with my_context():
    # 使用上下文
    pass
```
