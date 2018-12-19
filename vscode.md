# vscode笔记

## 快捷键

[官方cheetsheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)，我常用的：

- ctrl + B 切换侧边栏显示
- 列选择：光标处按下左键，然后按住shift+alt，拖动

## markdown使用

### 预览markdown

1. ctrl+shift+V，新标签预览模式。ctrl+K V（松开ctrl），分屏显示预览窗口。
2. 侧边栏有 outline view，可以显示大纲
3. 实测vscode内置的css样式表，与微信编辑器不匹配，可以安装下面的插件或者修改css文件。

#### 修改css

1. 下载一份[github-markdown-css](https://github.com/sindresorhus/github-markdown-css)里的 github.css 到workspace根目录
2. 进入设置-workspace setting，搜markdown，编辑setting.json。也可以直接编辑本地 `.vscode` 目录下的 setting.json
3. 添加如下：

```
{// Github style for all VSCode theme
"markdown.styles": [
    "github.css"
]
}
```

#### 插件模式

1. 安装 Instant Markdown 扩展
2. 编辑 user setting，修改为`"instantmarkdown.autoOpenBrowser": false,`
3. 添加快捷键：搜索`Instant Markdown: Open Browser`，添加 ctrl+alt+O

### 导出

#### PDF

安装插件：Markdown PDF

- 安装后会下载chromium，可以自定义指向本地浏览器，修改`markdown-pdf.executablePath` 到 `/usr/bin/google-chrome-stable`
- 对格式不满意可以修改css，参考[vscode-markdown-style](https://github.com/raycon/vscode-markdown-style)

