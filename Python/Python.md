# Python

## Pip换国内源

清华源：

```shell
mkdir ~/.pip && echo -e "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf
```

## 示例代码

- [命令行参数解析](parse_args.py)

### 文件IO

- [读取CSV](csv_io.py)
- [读写json](json_io.py)

### Python features

- [函数名重载(function overload)](function_overload.py)

## CUDA编程

- [numba.cuda](numba/cuda.ipynb)

## [Tensorflow](tensorflow/Tensorflow.md)

## References

### 基础教程

There are many online resources for learning the Python language; here are three of the best:\
https://www.learnpython.org/ -- Introductory Python 3 tutorials\
https://www.codecademy.com/learn/learn-python -- Free to sign up; introductory Python 2 tutorials (printing is a bit different than Python 3)\
https://www.youtube.com/watch?v=rfscVS0vtbw -- 4.5 hour video covering all the Python basics