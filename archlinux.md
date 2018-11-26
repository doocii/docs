# archlinux


## 安装准备

1. 下载最新版镜像，用rufus写入U盘
2. BIOS，Disable Secure Boot. BIOS > Secure Boot > Disabled
3. 确保ACHI模式
4. Win10关闭快速启动（控制面板-电源计划）
5. Win10压缩卷，留出给Linux的空间

## 安装开始

### 分区

1. lsblk 显示所有分区，刚留出的空白分区不会显示。Win10已经有一个EFI分区 /dev/sda1。
2. `cfdisk /dev/sda` 进行分区，在 free space 上选择 New、Write，输入q退出。显示linux分区是/dev/sda9
3. 格式化分区 `mkfs.ext4 /dev/sda9`
4. 挂载根分区 `mount /dev/sda9 /mnt`
5. 挂载ESP分区 `mkdir /mnt/boot` `mount /dev/sda1 /mnt/boot`

### 网络

wifi-menu ，选择并配置无线网络。ping通了就ok。

### 安装

- 修改/etc/pacman.d/mirrorlist，Server = http://mirrors.163.com/$repo/os/$arch
- 安装基本系统 `pacstrap /mnt base`
- 生成fstab `# genfstab -U /mnt >> /mnt/etc/fstab`
- `arch-chroot /mnt /bin/bash` 进入系统

## 配置

- Locale：编辑`/etc/locale.gen`，去掉三行注释：en_US.UTF-8 UTF-8 zh_CN.UTF-8 UTF-8 zh_TW.UTF-8 UTF-8。执行 `locale-gen`，写入配置 `echo LANG=en_US.UTF-8 > /etc/locale.conf`
- 时间： `tzselect` ，选择亚洲上海，生成时区配置 `hwclock --systohc --utc`
- 主机名：`echo mypc > /etc/hostname`
- 对应的hosts，修改 /etc/hosts
```
127.0.0.1	localhost
::1		localhost
127.0.1.1	myhostname.localdomain	myhostname
```

- 网络配置：新系统并没有网络包，所以要安装：`pacman -S iw wpa_supplicant dialog`
- root密码：`passwd`

## 系统引导

- 安装： `pacman -S grub efibootmgr os-prober --noconfirm`
- 安装引导： `grub-install --efi-directory=/boot --bootloader-id=grub`
- 生成配置： `grub-mkconfig -o /boot/grub/grub.cfg`

这里只配置好了arch的启动项

- exit退出chroot
- 卸载分区：umount -R /mnt
- reboot重启，检查bios里grub是不是第一启动项，正常可以进入arch
- 重启后再执行  `grub-mkconfig -o /boot/grub/grub.cfg` 把windows加入grub列表

### 用户

- 添加普通用户：useradd -m -g users -s /bin/bash laodu
- 设置密码： passwd laodu
- 设置sudo用户：`pacman -S sudo` 执行 visudo，添加一行 `laodu  ALL=(ALL) ALL`

## 系统配置

### 图形界面

- 安装显卡： `pacman -S xf86-video-inte`
- 安装桌面环境：`pacman -S mate mate-extra`
- 安装显示管理器： `pacman -S lightdm-gtk-greeter` 执行 ` systemctl enable lightdm`
- 如果使用startx进入桌面,编辑xinitrc，参考[Xinit](https://wiki.archlinux.org/index.php/Xinit_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

桌面系统要显示中文，就在`.xprofile` 文件添加：　`export LC_ALL="zh_CN.UTF-8"`

### 源

添加源，编辑 /etc/pacman.conf

    [archlinuxcn]
    SigLevel = Optional TrustedOnly
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

 安装AUR `pacman -S yaourt`
 
    [archlinuxfr]
    SigLevel = Never
    Server = http://repo.archlinux.fr/$arch

确保安装了 `pacman -S --needed base-devel`
执行`pacman -Syy`
 
### 常用pacman命令

pacman -Syu 升级系统
pacman -Syy 同步软件列表
pacman -Scc 清理软件包
pacman -S xxx 安装
pacman -Ss xxx 查询
pacman -R xxx 卸载
pacman -Qs xxx 查询已安装包

invalid pgp key错误解决 : `$ sudo pacman-key --refresh-keys`

### 环境变量

编辑 `~/.bashrc`，加入

`export PATH=$PATH:/somepath`

### 字体

- 等宽字体： `pacman -S ttf-dejavu`
- emoji： `noto-fonts-emoji`
- 中文字体，文泉驿微米黑： `pacman -S wqy-microhei`

### 输入法

- pacman -S fcitx  fcitx-im fcitx-configtool 
- pacman -S fcitx-sogoupinyin
- 需要编辑 `.xprofile` 文件,添加如下:

```
export XMODIFIERS=@im=fcitx
export QT_IM_MODULE=fcitx
export GTK_IM_MODULE=fcitx
```

### 网络配置

使用wicd管理无线网络

- 安装 wicd wicd-gtk ，以及xfce4-notifyd
- 添加服务 `systemctl enable wicd.service`
- 添加用户组 `gpasswd -a laodu users`
- 启动 `systemctl start wicd`

### 翻墙

安装 shadowsocks-qt5，开启后导入配置，本地sock5代理就可用了。浏览器需要配置插件，填写本地代理端口。

终端使用 proxychains ，查询本机ip：

    $curl ipinfo.io


### 坚果云

    pacman -S nutstore jre10-openjdk

选择其他jre环境报错，原因不明

### SSH and git

- 安装 openssh
- 创建本地ssh key：` ssh-keygen -t rsa -C "youremail@example.com"`
- 复制 `~.ssh/id_rsa.pub` 内容到github-Account settings-SSH Keys，Title随意
- 添加本地仓库 `git remote add origin git@github.com:some/git.git`
- 拉取远程 `git pull origin master` 
- 强制推送本地仓库 `git push -u origin +master`

### 微信

- 用过 electronic-wechat 和 deepin wine的微信
- 在用 wewechat

