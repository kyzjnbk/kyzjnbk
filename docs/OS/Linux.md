# Linux

Linux，全称GNU/Linux，是一种免费使用和自由传播的类UNIX操作系统，其内核由[林纳斯·本纳第克特·托瓦兹(Linus Benedict Torvalds)](https://zh.wikipedia.org/wiki/%E6%9E%97%E7%BA%B3%E6%96%AF%C2%B7%E6%89%98%E7%93%A6%E5%85%B9)
于1991年10月5日首次发布，它主要受到Minix和Unix思想的启发，是一个基于POSIX的多用户、多任务、支持多线程和多CPU的操作系统。

Linux严格来说指Linux系统内核，但是一般交流时却指各种Linux发行版操作系统，如[Ubuntu](https://ubuntu.com/)，[CentOS](https://www.centos.org/)等都是不同的Linux发行版。
各发行版大同小异，因此，尽管CentOS在科研中用的不多，也强烈推荐[鸟哥的私房菜-基础篇](https://linux.vbird.org/linux_basic/centos7/)开始学习。
而在实际的科研中，推荐使用软件较新的Ubuntu、Fedora等Linux发行版，选择主流的发行版，对应相关的文档和交流社区也比较有规模，方便学习和交流。

- [Linux发行版列表（中文维基）](https://zh.wikipedia.org/wiki/Linux%E5%8F%91%E8%A1%8C%E7%89%88%E5%88%97%E8%A1%A8)
- [鸟哥的Linux私房菜-基础篇](https://linux.vbird.org/linux_basic/centos7/)
- [鸟哥的Linux私房菜-服务器架设篇](https://linux.vbird.org/linux_server/centos6/)

以下主要根据Ubuntu为例，补充介绍一些常用的命令和知识。

!!! danger

    在使用管理员权限在执行命令前，请确保明白了命令的含义。

## Ubuntu的包管理

### apt和apt-get简介

!!! note "TL;DR"

    apt和apt-get用于管理Ubuntu上的**系统**软件环境，即包管理器。
    使用apt和apt-get可以**安装、卸载、更新**、查看系统软件包的状态。
    其中安装、卸载、更新的操作都需要**系统管理员(root)权限**。
    如果报错内容为"Permission denied"，请检查是否有root权限，或者使用sudo命令，例如：

    ```bash
    sudo apt ...
    ```

apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。
Ubuntu 16.04 发布时，一个引人注目的新特性便是 apt 命令的引入。其实早在 2014 年，apt 命令就已经发布了第一个稳定版，只是直到 2016 年的 Ubuntu 16.04 系统发布时才开始引人关注。

随着 apt install package 命令的使用频率和普遍性逐步超过 apt-get install package，越来越多的其它 Linux 发行版也开始遵循 Ubuntu 的脚步，开始鼓励用户使用 apt 而不是 apt-get。

那么，apt-get 与 apt 命令之间到底有什么区别呢？如果它们有类似的命令结构，为什么还需要新的 apt 命令呢？是否 apt 真的比 apt-get 更好？普通用户应该使用新的 apt 命令还是坚持旧有习惯继续使用 apt-get 呢？

系统极客将在本文中解释所有这些问题，我们希望本文结束时，你将会有一个更清晰的了解。

**apt与apt-get**

在开始对比 apt 与 apt-get 命令的区别之前，我们先来看看这两个命令的背景，以及它们要试图达到的目的。

Debian 作为 Ubuntu、Linux Mint 和 elementary OS 等 Linux 操作系统的母板，其具有强健的「包管理」系统，它的每个组件和应用程序都内置在系统中安装的软件包中。Debian 使用一套名为 Advanced Packaging Tool（APT）的工具来管理这种包系统，不过请不要把它与 apt 命令混淆，它们之间是其实不是同一个东西。

在基于 Debian 的 Linux 发行版中，有各种工具可以与 APT 进行交互，以方便用户安装、删除和管理的软件包。apt-get 便是其中一款广受欢迎的命令行工具，另外一款较为流行的是 Aptitude 这一命令行与 GUI 兼顾的小工具。

如果你已阅读过我们的 apt-get 命令指南，可能已经遇到过许多类似的命令，如apt-cache、apt-config 等。如你所见，这些命令都比较低级又包含众多功能，普通的 Linux 用户也许永远都不会使用到。换种说法来说，就是最常用的 Linux 包管理命令都被分散在了 apt-get、apt-cache 和 apt-config 这三条命令当中。

apt 命令的引入就是为了解决命令过于分散的问题，它包括了 apt-get 命令出现以来使用最广泛的功能选项，以及 apt-cache 和 apt-config 命令中很少用到的功能。

在使用 apt 命令时，用户不必再由 apt-get 转到 apt-cache 或 apt-config，而且 apt 更加结构化，并为用户提供了管理软件包所需的必要选项。

> 简单来说就是：apt = apt-get、apt-cache 和 apt-config 中最常用命令选项的集合。

**apt与apt-get之间的区别**

!!! note "TL;DR"

    基本没什么区别。

通过 apt 命令，用户可以在同一地方集中得到所有必要的工具，apt 的主要目的是提供一种以「让终端用户满意」的方式来处理 Linux 软件包的有效方式。

apt 具有更精减但足够的命令选项，而且参数选项的组织方式更为有效。除此之外，它默认启用的几个特性对最终用户也非常有帮助。例如，可以在使用 apt 命令安装或删除程序时看到进度条。

apt 还会在更新存储库数据库时提示用户可升级的软件包个数。

如果你使用 apt 的其它命令选项，也可以实现与使用 apt-get 时相同的操作。

虽然 apt 与 apt-get 有一些类似的命令选项，但它并不能完全向下兼容 apt-get 命令。也就是说，可以用 apt 替换部分 apt-get 系列命令，但不是全部。

| apt 命令         | 取代的命令           | 命令的功能                     |
| ---------------- | -------------------- | ------------------------------ |
| apt install      | apt-get install      | 安装软件包                     |
| apt remove       | apt-get remove       | 移除软件包                     |
| apt purge        | apt-get purge        | 移除软件包及配置文件           |
| apt update       | apt-get update       | 刷新存储库索引                 |
| apt upgrade      | apt-get upgrade      | 升级所有可升级的软件包         |
| apt autoremove   | apt-get autoremove   | 自动删除不需要的包             |
| apt full-upgrade | apt-get dist-upgrade | 在升级软件包时自动处理依赖关系 |
| apt search       | apt-cache search     | 搜索应用程序                   |
| apt show         | apt-cache show       | 显示安装细节                   |

当然，apt 还有一些自己的命令：

| 新的apt命令      | 命令的功能                           |
| ---------------- | ------------------------------------ |
| apt list         | 列出包含条件的包（已安装，可升级等） |
| apt edit-sources | 编辑源列表                           |

需要大家注意的是：apt 命令也还在不断发展， 因此，你可能会在将来的版本中看到新的选项。

| apt-get已弃用？                                              |
| ------------------------------------------------------------ |
| 目前还没有任何 Linux 发行版官方放出 apt-get 将被停用的消息，至少它还有比 apt 更多、更细化的操作功能。对于低级操作，仍然需要 apt-get。 |

| 我应该使用apt还是apt-get？                                   |
| ------------------------------------------------------------ |
| 既然两个命令都有用，那么我该使用 apt 还是 apt-get 呢？作为一个常规 Linux 用户，系统极客建议大家尽快适应并开始首先使用 apt。不仅因为广大 Linux 发行商都在推荐 apt，更主要的还是它提供了 Linux 包管理的必要选项。 |

最重要的是，apt 命令选项更少更易记，因此也更易用，所以没理由继续坚持 apt-get。



小结

最后结大家提供两点使用上的建议：

apt 可以看作 apt-get 和 apt-cache 命令的子集, 可以为包管理提供必要的命令选项。
apt-get 虽然没被弃用，但作为普通用户，还是应该首先使用 apt。



### 使用apt

!!! note

    对于网络不是很好的科研仔，可以使用国内的apt(ubuntu)镜像源，以下是更换对应镜像源的帮助文档：

    - [清华大学镜像源帮助文档](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)
    - [北京外国语大学镜像源帮助文档](https://mirrors.bfsu.edu.cn/help/ubuntu/)
    - [163(网易)镜像源帮助文档](http://mirrors.163.com/.help/ubuntu.html)

**更新本地的软件列表**

```bash
apt-get update
```

``update``命令，会访问源列表里的每个网址，并读取软件列表，然后保存在本地电脑。软件包管理器里看到的软件列表，都是通过update命令更新的。

**升级本地的所有软件包**

```bash
apt-get upgrade
```

`#!bash apt`命令，会把本地已安装的软件，与刚下载的软件列表里对应软件进行对比，如果发现已安装的软件版本太低，就会提示你更新。如果你的软件都是最新版本，会提示：

```bash
升级了 0 个软件包，新安装了 0 个软件包，要卸载 0 个软件包，有 0 个软件包未被升级。
```

总而言之，update是更新软件列表，upgrade是更新软件。

**安装特定的软件**

```bash
apt install Package1 [Package2]..
```

例如，我需要安装C语言的编译器gcc和clang,可以这样安装：

```
apt install gcc clang
```

## 使用vim编辑文本文件

**安装**

```bash
apt install vim
```

- [Vim教程](https://www.runoob.com/linux/linux-vim.html)
- [vim 操作命令大全](https://blog.csdn.net/weixin_37657720/article/details/80645991)

!!! caution "++ctrl+s++"

    有时会习惯性地写完程序后按下++ctrl+s++，潜意识地认为这是“保存”
    反应过来后发觉不对，又开始按esc，结果发现按啥都没反应了
    查找资料后得知，
    这是因为++ctrl+s++的组合快捷键在vim中是“阻塞后续输入”的作用
    可以按++ctrl+q++以取消。
