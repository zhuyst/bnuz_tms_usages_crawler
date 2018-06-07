from html.parser import HTMLParser
import session

loginUrl = "http://tm.bnuz.edu.cn/uaa/login"


class MyHtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._token = None

    @property
    def token(self):
        return self._token

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):

        def _attr(attrName):
            for attr in attrs:
                if attr[0] == attrName:
                    return attr[1]
            return None

        if tag == "input":
            for name, value in attrs:
                if name == "id" and value == "csrf_token":
                    self._token = _attr("value")


def getCsrfToken():
    response = session.get(loginUrl)
    parser = MyHtmlParser()
    parser.feed(response.text)
    parser.close()

    return parser.token


def login():
    token = getCsrfToken()

    username = input("输入教务账号：")
    password = input("输入教务密码：")

    data = {
        'username': username,
        'password': password,
        '_csrf': token
    }

    session.post(loginUrl, data)
