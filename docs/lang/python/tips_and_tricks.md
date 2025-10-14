# Python 实用技巧与经验

本文收集了科研编程中常用的Python技巧和最佳实践。

## 代码简化技巧

### 1. 使用解包简化变量交换

```python
# 传统方式
temp = a
a = b
b = temp

# Python方式
a, b = b, a
```

### 2. 多重赋值

```python
# 同时赋多个值
x, y, z = 1, 2, 3

# 解包列表
data = [1, 2, 3, 4, 5]
first, *middle, last = data
# first = 1, middle = [2, 3, 4], last = 5
```

### 3. 链式比较

```python
# 传统方式
if x > 0 and x < 10:
    pass

# Python方式
if 0 < x < 10:
    pass
```

### 4. 列表推导式

```python
# 创建平方列表
squares = [x**2 for x in range(10)]

# 带条件的列表推导
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 嵌套列表推导
matrix = [[i+j for j in range(3)] for i in range(3)]
```

### 5. 字典推导式

```python
# 创建字典
squares_dict = {x: x**2 for x in range(5)}

# 反转字典
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
```

### 6. 集合推导式

```python
# 去重并平方
unique_squares = {x**2 for x in [1, 1, 2, 2, 3, 3]}
# 结果: {1, 4, 9}
```

## 数据处理技巧

### 1. 使用 enumerate 获取索引

```python
# 不推荐
for i in range(len(items)):
    print(i, items[i])

# 推荐
for i, item in enumerate(items):
    print(i, item)

# 指定起始索引
for i, item in enumerate(items, start=1):
    print(i, item)
```

### 2. 使用 zip 并行迭代

```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

# 并行迭代
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 转置矩阵
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed = list(zip(*matrix))
```

### 3. 使用 any 和 all

```python
# 检查是否有任何元素满足条件
if any(x > 0 for x in data):
    print("至少有一个正数")

# 检查是否所有元素都满足条件
if all(x > 0 for x in data):
    print("所有数都是正数")
```

### 4. 使用 defaultdict 简化计数

```python
from collections import defaultdict

# 传统方式
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

# 使用 defaultdict
counts = defaultdict(int)
for item in items:
    counts[item] += 1
```

### 5. 使用 Counter 进行计数

```python
from collections import Counter

# 统计元素出现次数
data = ['a', 'b', 'c', 'a', 'b', 'a']
counts = Counter(data)
# Counter({'a': 3, 'b': 2, 'c': 1})

# 找出最常见的元素
most_common = counts.most_common(2)  # [('a', 3), ('b', 2)]
```

### 6. 使用 itertools 进行高效迭代

```python
import itertools

# 排列组合
list(itertools.permutations([1, 2, 3], 2))  # 排列
list(itertools.combinations([1, 2, 3], 2))   # 组合

# 笛卡尔积
list(itertools.product([1, 2], ['a', 'b']))  # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# 无限迭代器
counter = itertools.count(start=1, step=2)  # 1, 3, 5, 7, ...
repeater = itertools.repeat('hello', 3)     # 'hello', 'hello', 'hello'
cycler = itertools.cycle([1, 2, 3])         # 1, 2, 3, 1, 2, 3, ...
```

## 文件操作技巧

### 1. 使用 with 语句自动关闭文件

```python
# 推荐方式
with open('data.txt', 'r') as f:
    content = f.read()
# 文件自动关闭

# 同时打开多个文件
with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        fout.write(line.upper())
```

### 2. 使用 pathlib 处理路径

```python
from pathlib import Path

# 创建路径对象
path = Path('data/results.txt')

# 检查路径
if path.exists():
    print("文件存在")

# 创建目录
path.parent.mkdir(parents=True, exist_ok=True)

# 读写文件
content = path.read_text()
path.write_text("new content")

# 遍历目录
for file in Path('data').glob('*.txt'):
    print(file)

# 路径拼接
full_path = Path('data') / 'subdir' / 'file.txt'
```

### 3. 读取大文件

```python
# 逐行读取（节省内存）
with open('large_file.txt', 'r') as f:
    for line in f:
        process(line)

# 使用生成器
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

for line in read_large_file('large_file.txt'):
    process(line)
```

## 性能优化技巧

### 1. 使用局部变量

```python
# 慢（访问全局变量）
def process_data():
    for i in range(1000000):
        result = math.sqrt(i)

# 快（使用局部变量）
def process_data():
    sqrt = math.sqrt  # 创建局部引用
    for i in range(1000000):
        result = sqrt(i)
```

### 2. 避免循环中的重复计算

```python
# 慢
for item in items:
    if len(items) > 100:
        process(item)

# 快
length = len(items)
for item in items:
    if length > 100:
        process(item)
```

### 3. 使用 map 和 filter

```python
# 传统循环
results = []
for x in data:
    results.append(x ** 2)

# 使用 map
results = list(map(lambda x: x ** 2, data))

# 使用列表推导（通常更快）
results = [x ** 2 for x in data]
```

### 4. 字符串拼接优化

```python
# 慢（重复创建字符串对象）
result = ""
for s in strings:
    result += s

# 快（使用join）
result = "".join(strings)
```

### 5. 使用集合进行成员测试

```python
# 慢（列表查找是O(n)）
if item in my_list:
    pass

# 快（集合查找是O(1)）
my_set = set(my_list)
if item in my_set:
    pass
```

## NumPy 技巧

### 1. 布尔索引

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6])

# 选择大于3的元素
filtered = data[data > 3]  # [4, 5, 6]

# 复杂条件
filtered = data[(data > 2) & (data < 5)]  # [3, 4]
```

### 2. 花式索引

```python
# 使用索引数组
indices = [0, 2, 4]
selected = data[indices]

# 二维数组索引
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
rows = [0, 2]
cols = [1, 2]
result = matrix[rows, cols]  # [2, 9]
```

### 3. 广播机制

```python
# 矩阵加向量
matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
result = matrix + vector  # 向量会自动广播到矩阵的每一行

# 归一化
data = np.random.rand(100, 10)
mean = data.mean(axis=0)
std = data.std(axis=0)
normalized = (data - mean) / std
```

### 4. 向量化操作

```python
# 慢（使用循环）
result = np.zeros(len(data))
for i in range(len(data)):
    result[i] = data[i] ** 2 + 2 * data[i] + 1

# 快（向量化）
result = data ** 2 + 2 * data + 1
```

### 5. einsum 高级运算

```python
# 矩阵乘法
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)
C = np.einsum('ij,jk->ik', A, B)

# 对角线求和
matrix = np.random.rand(5, 5)
trace = np.einsum('ii->', matrix)

# 张量缩并
tensor1 = np.random.rand(3, 4, 5)
tensor2 = np.random.rand(5, 6)
result = np.einsum('ijk,kl->ijl', tensor1, tensor2)
```

## Pandas 技巧

### 1. 链式操作

```python
import pandas as pd

# 链式操作
result = (df
    .query('age > 25')
    .groupby('category')['value']
    .mean()
    .sort_values(ascending=False)
)
```

### 2. 使用 apply 和 lambda

```python
# 对列应用函数
df['new_col'] = df['old_col'].apply(lambda x: x ** 2)

# 对行应用函数
df['sum'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
```

### 3. 多列操作

```python
# 同时对多列应用相同操作
df[['col1', 'col2']] = df[['col1', 'col2']].apply(np.log)

# 创建多列
df[['new1', 'new2']] = df.apply(
    lambda row: pd.Series([row['A']*2, row['B']*3]),
    axis=1
)
```

### 4. 高效的数据筛选

```python
# 使用 query
df_filtered = df.query('age > 25 and income > 50000')

# 多条件筛选
mask = (df['age'] > 25) & (df['income'] > 50000)
df_filtered = df[mask]
```

## 调试技巧

### 1. 使用 pdb 调试

```python
import pdb

def my_function(x):
    result = x * 2
    pdb.set_trace()  # 在此处设置断点
    return result

# 或在程序崩溃后进入调试器
python -m pdb script.py
```

### 2. 使用 assert 进行断言

```python
def calculate_average(data):
    assert len(data) > 0, "数据不能为空"
    assert all(isinstance(x, (int, float)) for x in data), "数据必须是数字"
    return sum(data) / len(data)
```

### 3. 使用 logging 而不是 print

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# 使用日志
logging.debug('调试信息')
logging.info('一般信息')
logging.warning('警告')
logging.error('错误')
logging.critical('严重错误')
```

### 4. 使用 timeit 测试性能

```python
import timeit

# 测试代码执行时间
time = timeit.timeit(
    'result = [x**2 for x in range(1000)]',
    number=10000
)
print(f"执行时间: {time}秒")
```

### 5. 使用 cProfile 进行性能分析

```python
import cProfile
import pstats

# 分析函数性能
cProfile.run('my_function()', 'profile_stats')

# 查看统计信息
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative')
stats.print_stats(10)  # 显示前10个最耗时的函数
```

## 代码组织技巧

### 1. 使用 __name__ == '__main__'

```python
def main():
    # 主程序逻辑
    pass

if __name__ == '__main__':
    main()
```

### 2. 使用配置文件

```python
# config.py
DATABASE_URL = 'postgresql://localhost/mydb'
DEBUG = True
MAX_ITERATIONS = 1000

# main.py
import config

if config.DEBUG:
    print("Debug mode")
```

### 3. 使用 argparse 处理命令行参数

```python
import argparse

parser = argparse.ArgumentParser(description='数据分析脚本')
parser.add_argument('input', help='输入文件路径')
parser.add_argument('-o', '--output', default='output.txt', help='输出文件路径')
parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')

args = parser.parse_args()
process_data(args.input, args.output, args.verbose)
```

## 常用代码模板

### 1. 错误处理模板

```python
def safe_operation(data):
    try:
        result = process(data)
        return result
    except ValueError as e:
        print(f"值错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        raise
    finally:
        cleanup()
```

### 2. 上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def timer(name):
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"{name} 耗时: {end - start:.2f}秒")

# 使用
with timer("数据处理"):
    process_large_dataset()
```

### 3. 装饰器模板

```python
import functools

def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"尝试 {attempt + 1} 失败，重试...")
        return wrapper
    return decorator

@retry(max_attempts=3)
def fetch_data():
    # 可能失败的操作
    pass
```

## 参考资源

- [Python官方文档](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Cookbook](https://python3-cookbook.readthedocs.io/)
