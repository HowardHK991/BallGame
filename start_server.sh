#!/bin/bash

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 检查端口是否被占用
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "端口8000已被占用，尝试关闭..."
    kill -9 $(lsof -ti:8000)
    sleep 1
fi

# 默认端口
PORT=8000

# 解析命令行参数
while getopts "p:" opt; do
  case $opt in
    p) PORT="$OPTARG"
      ;;
    \?) echo "无效的选项: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# 启动服务器
echo "启动服务器..."
python3 server.py -p $PORT 