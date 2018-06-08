from typing import List
import session
import util

# 教室使用情况API的基础URL
baseUrl: str = "http://tm.bnuz.edu.cn/api/"

# 教学楼API URL
buildingsUrl: str = baseUrl + "place/buildings"

# 教室API URL
placesUrl: str = buildingsUrl + "/:building/places"

# 教室使用情况API URL
usagesUrl: str = placesUrl + "/:place/usages"


# 教学楼
class Building(object):
    __slots__ = (
        "name"  # 教学楼名
    )

    def __init__(self, name: str):
        self.name = name


# 教室
class Place(object):
    __slots__ = (
        "name",  # 教室名
        "seat",  # 教室座位数量
        "id",  # 教室ID
        "type"  # 教室类型
    )

    def __init__(self, _dict: dict):
        util.dictToObject(self, _dict)


# 教室使用情况
class Usage(object):
    __slots__ = (
        "startWeek",  # 开始星期
        "endWeek",  # 结束星期
        "oddEven",  # 是否是单双周（0:非单双，1:单周，2:双周）
        "dayOfWeek",  # 星期n
        "startSection",  # 从第几节开始使用
        "totalSection",  # 总共使用n节课
        "description",  # 描述
        "type",  # 使用类型
        "department",  # 使用部门/学院
    )

    def __init__(self, _dict: dict):
        util.dictToObject(self, _dict)


# 获取教学楼
def getBuildings() -> List[Building]:
    response = session.get(buildingsUrl)

    json = response.json()
    return list(map(lambda name: Building(name), json["buildings"]))


# 获取教室
def getPlaces(building: Building) -> List[Place]:
    url = placesUrl.replace(":building", building.name)
    response = session.get(url)

    json = response.json()
    return list(map(lambda place: Place(place), json))


# 获取教室使用情况
def getUsages(building: Building, place: Place) -> List[Usage]:
    url = usagesUrl.replace(":building", building.name).replace(":place", place.id)
    response = session.get(url)

    json = response.json()
    return list(map(lambda usage: Usage(usage), json))


# 打印考试周的考试科目
def printTestClass():
    print("开始获取考试科目信息...\n")

    buildings = getBuildings()

    for building in buildings:
        places = getPlaces(building)

        for place in places:
            usages = getUsages(building, place)

            for usage in usages:
                startWeek = usage.startWeek
                _type = usage.type
                if _type == "ks" and startWeek == 18 or startWeek == 19:
                    department = usage.department
                    subject = usage.description
                    dayOfWeek = usage.dayOfWeek
                    startSection = usage.startSection
                    totalSection = usage.totalSection
                    endSection = startSection + totalSection - 1

                    print("{} {} 第{}周 星期{} 第{} - {}节".format(department, subject,
                                                             startWeek, dayOfWeek,
                                                             startSection, endSection))

    print("\n考试科目获取完毕，祝您愉快 >_+<")
