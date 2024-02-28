import os
import random
import string

import requests
from flask import Flask, request, Response

app = Flask(__name__)
alphabet = string.ascii_letters + string.digits

# 获取环境变量
app.config["HOST"] = os.getenv("HOST", "hi77-overseas.mangafuna.xyz")
app.config["APIKEY"] = os.getenv("APIKEY", ''.join(random.sample(string.ascii_letters + string.digits, 32)))


app.logger.info("APIKEY: %s", app.config["APIKEY"])

# HOST = "hi77-overseas.mangafuna.xyz"
# APIKEY = "9AsyfnMfmUQNBKGj8sRrbY8T5VgZN3bd8UoL2WXMkbTxNjyXqyu8vjuw6qDck9xs"


# 此函数用于检查code是否正确
def check_code(code):
    # 假设有效的code为"12345"
    return code == app.config["APIKEY"]


@app.route('/', methods=['GET'])
def get_status():
    return Response("Server is up", status=200)


@app.route('/proxy', methods=['GET'])
def proxy():
    # 从GET请求中读取code和url参数
    code = request.args.get('code')
    url = request.args.get('url')

    # 校验code是否正确
    if not check_code(code):
        return Response("Invalid code.", status=403)

    if app.config["HOST"] not in url:
        return Response("Invalid url.", status=403)

    try:
        # 向目标URL发送GET请求，并获取响应
        response = requests.get(url, headers={'Host': app.config["HOST"]})

        # 将目标URL的响应内容返回给客户端
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.RequestException as e:
        # 如果请求目标URL时出现异常，返回错误信息
        return Response("Failed to retrieve content from the URL.", status=500)


if __name__ == '__main__':
    app.run()
