#!/usr/bin/env python3
"""
构建和发布脚本
用于将 whois-mcp-server 发布到 PyPI
"""

import subprocess
import sys
import os

def run_command(command, description):
    """运行命令并处理错误"""
    print(f"正在 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 成功")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失败: {e}")
        print(f"错误输出: {e.stderr}")
        return None

def main():
    """主函数"""
    print("🚀 开始构建和发布 whois-mcp-server...")
    
    # 检查是否在正确的目录
    if not os.path.exists("pyproject.toml"):
        print("❌ 错误: 请在项目根目录运行此脚本")
        sys.exit(1)
    
    # 清理之前的构建
    run_command("rm -rf build/ dist/ *.egg-info/", "清理之前的构建文件")
    
    # 构建项目
    if not run_command("python -m build", "构建项目"):
        sys.exit(1)
    
    # 检查构建结果
    if not os.path.exists("dist/"):
        print("❌ 构建失败: dist/ 目录不存在")
        sys.exit(1)
    
    print("\n📦 构建完成！")
    print("📁 构建文件:")
    for file in os.listdir("dist/"):
        print(f"   - {file}")
    
    # 询问是否发布到 PyPI
    response = input("\n是否要发布到 PyPI? (y/N): ").strip().lower()
    if response == 'y':
        # 发布到 PyPI
        if not run_command("python -m twine upload dist/*", "发布到 PyPI"):
            sys.exit(1)
        print("🎉 发布成功！")
    else:
        print("📦 构建完成，未发布到 PyPI")
        print("如需发布，请运行: python -m twine upload dist/*")

if __name__ == "__main__":
    main() 