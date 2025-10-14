# Python 包管理指南

Python有丰富的第三方库生态系统，掌握包管理工具对于高效开发至关重要。

## pip 基础

### 安装包

```bash
# 安装单个包
pip install numpy

# 安装特定版本
pip install numpy==1.21.0

# 安装最低版本要求
pip install 'numpy>=1.20.0'

# 从requirements.txt安装
pip install -r requirements.txt

# 从GitHub安装
pip install git+https://github.com/username/repo.git

# 安装可编辑模式（开发模式）
pip install -e .
```

### 卸载和更新

```bash
# 卸载包
pip uninstall numpy

# 更新包到最新版本
pip install --upgrade numpy

# 更新pip本身
python -m pip install --upgrade pip
```

### 查看已安装的包

```bash
# 列出所有已安装的包
pip list

# 显示包的详细信息
pip show numpy

# 列出过时的包
pip list --outdated

# 导出已安装的包
pip freeze > requirements.txt
```

## 虚拟环境

虚拟环境可以为每个项目创建独立的Python环境，避免包版本冲突。

### venv (Python内置)

```bash
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
## Windows
myenv\Scripts\activate
## Linux/Mac
source myenv/bin/activate

# 退出虚拟环境
deactivate

# 删除虚拟环境（直接删除文件夹）
rm -rf myenv  # Linux/Mac
rmdir /s myenv  # Windows
```

### virtualenv (功能更强大)

```bash
# 安装virtualenv
pip install virtualenv

# 创建虚拟环境
virtualenv myenv

# 指定Python版本
virtualenv -p python3.9 myenv

# 激活和使用方式与venv相同
```

### 最佳实践

```bash
# 项目结构示例
my_project/
├── venv/              # 虚拟环境（不提交到git）
├── src/               # 源代码
├── tests/             # 测试代码
├── requirements.txt   # 依赖列表
├── .gitignore        # 忽略venv/
└── README.md

# .gitignore 内容
venv/
__pycache__/
*.pyc
.env
```

## Conda 环境管理

Conda不仅管理Python包，还可以管理其他语言的包和二进制依赖。

### 基本命令

```bash
# 创建环境
conda create -n myenv python=3.9

# 激活环境
conda activate myenv

# 退出环境
conda deactivate

# 删除环境
conda remove -n myenv --all

# 列出所有环境
conda env list

# 克隆环境
conda create -n newenv --clone myenv
```

### 包管理

```bash
# 安装包
conda install numpy

# 安装特定版本
conda install numpy=1.21.0

# 从特定渠道安装
conda install -c conda-forge pandas

# 更新包
conda update numpy

# 更新所有包
conda update --all

# 搜索包
conda search numpy

# 列出已安装的包
conda list
```

### 环境导出和导入

```bash
# 导出环境（包含所有包）
conda env export > environment.yml

# 导出环境（仅包含手动安装的包）
conda env export --from-history > environment.yml

# 从文件创建环境
conda env create -f environment.yml

# 更新已存在的环境
conda env update -f environment.yml
```

### environment.yml 示例

```yaml
name: myproject
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy=1.21
  - pandas=1.3
  - matplotlib=3.4
  - scipy=1.7
  - pip
  - pip:
    - lsqfit
    - gvar
```

## 依赖管理最佳实践

### requirements.txt 的正确写法

```txt
# 生产环境依赖（精确版本）
numpy==1.21.5
pandas==1.3.5
matplotlib==3.5.1

# 开发环境依赖
# 使用 requirements-dev.txt 分离开发依赖
pytest>=7.0.0
black>=22.0.0
flake8>=4.0.0

# 从其他文件引用
-r requirements.txt

# 指定索引源
--index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 从GitHub安装
git+https://github.com/user/repo.git@v1.0.0#egg=package
```

### 项目结构示例

```
my_project/
├── requirements.txt          # 生产环境依赖
├── requirements-dev.txt      # 开发环境依赖
├── requirements-test.txt     # 测试依赖
└── setup.py                  # 项目元数据
```

**requirements.txt:**
```txt
numpy>=1.20.0,<2.0.0
pandas>=1.3.0
matplotlib>=3.4.0
```

**requirements-dev.txt:**
```txt
-r requirements.txt
black==22.3.0
pytest==7.1.2
ipython==8.4.0
```

### setup.py 示例

```python
from setuptools import setup, find_packages

setup(
    name="my_research_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A research package for data analysis",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    python_requires=">=3.8",
)
```

安装方式：
```bash
# 安装基础依赖
pip install .

# 安装开发依赖
pip install -e ".[dev]"

# 安装所有依赖
pip install -e ".[dev,docs]"
```

## 加速包下载

### 使用国内镜像源

**临时使用：**
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
```

**永久配置：**

Linux/Mac:
```bash
mkdir -p ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
EOF
```

Windows:
```
在 %APPDATA%\pip\pip.ini 文件中添加：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

**常用国内镜像：**
- 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple
- 阿里云：https://mirrors.aliyun.com/pypi/simple
- 中科大：https://pypi.mirrors.ustc.edu.cn/simple
- 豆瓣：https://pypi.douban.com/simple

### Conda 配置镜像

```bash
# 添加清华镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes

# 查看当前配置
conda config --show-sources
```

## 常见问题解决

### 包安装失败

**问题1：网络超时**
```bash
# 增加超时时间
pip install --timeout 1000 package_name

# 使用国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
```

**问题2：权限不足**
```bash
# 使用用户模式安装（不推荐在虚拟环境中使用）
pip install --user package_name

# 或使用sudo（Linux/Mac，不推荐）
sudo pip install package_name

# 最佳实践：使用虚拟环境
```

**问题3：依赖冲突**
```bash
# 查看依赖树
pip install pipdeptree
pipdeptree

# 强制重新安装
pip install --force-reinstall package_name

# 忽略已安装的依赖
pip install --no-deps package_name
```

### 包版本冲突

```bash
# 查看包的依赖
pip show package_name

# 查看哪些包依赖某个包
pip show -f package_name

# 解决方案：使用虚拟环境隔离项目
```

### pip 和 conda 混用问题

**最佳实践：**
1. 优先使用conda安装科学计算包（numpy, scipy, pandas等）
2. conda无法安装的包再用pip
3. 避免在base环境中安装包

```bash
# 在conda环境中使用pip
conda activate myenv
conda install pip
pip install package_not_in_conda
```

## 进阶工具

### Poetry (现代依赖管理)

```bash
# 安装Poetry
curl -sSL https://install.python-poetry.org | python3 -

# 创建新项目
poetry new my-project

# 添加依赖
poetry add numpy pandas

# 添加开发依赖
poetry add --group dev pytest black

# 安装所有依赖
poetry install

# 构建和发布
poetry build
poetry publish
```

### pipenv (结合pip和virtualenv)

```bash
# 安装pipenv
pip install pipenv

# 创建环境并安装包
pipenv install numpy pandas

# 安装开发依赖
pipenv install --dev pytest

# 激活环境
pipenv shell

# 运行命令（不激活环境）
pipenv run python script.py
```

### pip-tools (锁定依赖版本)

```bash
# 安装pip-tools
pip install pip-tools

# requirements.in 文件
numpy
pandas
matplotlib

# 生成锁定版本的requirements.txt
pip-compile requirements.in

# 同步环境
pip-sync requirements.txt
```

## 创建自己的包

### 基本结构

```
my_package/
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   └── test_module1.py
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
```

### 打包和发布

```bash
# 安装构建工具
pip install build twine

# 构建包
python -m build

# 上传到PyPI测试服务器
twine upload --repository testpypi dist/*

# 上传到PyPI
twine upload dist/*
```

## 参考资源

- [pip 文档](https://pip.pypa.io/)
- [Conda 文档](https://docs.conda.io/)
- [Python Packaging 用户指南](https://packaging.python.org/)
- [Poetry 文档](https://python-poetry.org/)
