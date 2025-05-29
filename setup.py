from setuptools import setup

setup(
    name="whois-mcp-server",  # PyPI包名（允许连字符）
    version="0.1.0",
    packages=["whois_mcp"],  # 包目录名（下划线）
    entry_points={
        "console_scripts": [
            "whois-mcp-server = whois_mcp.server:main"  # 命令行工具
        ]
    }
)