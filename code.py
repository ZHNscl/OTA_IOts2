import time
import wifi
import json
import storage
import set_iot
import socketpool
from secrets import secrets  # hold your AP name and password
from set_iot import *
MAXBUF = 255
buf_tcp = bytearray(MAXBUF)  # the received buffer for TCP server
# make a Wi-Fi connect firstly!
print("Connecting to a AP ..")  # connect to wifi
try:
    #wifi.radio.connect(secrets["ssid"], secrets["password"])
    SET.wifi_AP()
except ConnectionError:
    print("Please check /CIRCUITPY/secrets.py")
    #raise ConnectionError("No network with that ssid or error password")  #连接WIFI错误处理
print("Connected! my IP: {}".format(wifi.radio.ipv4_address))
# create a socketpool (Socket池!) with the Wi-Fi connect


while True:
    try:
        print("OK B")
        sock_tcp.settimeout(0.1)
        numsReceived = connectSocket.recv_into(buf_tcp)
        number = str(buf_tcp[:numsReceived])
        length = len(number)
        number = number[12 : length - 2]
        print(number)
        jsoning = json.loads(number)
        print(jsoning['ssid'],jsoning['password'])
        secrets['ssid']=jsoning['ssid']
        secrets['password']=jsoning['password']
        print(secrets)
        #file.write(secrets)
        #numsSent = connectSocket.send(buf_tcp[:numsReceived])
        #print("Send", buf_tcp[:numsSent], numsSent, "bytes to", clientAddr)
        with open('secrets.py','r') as file:
            print('xx')
            content = file.read()
            content = content[10:]
            data = "'''["+content+"]'''"
            print(content)
            print(type(content))
            data = json.loads(content)
            print(type(data))
            data['ssid']=secrets['ssid']
            data['password']=secrets['password']
            data = json.dumps(data)
            print(data)
            file.close()
            storage.remount('/',False)
            #print('AA')
            with open('secrets.py','w+') as file:
                file.write("secrets = "+str(data))
                file.close()
                storage.remount('/',True)
        #import wifi
        #from secrets import secrets
        #print(secrets["ssid"], secrets["password"])
        wifi.radio.enabled=False
        #time.sleep(0.5)
        #print(secrets["ssid"], secrets["password"])
        wifi.radio.enabled=True
        wifi.radio.connect(secrets["ssid"], secrets["password"])
        #print(secrets["ssid"], secrets["password"])
    except:
       time.sleep(0.1)
    # connectSocket.close()


