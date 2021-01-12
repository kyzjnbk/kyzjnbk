# WSL

Windows Subsystem for Linux

适用 Linux 的 Windows 子系统

## 配置 WSL

在 Windows 10 界面左下角的搜索栏里搜索 Powershell，以管理员身份运行 Powershell 并输入如下命令：

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

等 Powershell 中提示安装完成后，重启计算机。

## 下载 Ubuntu

我们直接在 Windows 10 的应用商店里下载最新版本的 Ubuntu。

在 Windows 10 界面左下角的搜索栏里搜索“应用商店”，然后在商店搜索栏输入 Ubuntu，安装所需要的版本即可。

安装后运行，会弹出黑色的命令框开始自动安装，等待几分钟后安装完成，依照提示设置用户名（username）和密码（passward），注意在 Linux 命令行中输入密码时，光标是不会有显示的。

设置完用户名和密码后，等待配置完成，然后在命令行中输入：

```
sudo apt update
```

## 配置 VS Code

在 VS Code 扩展栏中搜索 Remote-WSL 扩展并安装。之后即可在 VS Code 的左侧边栏中找到 Remote Explorer 选项，通过 Remote-WSL 连接新安装的 Ubuntu 系统。



