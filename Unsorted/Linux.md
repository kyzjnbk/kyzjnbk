# Linux

## Linux 环境配置

```shell
sudo apt update
```

### 换源

https://blog.csdn.net/wang_shen_tao/article/details/78676560

首先，备份源配置

```shell
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
```

替换为163源

```shell
sudo sed 's/archive.ubuntu.com/mirrors.163.com/g' /etc/apt/sources.list > /etc/apt/sources.list
```

替换为清华源

```shell
sudo sed 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list > /etc/apt/sources.list
```

## Linux 常用命令
