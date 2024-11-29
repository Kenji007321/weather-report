import requests
from twilio.rest import Client

# OpenWeather api variables
endpoint = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "<enter_api_key>"
MY_LAT = "<enter_latitude>"
MY_LON = "<enter_longitude>"

# Twilio variables
account_sid = "<enter_id>"
auth_token = "<enter_token>"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
current_weather = weather_data["weather"][0]

def check_weather(weather_id_more, weather_id_less, icon):
    if current_weather["id"] >= weather_id_more and current_weather["id"] <= weather_id_less:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Current weather: {current_weather['main']}.\nWeather condition: {current_weather['description']}{icon}",
            from_="<enter_number>",
            to="<enter_number>",
        )
        print(message.status)
        
def check_unique_weather(weather_id, icon):
    if current_weather["id"] == weather_id:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Current weather: {current_weather['main']}.\nWeather condition: {current_weather['description']}{icon}",
            from_="<enter_number>",
            to="<enter_number>",
        )
        print(message.status)

# Thunderstorm
check_weather(200, 232, "⛈️")

# Drizzle
check_weather(300, 321, "🌧️")

# Rain
check_weather(500, 531, "☔")

# Snow
check_weather(600, 622, "❄️")

# Clouds
check_weather(801, 804, "☁️")

# Clear sky
check_unique_weather(800, "☀️")

# Mist
check_unique_weather(701, "🌫")

# Haze
check_unique_weather(721, "🌁")

# Fog
check_unique_weather(741, "🌫️")

# Squall
check_unique_weather(771, "💨")

# Tornado
check_unique_weather(781, "🌪️")

