# frp

[GitHub项目](https://github.com/fatedier/frp)

免费的内网穿透软件，需要自己有服务器，如阿里云、腾讯云和华为云服务器。[中文文档](https://gofrp.org/docs/)

## 服务器端（公网）

使用docker来部署frp server的步骤（容器是一种虚拟化技术，[知乎](https://zhuanlan.zhihu.com/p/39155341)）：

1. 安装docker

```bash
apt install docker.io
systemctl enalbe --now docker
```

2. 创建frps配置


```bash
# apt install neovim
nvim frps.ini
```

在`frps.ini`中复制以下内容，参考完整的[官方默认配置](https://github.com/fatedier/frp/blob/dev/conf/frps_full.ini)：

```ini
# frps.ini
[common]
# A literl address or host name for IPv6 must be enclosed
# in square brackets, as in "[::1]:80", "[ipv6-host]:http" or "[ipv6-host%zone]:80"
# For single "bind_addr" field, no need square brackets, like "bind_addr = ::".
bind_addr = 0.0.0.0
bind_port = 7000

# udp port to help make udp hole to penetrate nat
bind_udp_port = 7001

# if you want to support virtual host, you must set the http port for listening (optional)
# Note: http port and https port can be same with bind_port
vhost_http_port = 80
vhost_https_port = 443

# set dashboard_addr and dashboard_port to view dashboard of frps
# dashboard_addr's default value is same with bind_addr
# dashboard is available only if dashboard_port is set
dashboard_addr = 0.0.0.0
dashboard_port = 7500

# dashboard user and passwd for basic auth protect
dashboard_user = admin
dashboard_pwd = admin

# authentication_method specifies what authentication method to use authenticate frpc with frps.
# If "token" is specified - token will be read into login message.
# If "oidc" is specified - OIDC (Open ID Connect) token will be issued using OIDC settings. By default, this value is "token".
authentication_method = token

# authenticate_heartbeats specifies whether to include authentication token in heartbeats sent to frps. By default, this value is false.
authenticate_heartbeats = false

# AuthenticateNewWorkConns specifies whether to include authentication token in new work connections sent to frps. By default, this value is false.
authenticate_new_work_conns = false

# auth token
token = 12345678
```

特别注意`token`字段，它是你进行内网穿透时的密码。

3. 运行容器，

```bash
docker run --restart=always --network host -d -v ${PWD}/frps.ini:/etc/frp/frps.ini --name frps snowdreamtech/frps
```

以上命令的参数说明：

```bash
--restart=always # 在容器停止后自动重启，这将容器设置为开机自动启动
--network host # 指定容器与主机享受相同的network namespace，在这种情况下，我们访问主机端口就能访问我们的容器
-v # 将当前目录的frps.ini 映射到容器中的/etc/frp/frps.ini
--name # 容器的名字
```

## 客户端(局域网)

```ini
# frpc.ini
[common]
server_addr = {{ .Envs.FRP_SERVER_ADDR }}
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 22
```

```bash
frpc -c frpc.ini
```
