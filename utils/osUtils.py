import os
from distutils.dir_util import copy_tree
from shutil import copyfile
import tarfile

filePath = os.path.dirname(__file__)
newFilePath = filePath + "/dir1/dir2"

#  eg1 创建目录
# if not os.path.exists(newFilePath):
#     os.makedirs(newFilePath)

#  eg2 拷贝目录
# copy_tree(newFilePath, newFilePath.replace("dir", "dirChanged")

#  eg3 创建写文件
# fileObj = open(newFilePath + "/test.txt", "a")
# fileObj.write("hello im here")
# fileObj.close()

#  eg4 拷贝文件
# copyfile(newFilePath + "/test.txt", newFilePath + "/test2.txt")

#  eg5 获取目录下文件
# contens = [os.path.join(newFilePath, file) for file in os.listdir(newFilePath)]
# print(contens)

#  eg6 创建压缩文件
with tarfile.open(newFilePath + "/test_tar.rar", "a") as testTar:
    testTar.add(newFilePath, arcname=os.path.basename(newFilePath))
testTar.close()