# Python 常见错误与解决方案

本文档整理了Python编程中最常见的错误及其解决方法，帮助初学者快速定位和解决问题。

## 语法错误 (SyntaxError)

### 1. 缩进错误

```python
# 错误示例
def my_function():
print("Hello")  # IndentationError

# 正确写法
def my_function():
    print("Hello")  # 使用4个空格缩进
```

**解决方案：**
- 统一使用4个空格进行缩进
- 不要混用Tab和空格
- 在VS Code中设置：`"editor.insertSpaces": true`

### 2. 括号不匹配

```python
# 错误示例
result = (1 + 2 * (3 + 4)  # SyntaxError: unexpected EOF

# 正确写法
result = (1 + 2 * (3 + 4))
```

**解决方案：**
- 使用IDE的括号高亮功能
- 写完左括号立即写右括号
- 使用代码格式化工具

### 3. 冒号缺失

```python
# 错误示例
if x > 0  # SyntaxError: invalid syntax
    print("positive")

# 正确写法
if x > 0:
    print("positive")
```

### 4. 引号不匹配

```python
# 错误示例
text = "Hello World'  # SyntaxError

# 正确写法
text = "Hello World"
text = 'Hello World'
text = """多行
文本"""
```

## 名称错误 (NameError)

### 变量未定义

```python
# 错误示例
print(result)  # NameError: name 'result' is not defined

# 正确写法
result = 42
print(result)
```

**常见原因：**
- 变量名拼写错误
- 变量在使用前未定义
- 作用域问题

```python
def my_function():
    local_var = 10

print(local_var)  # NameError: 局部变量在函数外不可见
```

## 类型错误 (TypeError)

### 1. 类型不匹配

```python
# 错误示例
result = "5" + 3  # TypeError: can only concatenate str to str

# 正确写法
result = int("5") + 3
# 或
result = "5" + str(3)
```

### 2. 不可调用的对象

```python
# 错误示例
my_list = [1, 2, 3]
result = my_list(0)  # TypeError: 'list' object is not callable

# 正确写法
result = my_list[0]  # 使用方括号访问列表元素
```

### 3. 参数数量错误

```python
# 错误示例
def add(a, b):
    return a + b

result = add(1, 2, 3)  # TypeError: add() takes 2 positional arguments but 3 were given

# 正确写法
result = add(1, 2)
```

## 索引错误 (IndexError)

```python
# 错误示例
my_list = [1, 2, 3]
value = my_list[3]  # IndexError: list index out of range

# 正确写法
value = my_list[2]  # 索引从0开始，最大索引是len(list)-1

# 或使用异常处理
try:
    value = my_list[3]
except IndexError:
    value = None
```

**防御性编程：**
```python
if index < len(my_list):
    value = my_list[index]
else:
    value = default_value
```

## 键错误 (KeyError)

```python
# 错误示例
my_dict = {'a': 1, 'b': 2}
value = my_dict['c']  # KeyError: 'c'

# 正确写法
value = my_dict.get('c', default_value)

# 或检查键是否存在
if 'c' in my_dict:
    value = my_dict['c']
else:
    value = default_value
```

## 属性错误 (AttributeError)

```python
# 错误示例
my_list = [1, 2, 3]
my_list.append(4)    # 正确
my_list.push(5)      # AttributeError: 'list' object has no attribute 'push'

# 错误示例2
my_var = None
result = my_var.upper()  # AttributeError: 'NoneType' object has no attribute 'upper'

# 正确写法
if my_var is not None:
    result = my_var.upper()
```

## 值错误 (ValueError)

### 1. 类型转换失败

```python
# 错误示例
number = int("hello")  # ValueError: invalid literal for int()

# 正确写法
try:
    number = int(user_input)
except ValueError:
    print("请输入有效的数字")
    number = 0
```

### 2. 解包数量不匹配

```python
# 错误示例
a, b = [1, 2, 3]  # ValueError: too many values to unpack

# 正确写法
a, b, c = [1, 2, 3]
# 或
a, b, *rest = [1, 2, 3]  # rest = [3]
```

## 导入错误 (ImportError / ModuleNotFoundError)

```python
# 错误示例
import nonexistent_module  # ModuleNotFoundError

# 解决方案
# 1. 检查模块名拼写
# 2. 安装缺失的包
# pip install module_name

# 3. 检查Python环境
# which python
# pip list
```

### 循环导入

```python
# file1.py
from file2 import func2
def func1():
    pass

# file2.py
from file1 import func1  # ImportError: cannot import name 'func1'
def func2():
    pass

# 解决方案：
# 1. 重构代码，避免循环依赖
# 2. 在函数内部导入
# 3. 将共同依赖提取到第三个文件
```

## 零除错误 (ZeroDivisionError)

```python
# 错误示例
result = 10 / 0  # ZeroDivisionError

# 正确写法
if denominator != 0:
    result = numerator / denominator
else:
    result = float('inf')

# 或使用异常处理
try:
    result = numerator / denominator
except ZeroDivisionError:
    result = float('inf')
```

## 文件错误 (FileNotFoundError)

```python
# 错误示例
with open('nonexistent.txt', 'r') as f:  # FileNotFoundError
    content = f.read()

# 正确写法
import os

if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        content = f.read()
else:
    print("文件不存在")

# 或使用异常处理
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在")
    content = ""
```

## NumPy 常见错误

### 1. 形状不匹配

```python
import numpy as np

# 错误示例
a = np.array([[1, 2], [3, 4]])  # shape (2, 2)
b = np.array([1, 2, 3])          # shape (3,)
result = a + b  # ValueError: operands could not be broadcast

# 正确写法
b = np.array([1, 2])  # shape (2,)
result = a + b
```

### 2. 数组索引错误

```python
# 错误示例
arr = np.array([[1, 2], [3, 4]])
value = arr[0, 0, 0]  # IndexError: too many indices

# 正确写法
value = arr[0, 0]  # 二维数组使用两个索引
```

### 3. dtype 不匹配

```python
# 错误示例
int_array = np.array([1, 2, 3], dtype=int)
int_array[0] = 1.5  # 值会被截断为1

# 正确写法
float_array = np.array([1, 2, 3], dtype=float)
float_array[0] = 1.5  # 现在可以存储浮点数
```

## Pandas 常见错误

### 1. KeyError: 列名不存在

```python
import pandas as pd

# 错误示例
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df['C']  # KeyError: 'C'

# 正确写法
if 'C' in df.columns:
    result = df['C']
else:
    df['C'] = 0  # 创建新列
```

### 2. SettingWithCopyWarning

```python
# 警告示例
subset = df[df['A'] > 0]
subset['B'] = 10  # SettingWithCopyWarning

# 正确写法
subset = df[df['A'] > 0].copy()
subset['B'] = 10

# 或直接在原数据上修改
df.loc[df['A'] > 0, 'B'] = 10
```

### 3. 索引对齐问题

```python
# 错误示例
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[0, 1, 2])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 3])
result = df1 + df2  # 索引不对齐，会产生NaN

# 正确写法
result = df1.add(df2, fill_value=0)
# 或重置索引
df2.index = [0, 1, 2]
result = df1 + df2
```

## 逻辑错误

### 1. 浮点数比较

```python
# 错误示例
a = 0.1 + 0.2
if a == 0.3:  # False！浮点数精度问题
    print("Equal")

# 正确写法
import numpy as np
if np.isclose(a, 0.3):
    print("Equal")

# 或
epsilon = 1e-10
if abs(a - 0.3) < epsilon:
    print("Equal")
```

### 2. 可变默认参数

```python
# 错误示例
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2]  # 意外！

# 正确写法
def append_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 3. 深拷贝 vs 浅拷贝

```python
# 错误示例
list1 = [[1, 2], [3, 4]]
list2 = list1  # 仅复制引用
list2[0][0] = 999
print(list1)  # [[999, 2], [3, 4]]  # list1也被修改！

# 正确写法
import copy

list2 = copy.deepcopy(list1)  # 深拷贝
list2[0][0] = 999
print(list1)  # [[1, 2], [3, 4]]  # list1不受影响
```

## 性能问题

### 1. 循环中拼接字符串

```python
# 慢（每次拼接都创建新字符串）
result = ""
for i in range(10000):
    result += str(i)

# 快（使用join）
result = "".join(str(i) for i in range(10000))
```

### 2. 不必要的列表创建

```python
# 内存效率低
total = sum([x**2 for x in range(1000000)])

# 内存效率高（使用生成器）
total = sum(x**2 for x in range(1000000))
```

### 3. 重复计算

```python
# 慢
for item in items:
    if expensive_function() > threshold:
        process(item)

# 快（缓存结果）
result = expensive_function()
for item in items:
    if result > threshold:
        process(item)
```

## 调试技巧

### 1. 打印调试信息

```python
# 基础方法
print(f"变量值: {variable}")
print(f"变量类型: {type(variable)}")
print(f"变量长度: {len(variable)}")

# 使用pprint美化输出
from pprint import pprint
pprint(complex_data_structure)
```

### 2. 使用断言

```python
def divide(a, b):
    assert b != 0, "除数不能为0"
    assert isinstance(a, (int, float)), "被除数必须是数字"
    return a / b
```

### 3. 使用日志

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def my_function(x):
    logger.debug(f"函数输入: {x}")
    result = x * 2
    logger.debug(f"函数输出: {result}")
    return result
```

### 4. 使用 pdb 调试器

```python
import pdb

def problematic_function(data):
    result = []
    for item in data:
        pdb.set_trace()  # 程序会在这里暂停
        processed = item * 2
        result.append(processed)
    return result
```

## 常用检查清单

遇到错误时，按以下顺序检查：

1. **仔细阅读错误信息** - Python的错误信息通常很准确
2. **查看堆栈跟踪** - 找到错误发生的确切位置
3. **检查变量类型** - 使用 `type()` 和 `isinstance()`
4. **检查变量值** - 使用 `print()` 或调试器
5. **查阅文档** - 确认API的正确用法
6. **搜索错误信息** - 在Google或Stack Overflow上搜索
7. **简化问题** - 创建最小可复现示例
8. **使用调试器** - 逐步执行代码

## 参考资源

- [Python官方文档 - 异常](https://docs.python.org/3/library/exceptions.html)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Real Python - Python Debugging](https://realpython.com/python-debugging-pdb/)
