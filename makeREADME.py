#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 读取当前目录生成README.md

import os
import sys
import datetime
from pypinyin import lazy_pinyin

f = open('README.md','w',encoding='utf-8')
f.write('# metaldudu docs\n') # 页面H1
files = os.listdir(os.getcwd())
files.sort()

for i in files:
    subpath = os.path.join(os.getcwd(),i)
    if (i[0] == '.'):
        pass #排除隐藏目录
    elif os.path.isdir(subpath):
        f.write('\n\n## ' + i + '\n\n')#文件夹
        subfiles = os.listdir(subpath)
        subfiles.sort(key=lambda char: lazy_pinyin(char)[0][0]) # 实现中文排序
        for j in subfiles:
            if j != 'README.md':
                if j != 'makeREADME.py':
                    link = '- [' + j.replace('.md', '') + '](' + i + '/' + j + ')\n'
                    f.write(link)
print ('done!')

f.write('\n--- \n\nUPDATE: ' + str(datetime.date.today()))
f.close()
