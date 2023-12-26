from dotenv import load_dotenv, dotenv_values
from flask import Flask, render_template, request
import datetime as dt
import os
import requests

# Create Flask app
app = Flask(__name__)

load_dotenv()

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle weather data
@app.route('/weather', methods=['POST', 'GET'])
def weather():
    
    if request.method == 'POST':
        city = request.form['city']

        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = os.getenv("API_KEY")
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': api_key, 'units': 'metric'}

        # Make API request
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)

        curr_time = dt.datetime.now().strftime("%I:%M %p")
        # Extract relevant weather information
        weather_info = {
            'country': data['sys']['country'],
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
            'wind_speed' : data['wind']['speed'],
            'curr_time' : curr_time,
        }

        return render_template('weather.html', weather=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
