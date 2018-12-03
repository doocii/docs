# Linux 命令学习

## ./的含义

可以用于执行当前目录下的可执行文件。例如 `./pushblog.sh`

## 文件操作

- 打包tar，格式：`tar -cvf /tmp/etc.tar /etc`

## 网络

### 局域网拷贝

- scp命令，格式：`scp -r local_folder remote_user@remote_ip:remote_folder`，需要先安装SSH

### 系统操作

- crontab命令用于设置周期性被执行的指令。
  - `crontab -e` 可以编辑当前用户的配置文件，例如`15 * * * * python -O /home/laodu/bash/airmail.py`，每小时的15分运行python脚本
  - `crontab -l` 显示当前配置
  - 打开服务 archlinux： `sudo systemctl enable cronie.service`
  - 重启服务 archlinux： `sudo systemctl restart cronie.service`
  - 重启服务 ubuntu： `sudo systemctl start cron.service`

---

## 我的bash目录（20180904）

在 ~/bash 目录下

- `airmail.py` 发送空气质量
- `conky.bash` conky配置文件
- `dm.bash` dm配置文件
- `douban.py` 抓取每月阅读数量并输出
- `doy.py`
- `doy.sh` 显示今天是今年的第几天
- `google` google something 
- `pm.py` 输出空气质量
- `pomo` 25分钟的番茄钟
- `pushnote` 向bitbucket备份笔记（已停用）
- `sysinfo.bash` 显示系统信息
- `vpn.sh` 全局vpn
- `weather.py` conky需要的天气部分，他人写的
- `wiki` 笔记以wiki形式显示


### 备份脚本

```
#!/bin/bash
# 20181009

# backup folders
backup_files="/home/laodu/bash /home/laodu/doc"

# backup to
dest="/home/laodu"
filename="laptop-backup-$(date +%y%m%d).tgz"

# use tar
tar czfP $dest/$filename  $backup_files

echo "Backup Finished!"
```
