# 遍历当前目录的每个子文件夹
for dir in */ ; do
    # 检查是否为目录
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
        
        # 进入目录
        cd "$dir"

        # 生成KPOINTS
        echo "Generating KPOINTS..."
        vaspkit << EOF
102
1
0.04
EOF

        # 返回上一级目录
        cd ..
    fi
done

echo "All tasks completed!"
