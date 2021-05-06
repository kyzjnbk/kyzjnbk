# SSH

## Based on VS Code

### 1. Install extension "Remote SSH" of VS Code


In the left sidebar you can see a sign like Tetris, which is called "Extensions", search "Remote SSH" in the "Extensions" and install it. 

After you install it successfully, you can see an extra sign in the left sidebar called "Remote Explorer".

<br />

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

<br />

### 3. Use Remote SSH

After you updated the "ssh_config" file, anytime you want to use Remote SSH, just turn to "Remote Explorer", move your mouse pointer on the host you want to connect, you will see a button for connection, click it.

Sign in with password, then turn to "Explorer" in the left sidebar, open the folder you want to access.



