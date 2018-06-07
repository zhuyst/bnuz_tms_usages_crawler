import session

baseUrl = "http://tm.bnuz.edu.cn/api/"
buildingsUrl = baseUrl + "place/buildings"
placesUrl = buildingsUrl + "/:building/places"
usagesUrl = placesUrl + "/:place/usages"


def getBuildings():
    response = session.get(buildingsUrl, headers=session.headers)
    return response.json()


def getPlaces(building):
    url = placesUrl.replace(":building", building)
    response = session.get(url, headers=session.headers)
    return response.json()


def getUsages(building, place):
    url = usagesUrl.replace(":building", building).replace(":place", place)
    response = session.get(url, headers=session.headers)
    return response.json()


def printTestClass():
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
