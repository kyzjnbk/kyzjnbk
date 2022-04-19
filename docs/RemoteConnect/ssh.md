# SSH

如果你并不了解SSH，希望比较系统地了解它，强烈推荐[鸟哥的SSH讲解](https://linux.vbird.org/linux_server/centos6/0310telnetssh.php#ssh_server)。
使用和维护服务器最简单的方式不是跑去实体机前面登入，而是通过网络进行远程连接来登入主机。
Linux 主机几乎都会提供sshd 这个服务，而且这个服务还是主动进行资料加密的！
SSH是接触Linux的科研仔应该掌握的最重要的基本工具之一。

## Based on VS Code

### 1. Install extension "Remote SSH" of VS Code


In the left sidebar you can see a sign like Tetris, which is called "Extensions", search "Remote SSH" in the "Extensions" and install it. 

After you install it successfully, you can see an extra sign in the left sidebar called "Remote Explorer".


### 2. Configure SSH

Turn to "Remote Explorer", move your mouse pointer to the right side of "SSH TARGETS" then you will see a gear on the right top of the left sidebar, called "Configure".

Click "Configure" and choose the one include"\ProgramData\ssh", then you opened "ssh_config" file.

Insert information of a new SSH Remote as below:

```
Host alias
    HostName hostname
    Port port
    User user
```

Save and close the "ssh_config" file.


### 3. Use Remote SSH

After you updated the "ssh_config" file, anytime you want to use Remote SSH, just turn to "Remote Explorer", move your mouse pointer on the host you want to connect, you will see a button for connection, click it.

Sign in with password, then turn to "Explorer" in the left sidebar, open the folder you want to access.



