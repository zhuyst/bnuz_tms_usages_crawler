import requests

# 欺骗用Headers
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
}

# 启动Session，自动响应Set-Cookie头
session = requests.Session()

# 将Headers设置到session中
session.headers.update(headers)


# 使用session发起GET请求
def get(url, **kwargs):
    return session.get(url, **kwargs)


# 使用session发起POST请求
def post(url, params=None, **kwargs):
    return session.post(url, params, **kwargs)
