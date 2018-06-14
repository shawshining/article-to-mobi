#!/usr/bin/env python3
import os
import platform
import shutil
import sys

from article import Article
from file import File

abs_path = os.getcwd() + os.sep
book_name = sys.argv[1]
main_url = sys.argv[2]
file_name = book_name + '.mobi'


temp_path = abs_path + os.sep + 'temp' + os.sep
images = abs_path + os.sep + 'images'
cover = temp_path + 'images'

# 获取文章
art_obj = Article(main_url)
articles = art_obj.get_article()

# 输出文件
file = File()
file.out_mobi(temp_path, book_name, articles)

# 复制图书封面
if not os.path.exists(cover):
    shutil.copytree(images, cover)

# 生成 mobi 文件
if 'Windows' == platform.system():
    os.system(abs_path + 'windows-kindlegen' + os.sep + 'kindlegen.exe ' + temp_path + book_name + '.opf')
elif 'Darwin' == platform.system():
    os.system(abs_path + 'macOS-kindlegen' + os.sep + 'kindlegen ' + temp_path + book_name + '.opf')
else:
    print('Not supported OS type.')

# 创建成功，移除临时文件，也可注释掉最后一行，保留临时文件。
if os.path.exists(temp_path + file_name):
    shutil.move(temp_path + file_name, abs_path)
    shutil.rmtree(temp_path)
