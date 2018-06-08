# 将Dict设置到Object中
def dictToObject(obj: object, _dict: dict):
    for name, value in _dict.items():
        setattr(obj, name, value)
