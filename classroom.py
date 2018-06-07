import session

# 教室使用情况API的基础URL
baseUrl = "http://tm.bnuz.edu.cn/api/"

# 教学楼API URL
buildingsUrl = baseUrl + "place/buildings"

# 教室API URL
placesUrl = buildingsUrl + "/:building/places"

# 教室使用情况API URL
usagesUrl = placesUrl + "/:place/usages"


# 获取教学楼
def getBuildings():
    response = session.get(buildingsUrl)
    return response.json()


# 获取教室
def getPlaces(building):
    url = placesUrl.replace(":building", building)
    response = session.get(url)
    return response.json()


# 获取教室使用情况
def getUsages(building, place):
    url = usagesUrl.replace(":building", building).replace(":place", place)
    response = session.get(url)
    return response.json()


# 打印考试周的考试科目
def printTestClass():
    print("开始获取考试科目信息...\n")

    buildings = getBuildings()

    for building in buildings['buildings']:
        places = getPlaces(building)

        for place in places:
            usages = getUsages(building, place["id"])

            for usage in usages:
                startWeek = usage["startWeek"]
                _type = usage["type"]
                if _type == "ks" and startWeek == 18 or startWeek == 19:
                    department = usage["department"]
                    subject = usage["description"]
                    dayOfWeek = usage["dayOfWeek"]
                    startSection = usage["startSection"]
                    totalSection = usage["totalSection"]
                    endSection = startSection + totalSection - 1

                    print("{} {} 第{}周 星期{} 第{} - {}节".format(department, subject,
                                                             startWeek, dayOfWeek,
                                                             startSection, endSection))

    print("\n考试科目获取完毕，祝您愉快 >_+<")
