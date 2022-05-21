# ESP32

## ESP-IDF 开发环境

环境变量设置

```shell
ESP32_PORT=/dev/ttyUSB0
```

使用开发环境shell

```shell
sudo docker run --rm \
	-v ${PWD}:/project -w /project \
	--device ${ESP32_PORT}:${ESP32_PORT} \
	-it espressif/idf
```

### API docs

- [esp-idf 编程指南](https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/get-started/index.html)

## Micropython

### 烧录micropython固件

清除flash  

```shell
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```

向flash刷入micropython ([esp32-20210902-v1.17.bin](esp32.asserts/esp32-20210902-v1.17.bin))

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 \
	--baud 460800 write_flash -z 0x1000 \
	esp32-20210902-v1.17.bin  
```

### rshell

安装

```shell
pip3 install rshell
```

连接esp32

```shell
rshell -p /dev/ttyUSB0
```

复制脚本文件(如main.py)到esp32

```shell
cp main.py /pyboard
```

获取MicroPython REPL终端

```shell
repl
```

### Micropython API docs

* [official](http://docs.micropython.org/en/latest/esp32/quickref.html)
