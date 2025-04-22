#!/bin/bash

# install.sh - 一键安装 SOAR-Lite 项目的依赖项

set -e  # 如果命令出错，则退出脚本

echo "🔧 开始安装 SOAR-Lite 项目的依赖项..."

# 更新包列表
echo "📦 更新系统包列表..."
sudo apt-get update

# 安装 Python3 和 pip3（如果尚未安装）
echo "🐍 检查并安装 Python3 和 pip3..."
sudo apt-get install -y python3 python3-pip

# 安装 virtualenv（用于创建虚拟环境）
echo "🛠️ 安装 virtualenv..."
sudo pip3 install virtualenv

# 创建虚拟环境
echo "📁 创建虚拟环境 'venv'..."
virtualenv venv

# 激活虚拟环境
echo "✅ 激活虚拟环境..."
source venv/bin/activate

# 安装 requirements.txt 中的依赖项
echo "📦 安装项目依赖项..."
pip install -r requirements.txt

echo "🎉 安装完成！要激活虚拟环境，请运行："
echo "source venv/bin/activate"
