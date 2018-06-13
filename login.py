from lxml import html
import session

# TMS系统登陆URL
loginUrl = "http://tm.bnuz.edu.cn/uaa/login"

# 登陆失败时的URL
loginFailUrl = loginUrl + "?error"


# 获取CSRF Token，用于进行安全验证
def getCsrfToken():
    response = session.get(loginUrl)
    tree = html.fromstring(response.text)
    token = tree.xpath("//input[@id='csrf_token']")[0].value
    return token


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
    response = session.post(loginUrl, data)
    if response.url == loginFailUrl:
        print("账号或密码错误！")
        return False
    else:
        print("登陆成功")
        return True
