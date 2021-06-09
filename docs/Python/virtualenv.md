# virtualenv介绍及基本使用

## 安装

```shell
pip3 install virtualenv
```

## 创建虚拟环境

基本操作：

```shell
virtualenv 环境名
```

例如，在命令行执行

```shell
virtualenv base
```

将在当前位置创建一个名为`base`的环境。

常用参数

- **-p python执行器路径** 为虚拟环境指定Python路径  
- **--system-site-packages** 允许虚拟环境访问系统包目录，此选项默认为`False`

## 使用虚拟环境

- Linux:
```shell
source ${path_to_activate}
```

## 环境配置

- 查看环境中的Python包

```shell
pip list
```

- 导出环境中的包和它们的版本

```shell
pip freeze > requirements.txt
```

- 在新环境中安装

```shell
pip install -r requirements.txt
```
