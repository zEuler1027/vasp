#!/bin/bash

# 遍历当前目录下的所有子目录
for dir in */; do
    # 进入子目录
    cd "$dir"
    # 删除除了INCAR和POSCAR以外的所有文件
    find . -type f ! -name 'INCAR' ! -name 'POSCAR' -delete
    # 返回上级目录
    cd ..
done
