#!/usr/bin/python3
import os

print('hello')
path = '/Users/flannchen/OpenCVTutorials'
for _, dirs, _ in os.walk(path, topdown=True):
    #DPS读取文件的子文件并打印文件名
    for dir in dirs:
        print(dir)
        files = os.listdir(path+"/"+dir)
        files.sort()
        for file in files:
            print("  - [%s](%s/%s)" %(file, dir, file))