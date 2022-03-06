
from flask import Flask,render_template,request
from matplotlib.style import use
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/data' ,methods=['GET','POST'])

def data():
    if request.method=='POST':
        city= request.form.get('city')

        user_api="2c752e9e4cca5dccee1562c2040c2bdf";
        complete_api_link_1="http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid={}".format(city,user_api)
        print(complete_api_link_1)

        app_link=requests.get(complete_api_link_1)

        api_data=app_link.json()

        lat=(api_data[0]['lat'])
        lon= abs( (api_data[0]['lon']))

        print("lat",lat)
        print("lon",lon)

        ans_api=("https://"+"api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,user_api))
        
        ans_data=requests.get(ans_api)

        
        ans_app_data=ans_data.json()
        temp=ans_app_data['main']['temp']

        ans_str="Current tem in your city {} is {}".format(city,temp-272.15)

        return (ans_str)

    return "hi"




app.run(debug=True)