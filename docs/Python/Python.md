# Python3

本手册用于整合归纳一些有用或有趣的 Python3 外部链接。

## 安装Python3

我建议安装 [Anaconda](https://www.anaconda.com/)，它提供了一个简单的初始环境并自带常用的计算库，可以让你快速安装 Python 和相关的第三方库。

!!! note
    一般来说，需要初始化shell环境，才能使用 Anaconda。

    ```bash
    # 初始化shell(仅需运行一次)
    conda init
    ```

    对于Windows的用户，执行conda init可能在下次启动命令行时提示没有权限运行profile.ps1，这是因为Windows的系统的安全策略默认禁止了自动执行脚本。
    如果你的系统禁止了执行profile.ps1，请以管理员权限手动执行以下命令：
    
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

如果你使用的是官方的Python，建议在使用时为项目创建虚拟环境，比如 virtualenv。

## 配置环境

### 使用conda

!!! note
    对于网络不是很好的科研仔，常常需要换国内源:

    - [清华源帮助文档](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
    - [上海交通大学(华东教育网骨干节点)](https://mirrors.sjtug.sjtu.edu.cn/docs/anaconda)


环境管理

```bash
# 创建一个名为 my_env_name 的环境，用python 3.7 版本
# 删除环境则将对应目录删除即可。一般为 “conda安装位置/envs/my_env_name”
conda create -n my_env_name python3.7

# 或从已有环境克隆，创建新的环境
conda create -n new_env_2 --clone env_name

# 激活 my_env_name 环境
conda activate my_env_name

#列出所有环境
conda env list

# 退出激活的环境
conda deactivate

# 导出环境为 my_env_name.yml 文件
conda env export > my_env_name.yml

# 从 .yml 文件导入环境
conda env create -n new_env -f my_env_name.yml
```

包管理

```bash
# 列出所有包
conda list

# 安装包
conda install pkg_name

# 从指定 channel 下载
conda install --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ pytorch
```

### 使用pip3

!!! note
    对于网络不是很好的科研仔，常常需要换国内源：

    - [清华源帮助文档](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
    - [上海交通大学](https://mirrors.sjtug.sjtu.edu.cn/docs/pypi-packages)
    - [163源(网易)帮助文档](https://mirrors.163.com/.help/pypi.html)
    - [腾讯云镜像帮助文档](https://mirrors.tencent.com/help/pypi.html)
    - [阿里云镜像帮助文档](https://developer.aliyun.com/mirror/pypi)




```bash
# 查看Python包的信息**
pip3 show Package

# 安装Python包
pip3 install Package1 [Package2]..
# 例如我需要安装numpy和scipy，可以这样安装：
pip3 install numpy scipy
# 在包名后可以使用运算符来指定版本，例如指定numpy版本为1.16：
pip3 install numpy==1.16
# 使用-U参数更新已安装的包，例如更新numpy版本：
pip3 install -U numpy

# 卸载第三方库
pip3 uninstall Package

# 查看已经安装的库
pip3 list
```

## Python3 基础教程

There are many online resources for learning the Python language; here are three of the best:

- [Introductory Python 3 tutorials](https://www.learnpython.org/)
- (Python2) [Free to sign up; introductory Python 2 tutorials (printing is a bit different than Python 3)](https://www.codecademy.com/learn/learn-python)
- [4.5 hour video covering all the Python basics](https://www.youtube.com/watch?v=rfscVS0vtbw)
    ![type:video](https://www.youtube.com/embed/rfscVS0vtbw)


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

