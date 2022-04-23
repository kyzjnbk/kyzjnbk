# C/C++

- [cppreference](https://en.cppreference.com/w/)([中文版](https://zh.cppreference.com/w/%E9%A6%96%E9%A1%B5))

视频教程

![type:video](https://www.youtube.com/embed/KJgsSFOSQv0)
![type:video](https://www.youtube.com/embed/vLnPwxZdW4Y)

## 编译器

### MSVC (Windows)

### gcc/g++

### clang/clang++ (LLVM)

## 包管理

### vcpkg

- [中文指南](https://github.com/microsoft/vcpkg/blob/master/README_zh_CN.md) C++ Library Manager for Windows, Linux, and MacOS

### apt(Debian,Ubuntu)

```bash
sudo apt install libxxx-dev
```

### yum(CentOS,Fedora)

## 构建工具

###Visual Studio (Windows)

### GNU make

### CMake
  
!!! note "cmake-init"
    推荐搭配使用的软件：[cmake-init](https://github.com/friendlyanon/cmake-init)。帮助您快速创建一个cmake工程。
    ![](cpp.asserts/cmake-init_example.gif)

    需要python3>=3.8，安装:

    ```bash
    pip3 install cmake-init
    ```

## 代码规范

### clang-format



## 实用库

### CLI

- [p-ranav/structopt](https://github.com/p-ranav/structopt)

    ??? example
    
        ```cpp title="main.cpp"
        #include <structopt/app.hpp>

        struct FileOptions {
            // Positional arguments
            // ./main <input_file> <output_file>
            std::string input_file;
            std::string output_file;
        };
        STRUCTOPT(FileOptions, input_file, output_file);

        int main(int argc, char *argv[]) {

            try {
                auto options = structopt::app("my_app").parse<FileOptions>(argc, argv);

                // Print parsed arguments:
                std::cout << "\nInput file  : " << options.input_file << "\n";
                std::cout << "Output file : " << options.output_file << "\n";

            } catch (structopt::exception& e) {
                std::cout << e.what() << "\n";
                std::cout << e.help();
            }
        }
        ```

        ```bash title="usage"
        foo@bar:~$ ./main foo.txt bar.csv

        Input file  : foo.txt
        Output file : bar.csv

        foo@bar:~$ ./main foo.csv
        Error: expected value for positional argument `output_file`.

        USAGE: ./my_app input_file output_file

        ARGS:
            input_file
            output_file
        ```

### GUI

- ImGui
- Qt

### CG / Physic simulation

- glm
- igl
- bullet

### network

- enet

### math

- GSL
- Eigen

### Parallel

- [MPI](mpi)
- [bshoshany/thread-pool](https://github.com/bshoshany/thread-pool)

