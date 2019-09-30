# coding= UTF-8
from flask import Flask,render_template, request
import sys
import requests
import time
import threading 
import datetime
def getWheaterData():
    print('hello')
    url = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast"
    r = requests.get(url)
    global listData
    listData = r.json()
num=0
twoNum=False
def fun_timer():
  global t
  global num
  global twoNum
  timeHour = time.localtime(time.time()).tm_hour
  timeMin = time.localtime(time.time()).tm_min
  print(timeHour,timeMin)
  if num==360:
    getWheaterData()
  if timeHour == 0 and timeMin >2 and twoNum==False:
    getWheaterData()
    twoNum=True
  if timeHour == 1 and twoNum==True:
    twoNum=False
  t = threading.Timer(1,fun_timer)
  t.start()  
getWheaterData()
t = threading.Timer(1,fun_timer)  #首次启动
t.start()  

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>首页</h1>"
#Adding data
@app.route("/weather",methods=['POST','GET'])
def get_value():
    # //获取系统时间
    timeNow = time.strftime('%H:%M:%S',time.localtime(time.time()))
    timeNowStr = str(timeNow)[0:2]
    print(timeNowStr)
    if request.method == 'POST':
        print("post")
    else:
      # 判断当前时间
        if '18'<timeNowStr<'23':
          weather = listData['items'][0]['periods'][0]['regions']['central'];#天气状况
        elif '12'<timeNowStr<'18':
          weather = listData['items'][0]['periods'][2]['regions']['central'];#天气状况          
        elif '06'<timeNowStr<'12':
          weather = listData['items'][0]['periods'][1]['regions']['central'];#天气状况
        else :
          weather = listData['items'][0]['periods'][0]['regions']['central'];#天气状况
        city = request.args.get('city')
        locations = request.args.get('locations')
        info = request.args.get('info')

        temp_low = listData['items'][0]['general']['temperature']['low']; #最低温度
        temp_high = listData['items'][0]['general']['temperature']['high'];#最高温度   

        humi_low = listData['items'][0]['general']['relative_humidity']['low']; #最低相对湿度
        humi_high = listData['items'][0]['general']['relative_humidity']['high'];#最高相对湿度

        winds_min = listData['items'][0]['general']['wind']['speed']['low']; #最小风力
        winds_max = listData['items'][0]['general']['wind']['speed']['high'];#最大风力       

        # weather/temp_high/temp_low/humi_high/humi_low/winds_max/winds_min
        returnData = ''
        if info.find('weather')!=-1:
          returnData += weather+'/'
        if info.find('temp_high')!=-1:
          returnData += str(temp_high)+'/'
        if info.find('temp_low')!=-1:
          returnData += str(temp_low)+'/'
        if info.find('humi_high')!=-1:
          returnData += str(humi_high)+'/'
        if info.find('humi_low')!=-1:
          returnData += str(humi_low)+'/'
        if info.find('winds_min')!=-1:
          returnData += str(winds_min)+'/'
        if info.find('winds_max')!=-1:
          returnData += str(winds_max)+'/'
    sys.stdout.flush()
    return returnData

if __name__ == "__main__":
  app.run(port=1125,debug=False) #use_reloader=False
     

