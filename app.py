from flask import Flask, render_template, jsonify, request
from requests import get
from model import Weather
from os import getenv

app = Flask(__name__)

def get_weather(city: str):
    api_key = getenv('API_KEY')
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = get(url)
    return response.json()

def render_icon_weather(icon: str):
    return f"https://openweathermap.org/img/w/{icon}.png"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    icon = None
    if request.method == 'POST':
        params = request.form
        response = get_weather(params['city'])
        weather = Weather(response)
    return render_template('index.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
