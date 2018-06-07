from html.parser import HTMLParser
import session

# TMS系统登陆URL
loginUrl = "http://tm.bnuz.edu.cn/uaa/login"


# 解析登陆页的HTML，用于获取表单中的CSRF Token
class MyHtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._token = None

    # CSRF Token
    @property
    def token(self):
        return self._token

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):

        # 从标签中获取属性值
        def _attr(attrName):
            for attr in attrs:
                if attr[0] == attrName:
                    return attr[1]
            return None

        # 获取表单中的CSRF Token
        # input -> id="csrf_token":
        if tag == "input":
            for name, value in attrs:
                if name == "id" and value == "csrf_token":
                    self._token = _attr("value")


# 获取CSRF Token，用于进行安全验证
def getCsrfToken():
    response = session.get(loginUrl)
    parser = MyHtmlParser()
    parser.feed(response.text)
    parser.close()

    return parser.token


# 登陆TMS系统
def login():
    token = getCsrfToken()

    # 获取账号与密码
    username = input("输入教务账号：")
    password = input("输入教务密码：")

    data = {
        'username': username,
        'password': password,
        '_csrf': token
    }

    # 执行登陆
    session.post(loginUrl, data)
