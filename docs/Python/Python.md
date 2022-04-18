# Python3

本手册用于整合归纳一些有用或有趣的 Python3 外部链接。

## 安装Python3

我建议安装 [Anaconda](https://www.anaconda.com/)，它提供了一个简单的初始环境并自带常用的计算库，可以让你快速安装 Python 和相关的第三方库。

!!! note

    对于Windows的用户，执行conda init可能在下次启动命令行时提示没有权限运行profile.ps1，这是因为Windows的系统的安全策略默认禁止了自动执行脚本。
    如果你的系统禁止了执行profile.ps1，请以管理员权限手动执行以下命令：
    
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

如果你使用的是官方的Python，建议在使用时为项目创建虚拟环境，比如 virtualenv。

## 配置环境

### 使用conda


### 使用pip3

[https://blog.csdn.net/peiwang245/article/details/98317863](https://blog.csdn.net/peiwang245/article/details/98317863)

!!! note
    对于网络不是很好的科研仔，常常需要换国内源，以清华源为例：

    Linux用户：

        mkdir ~/.pip && echo -e "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf


## Python3基础教程

There are many online resources for learning the Python language; here are three of the best:

- Introductory Python 3 tutorials [https://www.learnpython.org/](https://www.learnpython.org/)
- Free to sign up; introductory Python 2 tutorials (printing is a bit different than Python 3) [https://www.codecademy.com/learn/learn-python](https://www.codecademy.com/learn/learn-python)
- 4.5 hour video covering all the Python basics [https://www.youtube.com/watch?v=rfscVS0vtbw](https://www.youtube.com/watch?v=rfscVS0vtbw) 


### 示例代码

- [命令行参数解析](parse_args.py)

#### 文件IO

- [读取CSV](csv_io.py)
- [读写json](json_io.py)

#### [numpy](numpy/numpy.md)

#### Python features

- [函数名重载(function overload)](function_overload.py)

#### CUDA编程

- [numba.cuda](numba/cuda.ipynb)

#### [Tensorflow](tensorflow/Tensorflow.md)

