# WHOIS MCP 服务

这是一个基于 Python 和模型上下文协议（MCP）实现的域名可用性检查服务器。它提供 MCP 工具来检查域名的注册状态。

## 功能特点

- 域名注册状态检查
- 使用 WHOIS 和 DNS 双重验证
- 支持国际化域名（IDN）
- 简洁的输出格式
- 内置输入验证和错误处理

## 工具文档

### check_domain

检查域名的注册状态。

#### 输入格式

```json
{
  "domain": "example.com"
}
```

参数：
- `domain`: 要检查的域名
  - 域名最大长度为 255 个字符
  - 不允许空域名

#### 输出格式

```json
{
  "result": {
    "registered": true
  }
}
```

响应字段：
- `result`: 检查结果对象
  - `registered`: 布尔值
    - `true`: 域名已注册
    - `false`: 域名可用

#### 错误处理

在以下情况下，工具将返回错误：
1. 域名为空
2. 域名长度超过 255 个字符
3. 结果序列化失败

错误响应格式：
```json
{
  "error": "Error: domain cannot be empty"
}
```

#### 使用示例

检查域名：
> 请求
```json
{
  "domain": "example.com"
}
```

> 响应
```json
{
  "result": {
    "registered": true
  }
}
```

## MCP 服务器设置

#### 在 Claude Desktop 中配置 WHOIS MCP

修改您的 claude-desktop-config.json 文件，如下所示：

```json
{
  "mcpServers": {
    "whoismcp": {
      "command": "uvx",
      "args": [
        "whois-mcp-server"
      ]
    }
  }
}
```

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

## 开发说明

### 依赖项
- Python 3.6+
- Flask
- Requests
- python-whois
- dnspython

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