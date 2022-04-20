# Windows Subsystem for Linux (WSL)

适用 Linux 的 Windows 子系统

- [微软官方中文教程](https://docs.microsoft.com/zh-cn/windows/wsl/install)

## 配置 VS Code

在 VS Code 扩展栏中搜索 Remote-WSL 扩展并安装。之后即可在 VS Code 的左侧边栏中找到 Remote Explorer 选项，通过 Remote-WSL 连接新安装的 Ubuntu 系统。

## 利用文件资源管理器访问 WSL 中的文件夹

在任一文件夹目录下,从WSL终端中运行：

```cmd
explorer.exe .
```

即可在文件资源管理器中打开 WSL 中该文件夹的路径。
