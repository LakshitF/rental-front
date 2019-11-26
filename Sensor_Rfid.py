import serial
import json
import requests
import urllib3
urllib3.disable_warnings()

dic = {"4 93 D3 83 C7": "abc@gmail.com", "96 70 4B 43 EE": "lak@gmail.com"}
url = 'http://rental-back.herokuapp.com/api/returnCycle'

# url="https://www.mocky.io/v2/5185415ba171ea3a00704eed"


def senddate(t, loc):
    print(dic[t])
    payload = {'locationId': loc, 'email': dic[t]}
    headers = {'content-type': 'application/json'}
    jfile = json.dumps(payload)
    x = requests.post(url, data=jfile, verify=False, headers=headers)
    y=x.json()
    while x.status_code != 200:
        print("API not successful, Trying again")
        x = requests.post(url, data=jfile, verify=False, headers=headers)
        y=x.json()
    if y["msg"]=="error100":
        print("Cycle Not Rented")
    if y["msg"]=="success":
        print("Cycle Retured")


ser = serial.Serial()
ser.port = 'COM3'
ser.buadrate = 9600
ser.open()
loc = input('Please Enter the Location: ')
while True:
    print("Waiting For RFID Tag")
    t = ser.readline()
    t = t.decode("utf-8")
    t = t.strip('\r\n')
    print("Tag Number: "+t)
    senddate(t, loc)
# print(t)
# print(type(t))
