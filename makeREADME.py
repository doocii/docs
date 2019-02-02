#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 读取当前目录生成README.md

import os
import sys

f = open('README.md','w',encoding='utf-8')
files = os.listdir(os.getcwd())
files.sort()

for i in files:
    fpath = os.path.join(os.getcwd(),i)
    if (i[0] == '.'):
        pass#排除隐藏目录
    elif os.path.isdir(fpath):
        f.write('\n\n## ' + i + '\n\n')#文件夹
        for j in os.listdir(fpath):
            if j != 'README.md' and j != 'makeREADME.py':
                link = '- [' + j.replace('.md', '') + '](' + j + ')\n'
            f.write(link)
print ('done!')

f.close()
