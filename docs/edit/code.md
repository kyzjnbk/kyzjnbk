# Visual Studio Code

*功能强大，爱不释手。*

## 下载与安装

Windows 用户直接网页搜索下载安装即可。

- [Visual Studio Code 官方网站](https://code.visualstudio.com/download)

!!! important "MacOS"
    Mac用户安装完后还需要自行配置（install 'code' command in PATH），参考[官方文档](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line)。

![type:video](https://www.youtube.com/embed/WPqXP_kLzpo)

## 推荐插件

在这里，我们推荐安装一些通用的插件，由于一些特定语言的基础插件根据具体科研方向而言是必装的，不包含在此，
如[Python插件](https://marketplace.visualstudio.com/items?itemName=ms-python.python)。

### 远程连接

- [Remote-SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
- [Remote-WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
- [Remote-Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)*

### AI代码补全

- [Tabnine](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

### 文档工作、代码注释 (Documentation & Comment)

- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- Comment Anchors
- [Auto Comment Blocks (Javadoc-style: C/C++/C#/Java)](https://marketplace.visualstudio.com/items?itemName=kevinkyang.auto-comment-blocks)
- Doxygen Documentation Generator (C/C++)
- autoDocstring - Python Docstring Generator (Python)

## 实用技巧

### 快捷键

掌握快捷键可以大幅提高编码效率：

**通用操作**

- `Ctrl/Cmd + P` - 快速打开文件
- `Ctrl/Cmd + Shift + P` - 命令面板
- `Ctrl/Cmd + B` - 切换侧边栏显示
- `Ctrl/Cmd + \` - 拆分编辑器
- `Ctrl/Cmd + W` - 关闭当前标签页

**编辑操作**

- `Alt + ↑/↓` - 移动当前行
- `Shift + Alt + ↑/↓` - 复制当前行
- `Ctrl/Cmd + /` - 注释/取消注释
- `Ctrl/Cmd + D` - 选择下一个相同的词
- `Ctrl/Cmd + Shift + L` - 选择所有相同的词
- `Alt + Click` - 多光标编辑

**代码导航**

- `Ctrl/Cmd + G` - 跳转到指定行
- `F12` - 跳转到定义
- `Alt + ←/→` - 前进/后退
- `Ctrl/Cmd + Shift + O` - 跳转到文件中的符号

### 代码片段 (Snippets)

创建自定义代码片段可以节省大量时间：

1. 打开命令面板 (`Ctrl/Cmd + Shift + P`)
2. 输入 "Preferences: Configure User Snippets"
3. 选择语言（如 Python）

示例Python代码片段：

```json
{
    "Plot with matplotlib": {
        "prefix": "plotm",
        "body": [
            "import matplotlib.pyplot as plt",
            "import numpy as np",
            "",
            "fig, ax = plt.subplots(figsize=(8, 6))",
            "ax.plot($1, $2, label='$3')",
            "ax.set_xlabel('$4')",
            "ax.set_ylabel('$5')",
            "ax.legend()",
            "plt.show()"
        ],
        "description": "Create a basic matplotlib plot"
    }
}
```

### 工作区设置

为不同项目配置不同的设置：

在项目根目录创建 `.vscode/settings.json`：

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

## 常见问题

### Python 解释器未找到

**症状：** VS Code无法识别Python或提示找不到解释器

**解决方法：**
1. 按 `Ctrl/Cmd + Shift + P` 打开命令面板
2. 输入 "Python: Select Interpreter"
3. 选择正确的Python解释器路径
4. 如果列表为空，点击 "Enter interpreter path" 手动输入

### 远程SSH连接超时

**症状：** 使用Remote-SSH插件连接服务器时超时

**解决方法：**
1. 编辑SSH配置文件 (`~/.ssh/config`)：
```
Host myserver
    HostName server.example.com
    User username
    ServerAliveInterval 60
    ServerAliveCountMax 3
```
2. 在VS Code设置中增加超时时间：
```json
{
    "remote.SSH.connectTimeout": 60
}
```

### 代码格式化不工作

**症状：** 保存文件时代码没有自动格式化

**解决方法：**
1. 确保已安装格式化工具（如 `black`）：
```bash
pip install black
```
2. 在设置中启用保存时格式化：
```json
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

### Git 集成显示大量变更

**症状：** Git面板显示了不应该追踪的文件

**解决方法：**
1. 在项目根目录创建 `.gitignore` 文件
2. 添加常见的Python忽略规则：
```
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints/
venv/
.env
.venv
*.so
.Python
```

### 插件安装失败

**症状：** 插件下载或安装时出错

**解决方法：**
1. 检查网络连接
2. 清除VS Code缓存：
   - Windows: `%APPDATA%\Code\Cache`
   - Mac/Linux: `~/.config/Code/Cache`
3. 使用代理（如果在防火墙后）：
```json
{
    "http.proxy": "http://proxy.example.com:8080"
}
```

## 调试技巧

### Python 调试配置

在项目中创建 `.vscode/launch.json`：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Python: Script with Arguments",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["--input", "data.txt", "--output", "result.txt"],
            "console": "integratedTerminal"
        }
    ]
}
```

### 断点调试

- 点击行号左侧添加断点
- `F5` 开始调试
- `F10` 单步跳过
- `F11` 单步进入
- `Shift + F11` 单步跳出
- 使用"调试控制台"在断点处执行代码

### 条件断点

右键点击断点，选择"编辑断点"，可以设置：
- **条件断点：** 仅在满足条件时中断（如 `i > 100`）
- **命中次数：** 在命中特定次数后中断
- **日志点：** 不中断，只输出日志

## 推荐主题和字体

### 主题
- **Dark+** (默认暗色主题，护眼)
- **One Dark Pro** (优雅的暗色主题)
- **Dracula Official** (流行的暗色主题)
- **Light+** (默认亮色主题)

### 字体
- **Fira Code** (支持连字符，免费)
- **JetBrains Mono** (专为开发者设计)
- **Cascadia Code** (微软出品)

启用字体连字符：
```json
{
    "editor.fontFamily": "'Fira Code', Consolas, 'Courier New', monospace",
    "editor.fontLigatures": true,
    "editor.fontSize": 14
}
```


