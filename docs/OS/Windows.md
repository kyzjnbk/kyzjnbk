# Windows 

## - 理解windows环境变量

**1 理解**

目前的理解：环境变量就是给一个路径起个名，一个名就代表了某个路径。

环境变量中的path中，可以看到有一堆的路径，这个的用处就是当我们在输入某种命令的时候，它会现在当前文件夹中寻找可以执行该命令的程序。没找到的话就会去path中描述的一堆路径中去寻找。

可以执行命令的文件类型有：.exe   .cmd  等。

**2 注意事项**

给系统变量的path添加新的路径的时候，在以下窗口添加的变量不要加最后的分号。网上那些加分号的估计是老的windows版本，没有把每个path展开写，将所有的path写到一行，然后用分号分隔。

![](windows.assets/1586797143666.png)

如图所示：当只用一行展示所有的path的时候，就会用分号将path都分隔。

![1586797290120](windows.assets/1586797290120.png)	





## - 如何调出软键盘

运行->osk

![image-20200219003005421](windows.assets/image-20200219003005421.png)

即可调出软键盘：

![image-20200219003109057](windows.assets/image-20200219003109057.png)





## - windows访问某些可以访问的外网很慢

![image-20200720210856912](windows.assets/image-20200720210856912.png)

```cmd
192.30.255.113 github.com
35.244.233.98 kaggle.com
```









## - windows cmd 的用法积累

**1 关机**

```
shutdown -s -t 60        # 表示在60s后关机，如果把60改成0，就表示立刻关机了
```



**2 批处理**

可以把一堆cmd命令写到一个bat文件中，这样就可以批处理运行了。



**3 查看ip地址**

ps：已写百度经验。

![1589300749744](windows.assets/1589300749744.png)



**4 判断命令是否执行成功，失败重新执行**

```cmd
@echo off
:video1
youtube-dl -f bestvideo xxxxx1
if %errorlevel% == 1 (
	goto video1
)

:video2
youtube-dl -f bestvideo xxxxx2
if %errorlevel% == 1 (
	goto video2
)

:video3
youtube-dl -f bestvideo xxxxx3
if %errorlevel% == 1 (
	goto video3
)
```









## - 睡眠后，电脑风扇还在转



## - chrome Software Reporter Tool长时间占用CPU解决办法

**什么是Software Reporter Tool：**

> Software Reporter Tool是一个Chrome清理工具,用于清理谷歌浏览器中不必要或恶意的扩展，应用程序，劫持开始页面等等。当你安装Chrome时，Software_reporter_tool.exe也j就会被下载在SwReporter文件夹下的Chrome应用数据文件夹中。

**如何关闭SRT：**

> 这个软件在运行的过程中可能会长时间地占用CPU，导致高CPU使用率。我们虽然可以通过任务管理器手动结束进程或者选择删除SRT，但这都不是长久的解决办法。因为前者过一段时间它又会再次运行，后者在浏览器更新的时候就又会重新被下载下来。要完美地解决这一个问题我们可以进入SRT目录，默认它位于以下目录
>
> <font color="red">C:\Users\[YourName]\AppData\Local\Google\Chrome\User Data\SwReporter\[版本]\software_reporter_tool.exe</font>
>
> 我们还可以通过`win+r`键打开运行命令窗口并输入以下命令快速找到它
>
> <font color = 'red'>%localappdata%\Google\Chrome\User Data\SwReporter</font>
>
> ![image-20200518134315005](windows.assets/image-20200518134315005.png)
>
> 1.右键单击software_reporter_tool.exe选择属性
> 2.转到“安全”选项卡 
>
> ![](windows.assets/image-20200518134410625.png)
> 
> 4.点击“禁用继承”
> 5.选择"从此对象中删除所有继承的权限",之后一路点击“确定”“确定”。
>
> 这样就没有人可以访问SwReporter文件夹并启动Software Reporter Tool了。
>
> ps：我当时的做法是直接把这个.exe给删了。删了之后也没出现什么问题。



## - win10设置保存图片时保存jpg格式而不是.jfjf格式

**step1：**win+R，并键入 regedit打开注册表

 ![1597943264475](windows.assets/1597943264475.png)



**step2：**修改参数，见下图

![1597943488756](windows.assets/1597943488756.png)





## - 解决Chrome谷歌浏览器Win10右下键弹出广告信息

**第一步：复制连接在网址栏打开**

- 网址
  `chrome://settings/content/notifications?search=%E9%80%9A%E7%9F%A5`
- 回车后进入下一步

**第二步：禁止弹窗**

- 推荐将所有的弹窗都禁止了
- 其实一般都是境外网站弹窗广告
- 如果你还希望收到其它网站的通知
- 那就只进制境外网站就好了

![image-20200913140444810](windows.assets/image-20200913140444810.png)



## - win10简体繁体切换

ps：已写百度经验

win10自带的输入法是：微软拼音输入法。默认情况下，该输入法的简繁体切换快捷键是开启的，快捷键为：ctrl+shft+F。但如果用户只使用一种，不需要切换，此时若仍开启着快捷键则会出现用户误按了快捷键的情况，反而造成不方便。因此本经验将介绍win10如何关掉输入法简繁体切换的快捷键。

![](windows.assets/image-20201214142906677.png)

![](windows.assets/image-20201214142549295.png)

![](windows.assets/image-20201214141819190.png)

![](windows.assets/image-20201214141859267.png)

![](windows.assets/image-20201214142003458.png)

![](windows.assets/image-20201214142154999.png)

![](windows.assets/image-20201214142221288.png)

![](windows.assets/image-20201214142252162.png)



## - windows 添加映射网络驱动

![](windows.assets/image-20210301145623213.png)

下图那个ip是部署了samba服务的ip地址，记得要勾选“使用其他凭据连接”

![](windows.assets/image-20210301145933638.png)

![](windows.assets/image-20210301145527668.png)

ps：我在实验室的samba的密码：123456



## - windows安装

### 一、U盘装系统的三个步骤：

U盘安装Win10系统整个过程分三步，虽说讲的很多，但其实操作都不难，只是为了让电脑小白用户也能看得懂，必需详细一些。

1、制作原版系统U盘

2、如何启动制作好的系统U盘

3、安装win10系统



### 二、准备工作

1、U盘启动制作工具——软碟通(UltraISO)

2、Win10原版系统镜像文件(ISO格式)

3、U盘一个，容量需要8GB以上（因为Win10镜像文件就超过4GB，因此U盘必须8GB或更大）

下面我们正式U盘安装Win10系统环节。

第一步、制作原版win10系统U盘

1、首先将U盘插入电脑USB接口，然后运行打开UltraISO软碟通工具，点击顶部菜单中的「文件」->「打开」，如图所示。

![](windows.assets/image-20200223053738784.png)

2、 然后打开找到我们下载的win10系统镜像文件，再点击启动，写入硬盘映像，更改写入方式为USB-HDD+ v2，最后点击写入即可，操作步骤如下图所示。 

![](windows.assets/image-20200223053830811.png)

![](windows.assets/image-20200223053840788.png)

![](windows.assets/image-20200223053848300.png)

 3、接下来等待完成系统镜像写入启动U盘即可，写入完成后就说明原版系统U盘已经做好了，如图所示。 

![](windows.assets/image-20200223054003850.png)

![](windows.assets/image-20200223054020515.png)

 值得一提的是，UltraISO将U盘制程成可用于安装系统的启动盘，并写入镜像之前，会格式化U盘。如果你U盘之前存储了重要文件，记得提前备份到其他U盘或者放在网盘或电脑硬盘中，否则会出现数据丢失。制作好的启动U盘，打开之后可以看到原本系统文件和配置文件，这些文件以后都不要去动（删），否则会影响今后安装系统使用。 

![](windows.assets/image-20200223054701686.png)

![](windows.assets/image-20200223054736379.png)

**第二步、设置U盘启动**

UltraISO将U盘制作成启动盘，并写入Windows10原本镜像后，今后这个U盘，就可以给电脑安装系统了，包括刚才我们用的这台电脑或者其它任何电脑安装系统。

不过呢？启动U盘插入电脑，重启电脑默认不会进入系统安装界面，而是直接进入系统。这主要是因为，电脑默认是从硬盘启动的，而 不是U盘启动，因此还需要设置电脑从U盘启动，这样才能进入U盘系统安装界面。

 

目前，原版Win10系统进入U盘启动有2种方式，一种是UEFI启动，一种是传统B[iOS](http://www.ityears.com/pc/ios/)启动，两种启动方式都可以。**电脑进入启动U盘的方法，是电脑开机后，立即马上不停的按启动键，而不是按着不动**； 

**1、UEFI启动**

UEFI启动也就是快启动，可以直接选择进入U盘安装系统。不过，不同电脑开机进入快启动的按键不同，它是根据你的[主板](http://www.ityears.com/tags/2771-0.html)或[笔记本](http://www.ityears.com/notebook/)的品牌来定的，大家可以参考下图中的表格来找出自己电脑的启动键，也可以查询百度。

![](windows.assets/image-20200223054837859.png)

**2、传统BIOS启动**

传统BIOS启动就是先进入电脑Bios设置，然后将电脑第一启动项由默认的 硬盘 设置改成 U盘，并保存并退出，之后重启电脑就可以直接进入U盘系统安装界面了。

![](windows.assets/image-20200223054919968.png)



不管是BIOS还是UEFI，只要能运行到U盘就行。

**第三步：安装系统**

设置电脑从U盘启动之后，接下来就可以看到Win10初始化安装界面了。

1、Win10初始安装界面，一般默认是简体中文，直接点击下一步即可，如图所示。

![](windows.assets/image-20200223055900256.png)

 2、接下来选择Win10系统版本，一般建议选择专业版。当然，如果您有家庭版的序列号，那就选家庭版，之后再点下一步，在继续下一步中，选择“自定义安装”，如图所示。 

![](windows.assets/image-20200223055929156.png)

![](windows.assets/image-20200223055951151.png)



**敲重点！！**，对于那种新建分区的磁盘，这里都是这样，都会提示有问题的。如果，磁盘在这里显示不了，说明这个磁盘还没有创建分区，此时，只要通过PE里的磁盘管理工具，格式化分区，再创建一个分区即可。

![](windows.assets/image-20200223060033789.png)

然后，这里提示：

![image-20200223060409420](windows.assets/image-20200223060409420.png)

这是因为，磁盘的管理方式不同。解决方法：

![](image-20200223060507335.png)

![](windows.assets/image-20200223060528054.png)

![](windows.assets/image-20200223060543687.png)

![](windows.assets/image-20200223060638604.png)



然后这里点击 刷新 即可出现刚才分配的那些盘。

![](windows.assets/image-20200223060730885.png)

这里可能会提示 整个盘有些空间没有分配完，解决方案：选中最后一个盘，点击“拓展”，按照操作来，则可成功将剩下的空闲的盘拓展成一个盘，就不会浪费磁盘的空间了。



然后就开始安装了。

![](windows.assets/image-20200223061102153.png)

