from typing import Any, Dict
import os
import requests

API_KEY = os.getenv("TAVILY_API_KEY")

class DomainModel:
    """域名模型类"""
    def __init__(self, domain: str):
        self.domain = domain

class WhoisContext:
    """WHOIS 查询上下文"""
    def __init__(self, model: DomainModel):
        self.model = model
        self.api_key = API_KEY
        self.base_url = 'https://openapi.chinaz.net/v1/1001/whois'

    def get_whois_info(self) -> Dict[str, Any]:
        """获取 WHOIS 信息"""
        api_params = {
            "APIKey": self.api_key,
            "ChinazVer": "1.0",
            "domain": self.model.domain
        }
        response = requests.get(self.base_url, params=api_params, timeout=60)
        return response.json()

def whois_query(domain: str) -> Dict[str, Any]:
    """Whois 查询接口
    Args:
        domain: 需要查询的域名
    Returns:
        查询结果字典
    """
    if not domain:
        return {
            "code": -1,
            "message": "domain参数不能为空",
            "data": None
        }
    if not API_KEY:
        return {
            "code": -1,
            "message": "Missing API Key",
            "data": None
        }
    domain_model = DomainModel(domain)
    whois_context = WhoisContext(domain_model)
    try:
        result = whois_context.get_whois_info()
        return {
            "code": 0,
            "message": "success",
            "data": result
        }
    except Exception as ex:
        return {
            "code": -1,
            "message": f"系统异常：{str(ex)}",
            "data": None
        }

def main():
    """主函数入口点"""
    print("WHOIS MCP Server")
    print("这是一个 WHOIS 查询工具")
    print("使用方法: from whois_mcp.__main__ import whois_query")
    print("示例: result = whois_query('example.com')")

if __name__ == "__main__":
    main() 