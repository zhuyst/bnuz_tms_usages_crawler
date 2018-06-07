import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
}

session = requests.Session()
session.headers.update(headers)


def get(url, **kwargs):
    return session.get(url, **kwargs)


def post(url, params=None, **kwargs):
    return session.post(url, params, **kwargs)
