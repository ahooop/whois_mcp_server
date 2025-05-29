# WHOIS MCP 服务
## 简介
WHOIS MCP (Model Context Protocol) 服务是一个基于 Python 开发的 WHOIS 查询服务器，提供域名信息查询功能。该服务采用 Flask 框架构建，通过模型上下文协议处理域名信息。

## 功能特点
- 支持标准 WHOIS 协议查询
- RESTful API 接口
- 轻量级设计
- 易于部署和扩展
## 安装方法
### 使用 pip 安装
```bash
pip install whois-mcp-server
 ```

### 从源码安装
```bash
git clone https://github.com/your-username/whois-mcp-server.git
cd whois-mcp-server
python setup.py install
 ```

## 使用方法
### 启动服务
```bash
whois-mcp-server
 ```

默认情况下，服务器将在 localhost:5000 上运行。

### API 端点 1. WHOIS 查询
- 端点 : /whois
- 方法 : GET
- 参数 :
  - domain : 要查询的域名
- 示例请求 :
  ```plaintext
  GET /whois?domain=example.com
   ```
- 响应格式 : JSON 2. 健康检查
- 端点 : /health
- 方法 : GET
- 响应 : 服务器状态信息
## 配置选项
服务器支持通过环境变量进行配置：

- WHOIS_SERVER_HOST : 服务器监听地址（默认：0.0.0.0）
- WHOIS_SERVER_PORT : 服务器端口（默认：5000）
- WHOIS_TIMEOUT : 查询超时时间（默认：10秒）
## 开发说明
### 依赖项
- Python 3.6+
- Flask
- Requests
### 项目结构
```plaintext
whois-mcp-server/
├── whois_mcp/
│   ├── __init__.py
│   ├── main.py
│   └── server.py
├── setup.py
└── README.md
 ```

## 许可证
MIT License

## 贡献指南
欢迎提交 Pull Requests 和 Issues。在提交代码前，请确保：

1. 代码符合 PEP 8 规范
2. 添加适当的测试用例
3. 更新相关文档
## 技术支持
如有问题，请通过 GitHub Issues 提交。