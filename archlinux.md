# 笔记：Archlinux

## 安装

> 参考：
- [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)
- [beginner's guide](https://wiki.archlinux.org/index.php/Beginners_guide)

### iso制作

U盘写入工具：[YUMI – Multiboot USB Creator](http://www.pendrivelinux.com/yumi-multiboot-usb-creator/)

### 建立网络连接

确定无线网络接口名，可能是wlp2s0

    iw dev

执行 wifi-menu

    wifi-menu wlp2s0

按照提示选择无线网络，填写密码，无错误提示就联网成功。

### 建立存储设备

对应选择mbr或者gpd格式的硬盘，新电脑可以用gpd。

#### 擦除分区表

    sgdisk -Z /dev/sda

#### 用 fdisk 建立 MBR 分区

    fdisk /dev/sda

按照wiki分区。

### 创建文件系统

使用mkfs命令格式化分区

    mkfs.ext4 /dev/sda1
    mkfs.ext4 /dev/sda2

### 挂载分区

显示当前分区布局：

    lsblk -f

mount命令挂载：

    mount /dev/sda1 /mnt
    mkdir /mnt/home
    mount /dev/sda2 /mnt/home

### 选择安装镜像

    nano /etc/pacman.d/mirrorlist

只保留清华的源即可。Server = http://mirrors.tuna.tsinghua.edu.cn/archlinux/arch

使用 `sudo pacman -Syy` 更新

### 安装基本系统

    pacstrap -i /mnt base base-devel

默认选择全部包，等待下载安装。

#### 生成 fstab

    genfstab -U -p /mnt >> /mnt/etc/fstab

运行一次即可，然后可以查看：

    nano /mnt/etc/fstab

### 修改根目录

（此步骤的意思应该是从livecd模式切换成硬盘上的系统）

    arch-chroot /mnt /bin/bash

#### 修改时区编码

    nano /etc/locale.gen

只保留以下：

    en_US.UTF-8 UTF-8
    zh_CN.UTF-8 UTF-8
    zh_TW.UTF-8 UTF-8

运行locale-gen命令，重建编码表。

    #locale-gen

#### 修改时区

    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#### 修改时间模式

    hwclock --systohc --utc

#### 设置电脑名

    echo myhostname > /etc/hostname

#### 安装网络有关的包

    pacman -S dialog
    pacman -S wpa_supplicant
    pacman -S netctl
    pacman -S wireless_tools

####设置密码

  passwd

### 安装并配置 bootloader

#### 安装GRUB

安装grub并执行安装到MBR

  pacman -S grub
  grub-install --target=i386-pc --recheck /dev/sda

生成配置文件

  grub-mkconfig -o /boot/grub/grub.cfg

离开 chroot 环境：

  exit

重启：

  reboot

## 配置

### 无线网络配置

在beginner's guide 里推荐reboot之前就安装配置wifi，但我跳过这段，所以重新配置。

参考 [Wireless network configuration (简体中文)](https://wiki.archlinux.org/index.php/Wireless_network_configuration_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

先查看设备

    ip link

如果显示类似wlp2s0这样无线设备，证明设备正常，启用设备：

    ip link set wlp2s0 up

之前安装步骤里安装了 dialog, wifi-menu ，所以可以执行：

    wifi-menu wlp2s0

这时会自动生成一份配置文件，在/etc/netctl，不需编辑，查看一下然后自动启用它，my_network是该配置文件名：

    netctl enable my_network

正常应该可以上网了，但是又失败。查看问题：

    netctl status my_network

提示Loaded，但Active failed。把自动生成的带有“-”的profile重命名，然后重启一次就联网成功了。这部分可以查看 `etctl--h` 帮助。

### 安装桌面

#### 安装Xorg

选择xinit和xfce

安装xorg和xfce

    pacman -S xorg-server xorg-xinit xorg-server-utils
    pacman -S xfce4 xfce4-goodies

尝试配置xinit，先拷贝配置文件

  $ cp /etc/skel/.xinitrc ~/

编辑它，只保留xfce一行，并且放在文件最后

运行startx就可以到xfce桌面！

## 硬件

安装触摸板

    pacman -S xf86-input-synaptics

### 账户设置

因为一直用root登录，所以xfce里mousepad会提示root不安全，按照wiki的步骤增加账户：

先安装zsh：

  pacman -S zsh

创建一个用户laodu，并使用zsh作默认shell（用bash也可以？）

    useradd -m -g users -G audio,video,floppy,network,rfkill,scanner,storage,optical,power,wheel,uucp -s /usr/bin/zsh laodu

创建密码：

    passwd archie

注销xfce，切换到新用户，startx。

解决方法：安装sudo

    pacman -S sudo

编辑sudo配置文件，只能用vi

    visudo

取消wheel权限的注释，当用户使用sudo命令时，就可以以root身份执行命令了。

同样给新用户配置.xinitrc

     cd ~
     cp /etc/skel/.xinitrc ~
     vi ~/.xinitrc

在最后一行取消xfce注释，然后startx启动。

#### 解决声音问题

安装alsa

   pacman -S alsa-utils 

解除静音，运行

  $ alsamixer

在顶部panel添加一个 audio mixer plugin，就是音量调节工具。

#### 安装字体

  #pacman -S wqy-microhei ttf-dejavu

#### 安装yaourt

加Yaourt源至 /etc/pacman.conf:

  [archlinuxcn]
  SigLevel = Optional TrustedOnly
  Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

执行

  pacman -Sy yaourt

提示三个包需要下载：packgage-query-1.14-1 yajl-2.1.0-1,yaourt-1.5-1，但第一个包总出现错误，原因：注意要加SigLevel = Optional TrustAll，这样就不会报PGP验证错误了。

archlinuxcn 速度慢，可以添加其他镜像：[Arch Linux CN Community repo mirrors list](https://github.com/archlinuxcn/mirrorlist-repo)

## 输入法

2016/12/29 更新：已经改为使用fcitx+搜狗拼音，方便流畅。

  yaourt -S fcitx-sogoupinyin

## 网络

$ pacman -S wicd wicd-gtk notification-daemon

参考： https://wiki.archlinux.org/index.php/Wicd

    systemctl enable wicd.service
    gpasswd -a $USERNAME users
    systemctl start wicd

## xfce桌面

### 挂载U盘

安装 gvfs

### 解压ISO文件

安装 cdrkit，其中包含mkisofs命令，格式如下：

     mkisofs -o xxx.iso /the/path

## pacman

### 常用

  pacman -Syu 升级系统
  pacman -Syy 同步软件列表
  pacman -Scc 清理软件包
  pacman -S xxx 安装
  pacman -Ss xxx 查询
  pacman -R xxx 卸载
  pacman -Qs xxx 查询已安装包

### invalid pgp key 错误

$ sudo pacman-key --refresh-keys

### xfce workspace

ctrl+alt+left/right 切换

xfce的panel可以选择显示在某个显示器上，方便在大显示器使用。

### thunar技巧

- 多选文件，按F2，可以批量重命名
- [Custom Actions](http://docs.xfce.org/xfce/thunar/custom-actions)，可以自定义右键菜单命令
- 安装`davfs2`，可以访问webdav共享，格式：`dav://192.168.1.100:2112/`
- 安装？？，可以访问ftp

### 翻墙

安装 shadowsocks-qt5，开启后导入配置，本地sock5代理就可用了。浏览器需要配置插件，填写本地代理端口。

终端使用 proxychains ，查询本机ip：

    $curl ipinfo.io

### 解决u盘不显示问题(20180626)

- 显示usb设备: lsusb
- thunar需要安装 gvfs thunar-volman
- 动挂载需要使thunar在daemon模式下运行，编辑`~/.xinitrc`文件，加入　`thunar --daemon &`

---

## TODO

挂载u盘无法拷贝中文文件名