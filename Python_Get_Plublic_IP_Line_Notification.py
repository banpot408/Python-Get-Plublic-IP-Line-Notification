from requests import get
import time
import datetime
import requests, json
import urllib.parse
import sys

LINE_ACCESS_TOKEN = "fgxqjVlCMbqWiwUTA9JHKxYzzrmfSWvvCgr3VhNpsUF"
URL_LINE = "https://notify-api.line.me/api/notify" 
data = [8,9,10,11,12,13,14,15,16,17,18]

def line_text(message):	
    msg = urllib.parse.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, data=msg)
    print(session_post.text)

current_time = datetime.datetime.now()
current_time_hour = current_time.hour
current_time_minute = current_time.minute
current_time_second = current_time.second
print ('current_time is:', current_time)
print ('current_time_hour is:', current_time_hour)
print ('current_time_minute is:', current_time_minute)
print ('current_time_second is:', current_time_second)
bit_send_line = False
bit_working_time_bit = False
while True:
    current_time = datetime.datetime.now()
    current_time_hour = current_time.hour
    current_time_minute = current_time.minute
    current_time_second = current_time.second
    #print ('------------------------------------------------------- current_time_second -----> ', current_time_second)
    if current_time_minute == 0 and bit_send_line == False:
        bit_send_line = True
        ip = get('https://api.ipify.org').text
        datetime_object = datetime.datetime.now()    
        #print ('My public IP address is:', ip, 'date time is :', datetime_object)
        if bit_working_time_bit == True:
            public_IP = ('OVSys public IP address is:'+ ip)
            line_text(public_IP)
        else:
            print ('My public IP address is:', ip, 'date time is :', datetime_object)
		
    if current_time_minute > 0 and bit_send_line == True:
        bit_send_line = False
		
    if current_time_hour in data:
        bit_working_time_bit = True
        print('True')
        print ('----------> current_time_second ----------> ', current_time_second, '----------> send line on working time is ---------->  True', '----------> current_time_hour ----------> ', current_time_hour)
    else:
        bit_working_time_bit = False
        print ('----------> current_time_second ----------> ', current_time_second, '----------> send line on working time is ---------->  False', '----------> current_time_hour ----------> ', current_time_hour)
        
    time.sleep(1)

	
##while True:
##    ip = get('https://api.ipify.org').text
##    datetime_object = datetime.datetime.now()    
##    print ('My public IP address is:', ip, 'date time is :', datetime_object)
##    time.sleep(1)

