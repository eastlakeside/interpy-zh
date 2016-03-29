# -*- coding: utf-8 -*-

"""
这个文件是用于构建readthedocs的配置文件，

ReadTheDocs的规范：
1. 从docs目录读取所有文档 (已经在根目录下 ln -s . docs了)
2. 使用根目录下的mkdocs.yml作为目录

ReadTheDocs本地构建Gitbook的md文件： 
>>> pip install mkdocs
>>> mkdocs build --clean --site-dir _build/html
>>> mkdocs serve

福利： mkdocs构建好以后，可以直接publish到github pages
（目前github pages的自动生成只能使用单页md， 而Jekell构建又引入新的节点，不方便）

"""


# 从本地读取到Summary.md， 然后转译成mkdocs.yml
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'nature'
