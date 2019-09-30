# coding= UTF-8
from flask import Flask,render_template, request
import sys

app = Flask(__name__)
@app.route("/http://192.168.0.120/weather?city=Singapore&locations=Pulau_Ubin&info=weather/temp_hightemp_low/humi_high/humi_low/winds_max/winds_min/")
def index():
    return "首页"

#Adding data
@app.route("/input",methods=['POST','GET'])
def get_value():
    if request.method == 'POST':
        print("post")
        sensorid = int(request.form.get('id'))
        sensorvalue = float(request.form.get('val'))
    else:
        print("get")
        sensorid = int(request.args.get('city'))
        sensorvalue = float(request.args.get('val')) 
    print("sensorid = %d"%sensorid)
    print("sensorval = %f"%sensorvalue)
    sys.stdout.flush()
    return '30'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080,debug=True,threaded=True)

    /weather?city=Singapore&locations=Pulau_Ubin&info=weather/temp_high/temp_low/humi_high/humi_low/winds_max/winds_min