import eel
import requests
from duringClass import ClassHandle


eel.init('web')


@eel.expose
def login(id, password):
    response = requests.post('http://13.125.141.137:3000/api/login/student', data={
        'id': id,
        'password': password
    })
    response = response.json()
    return response


@eel.expose
def get_timeTable(classId):
    response = requests.get(
        'http://13.125.141.137:3000/api/time-table?classId=%d' % classId)
    response = response.json()
    return response


@eel.expose
def startClass(studentId, classId, accessToken, name):
    classHandler = ClassHandle(studentId, classId, accessToken, name)


eel.start('index.html')
