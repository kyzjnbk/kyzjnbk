# Git

- [官方网站](https://git-scm.com/)
- [Git教程|菜鸟教程](https://www.runoob.com/git/git-tutorial.html)
- [gitignore模板](https://www.toptal.com/developers/gitignore)

<iframe src="//player.bilibili.com/player.html?aid=711226636&bvid=BV1KD4y1S7FL&cid=206667600&page=1" 
scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"  
style="width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;"> </iframe>

## 常用命令

```bash
git init # 新建一个空的仓库
git status # 查看状态
git add . # 添加文件
git commit -m '注释' # 提交添加的文件并备注说明
git remote add origin git@github.com:jinzhaogit/git.git # 连接远程仓库
git push -u origin master # 将本地仓库文件推送到远程仓库
git log # 查看变更日志
git reset --hard 版本号前六位 # 回归到指定版本
git branch # 查看分支
git branch newname # 创建一个叫newname的分支
git checkout newname # 切换到叫newname的分支上
git merge newname # 把newname分支合并到当前分支上
git pull origin master # 将master分支上的内容拉到本地上
```

[下载 git 常用命令.pdf](git 常用命令.pdf)

## Git托管网站

- [[GitHub]]
- [Gitee](https://gitee.com)

## 自建Git托管网站(self-hosted Git server)

- [gogs](https://github.com/gogs/gogs) 推荐，适合小团队，即使在树莓派上也能流程运行。
- [gitea](https://github.com/go-gitea/gitea) gogs的分支。
- [gitlab](https://about.gitlab.com/) 这个就比较重量级了，不适合在配置较差的机器上运行。
