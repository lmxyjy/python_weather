# 新加坡天气接口
python封装新加坡天气接口

- **clone后运行命令python weather.py**
- **打开postman进行接口调试。接口地址localhost:1125**

**发送数据包返回值：**

	weather：天气状况
	temp_high:最高温度
	temp_low:最低温度
	humi_high:最高湿度
	humi_low:最低湿度
	winds_max:最大风速
	winds_min:最小风速

**请求格式：**

**1,发送get请求**

**2,格式:**

    localhost:1125/weather?city=Singapore&locations=Pulau_Ubin&info=weather/temp_high/temp_low/humi_high/humi_low/winds_max/winds_min