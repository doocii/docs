# sublime text 做笔记工具探究

## 引言

Sublime Text，默认可以打开一个目录，这样就可以用文件夹组织markdown文档，实现编辑、查询功能，同步可以依靠云盘或git。目标侧重书写。

## 优势vs劣势

- 优势：数据可控，管理方式直接，文档简单，跨平台同步
- 劣势：没有商业软件的分享/导入优势，图片支持匮乏

## 使用准备

- 下载对应版本
- 依照个人习惯建立层级文件夹
- 安装[Package Control](https://packagecontrol.io)
- 插件：OmniMarkupPreviewer
- theme：[Monokai Extended](https://github.com/jonschlinkert/sublime-monokai-extended)
- win7需要解决输入法光标跟随，插件：IMESupport
- win7字体修改：[YaHei Consolas Hybrid](https://github.com/yakumioto/YaHei-Consolas-Hybrid-1.12)
- Ubuntu 17.04 需要解决fcitx输入问题：[Sublime Text 3 Input Method(Fcitx)](https://github.com/lyfeyaj/sublime-text-imfix)

## 界面

- 使用file-openfolder 打开文件，就能实现类似evernote的树形侧边栏界面
- 快捷键 ctrl+kb，开关侧边栏
- 宽屏用户，可以实现分栏打开多个文件，快捷键alt+shift+1/2/3/4/5/8/10，各种分屏方式
- F11 全屏，shift+F11 无干扰全屏模式

## 收集

因为没有足够的移动端支持，所以要配合日程工具、todolist工具来收集，比如滴答清单。

收集后定期整理，否则堆积信息也是垃圾，最早用印象笔记就剪藏了许多文章，最后一次性删掉了。

## 搜索

- ctrl+P，goto anything，可以快速预览并打开文件
- ctrl+shift+F，默认搜索已打开的笔记目录，全文搜索
- 结合第二条，可以在特定文档加入**标签**，比如 #github
- ctrl+R，可以列出当前文档的markdown层级标签，长文编辑很方便

## 其他操作技巧

- 列编辑：鼠标中键选取（linux下是右键+shift）

## 预览和输出

- ctrl+alt+O，在浏览器预览当前文件

## 同步

- dropbox 或 坚果云
- git，版本可控。私有git推荐 bitbucket

---

参考文档：

- [st3中文技巧](https://liam0205.me/2013/11/11/Sublime-elegant/)
- [st3添加右键菜单](https://gist.github.com/roundand/9367852)

## 更新记录

> from 20170629
> 20170929 更新Ubuntu下使用细节，已经高亮显示插件