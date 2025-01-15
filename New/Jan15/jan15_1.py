import requests
import json

# Function to fetch weather forecast data
def fetch_weather_forecast(city_name, api_key, days, temperature, wind_speed, weather_description):
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m"
    response = requests.get(url)

   #Check if the request was successful 
    if response.status_code == 200:
        print("Weather forecast data fetched successfully.")
        data = response.json()
        for info in data['items']:
            city_name = info['city_name']
            temperature = info['temperature']
            wind_speed = info['wind_speed']
            weather_description = info.get['weather_description']
            print(f"City: {city_name}\nTemperature: {temperature}\nWind Speed: {wind_speed}\nWeather Description: {weather_description}\n")
        return response.json()  # Return the JSON data
    else:
        print(f"Failed to fetch weather data. Error: {response.status_code}")
        return None  # Return None if the request fails

# Function to save data to a file
def save_weather_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)  
    print(f"Weather forecast data saved to {file_name}")

# Main script
if __name__ == "__main__":  
    API_KEY = "your_api_key_here"  # Replace with your actual API key if needed
    city_name = print(input("Enter your city name: ")) 
    forecast_days = 3  # Forecast for the next 3 days
    temperature = 25
    wind_speed = 10
    weather_description = "Sunny"
    
    forecast_data = fetch_weather_forecast(city_name, API_KEY, forecast_days, temperature, wind_speed, weather_description)
   
    if forecast_data:
        save_weather_data(forecast_data, "forecast_data.json")

