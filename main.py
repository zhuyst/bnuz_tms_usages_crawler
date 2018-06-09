import classroom
import login

loginResult = login.login()

printTestClass = classroom.printTestClass()
next(printTestClass)
getUsages = classroom.getUsages(printTestClass)
next(getUsages)
getPlaces = classroom.getPlaces(getUsages)
next(getPlaces)
classroom.getBuildings(getPlaces)
