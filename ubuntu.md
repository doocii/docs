# Ubuntu笔记

> from 2015.2 update 20171001

## 安装配置

- 字体：文泉驿 `sudo apt-get install ttf-wqy-microhei`

### 软件

- 输入法：直接安装搜狗拼音
- 浏览器：Chrome，翻墙后同步账户
- 编辑器：SublimeText3，参考subulime笔记
- rss阅读：Liferea
- 下载：wget, [uGet](http://ugetdm.com/)

### xfce桌面配置

按照windows下的习惯配置快捷键，在 `Settings Manager > Window Manager > Keyboard.` 找到并配置：

- show desktop：win+D
- mousepad ：win + N
- xfce4-terminal : win + T
- google-chrome-stable : win + C
- thunar : win + E

#### 任务栏

- Orage时间显示修改，属性里，时间格式为：`---  %T --- %n%F(%V)`

## 硬件问题

### 网络

重启网络：

    /etc/init.d/network-manager restart

使用 wicd 管理xfce下的网络。如果不稳定，可以改为固定IP，避免IP冲突。（20150508）

### 软件问题

### python版本问题

要切换默认python版本，网上的一个方法是修改默认链接：

`ln -s /usr/bin/ptyhon2.7 /usr/bin/python`

但这个方法会导致之后安装calibre时，出现apport相关错误，应该是python2/3之间以来的问题。解决方法是，不要使用上面的链接方法，脚本制定python版本。这一点似乎不如archlinux，直接改成python3。
