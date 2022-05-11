# Python

本手册用于整合归纳一些有用或有趣的 Python3 外部链接。
## Python3 基础教程

There are many online resources for learning the Python language; here are three of the best:

- [Introductory Python 3 tutorials](https://www.learnpython.org/)
- (Python2) [Free to sign up; introductory Python 2 tutorials (printing is a bit different than Python 3)](https://www.codecademy.com/learn/learn-python)
- [4.5 hour video covering all the Python basics](https://www.youtube.com/watch?v=rfscVS0vtbw)
    ![type:video](https://www.youtube.com/embed/rfscVS0vtbw)

## Tyro Notes

- [Python 基础笔记](lang/python/tyro_note.md)
- [爬虫入门笔记](lang/python/spider/spider_note_for_tyro.md)
- [一些实用的代码实例](https://github.com/kyzjnbk/kyzjnbk/tree/master/docs/lang/python/examples_for_tyro)

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

### 使用conda管理环境和包

!!! note
    对于网络不是很好的科研仔，常常需要换国内源:

    - [清华源帮助文档](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
    - [上海交通大学(华东教育网骨干节点)](https://mirrors.sjtug.sjtu.edu.cn/docs/anaconda)


环境管理

```bash
# 创建一个名为 my_env_name 的环境，用python 3.7 版本
conda create -n my_env_name python=3.7

# 或从已有环境克隆，创建新的环境
conda create -n new_env_2 --clone env_name

# 激活 my_env_name 环境
conda activate my_env_name

#列出所有环境
conda env list

# 退出激活的环境
conda deactivate

# 删除环境
conda env remove -n my_env_name --all

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

### 使用pip3管理包

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

# 导出环境中的包和它们的版本
pip freeze > requirements.txt

# 在新环境中安装
pip install -r requirements.txt
```

### 使用virtualenv管理环境

安装virtualenv

```shell
# 安装virtualenv
pip3 install virtualenv
```

```shell
# 创建虚拟环境
# 常用参数
# -p python执行器路径 为虚拟环境指定Python路径  
# --system-site-packages 允许虚拟环境访问系统包目录，此选项默认为`False`
virtualenv [-p PythonPath] [--system-site-packages] 环境名
# 例如，在当前位置创建一个名为`base`的环境。
virtualenv base

# 激活虚拟环境
source path_to_activate
```

将对应目录删除即可删除环境。

## Python基础

### 函数

关键字参数

```python
#可写函数说明
def printme( str ):
    "打印任何传入的字符串"
    print (str)
    return
 
# 调用 printme 函数，不加参数会报错
printme() # ERROR
printme('123') # OK
printme(str='123') # OK
```

可以对关键字参数设置默认值

```python
def printme( str='123' ):
   	"打印任何传入的字符串"
    print (str)
    return
   
printme() # OK
```

不定长参数

```python
def functionname([formal_args,] *var_args_tuple ):
    # function body

def functionname([formal_args,] **var_args_dict ):
    # function body
```

加了星号`*`的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```python
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1) # 70
    print (vartuple) # (60, 50)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 ) 
```


加了两个星号 `**` 的参数会以字典的形式导入。

```python
def printinfo( arg1, **vardict ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1) # 1
    print (vardict) # { 'a': 2, 'b': 3 }
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```

批量传递不定长参数

```python
args = [1,2,3,4]
f(*args) # f(1,2,3,4)
```

```python
kargs = {'a':1, 'b':2}
f(**kargs) # f(a=1,b=2)
```

