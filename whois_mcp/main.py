import os
import requests
from typing import Dict, Any
from flask import Flask, request, jsonify

app = Flask(__name__)
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

@app.route("/whois")
def whois_query():
    """Whois 查询接口"""
    try:
        domain = request.args.get("domain")
        if not domain:
            return jsonify({
                "code": -1,
                "message": "domain参数不能为空",
                "data": None
            }), 400

        if not API_KEY:
            return jsonify({
                "code": -1,
                "message": "Missing API Key",
                "data": None
            }), 500

        # 创建模型和上下文
        domain_model = DomainModel(domain)
        whois_context = WhoisContext(domain_model)
        
        # 通过上下文获取结果
        result = whois_context.get_whois_info()
        
        return jsonify({
            "code": 0,
            "message": "success",
            "data": result
        })

    except Exception as ex:
        return jsonify({
            "code": -1,
            "message": f"系统异常：{str(ex)}",
            "data": None
        }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)