# Anaconda for ubuntu

打开 VScode，利用 Remote-WSL 链接到已经安装好的 ubuntu 系统，然后在终端中输入

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Linux-x86_64.sh
```

这一步是下载安装包，也可以访问网址
（https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=A ）
找到自己想要的版本进行下载。

<br />

在刚刚下载 .sh 文件的目录下运行

```
bash Anaconda3-2021.05-Linux-x86_64.sh
```

<br />

阅读注册信息，然后输入yes；查看文件即将安装的位置，按enter，即可安装

安装完成后，收到加入环境变量的提示信息，输入yes

<br />

提示信息“Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]”，输入no

<br />

重启终端，即可使用Anaconda3

<br />

若在终端输入 python，仍然会显示Ubuntu自带的python版本，我们执行

```
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc
```

上面的命令会修改终端的默认 python 为 anaconda，至此全部完成。