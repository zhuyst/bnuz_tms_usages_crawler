import classroom
import login

loginResult = login.login()
if loginResult:
    classroom.printTestClass()
