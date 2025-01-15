import requests
import json

# Function to fetch weather forecast data
def fetch_weather_forecast(city, api_key, days):
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2mt"
    response = requests.get(url)
    
    city_coords = {
        "New York": {"latitude": 40.7128, "longitude": -74.0060},
        "Berlin": {"latitude": 52.52, "longitude": 13.41},
    }
    
    if city not in city_coords:
        print(f"City {city} not found in predefined coordinates.")
        return None

    latitude = city_coords[city]["latitude"]
    longitude = city_coords[city]["longitude"]

    # Construct the API request URL
    url = f"{url}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

    # Send the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Weather forecast data fetched successfully.")
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
    city_name = "New York"  
    forecast_days = 3  # Forecast for the next 3 days
    
    forecast_data = fetch_weather_forecast(city_name, API_KEY, forecast_days)
   
    if forecast_data:
        save_weather_data(forecast_data, "forecast_data.json")
