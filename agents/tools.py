import requests
import os
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transfer_to_task_manager():
    from agents.task_manager_agent import task_manager_agent 
    return task_manager_agent

def transfer_to_news_agent():
    from agents.news_agent import news_agent
    return news_agent

def transfer_back_to_triage():
    from agents.triage_agent import triage_agent
    return triage_agent

def transfer_to_weather():
    from agents.weather_agent import weather_agent
    return weather_agent

def get_weather(location, time="now"):
    """Get the current weather in a given location using OpenWeatherMap API."""
    logger.info(f"get_weather called with location: {location}, time: {time}")
    
    api_key = "weather-api-key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        weather_info = {
            "location": location,
            "temperature": str(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "time": time
        }
        
        logger.info(f"Weather info retrieved: {weather_info}")
        return json.dumps(weather_info)
    except Exception as e:
        logger.error(f"Error in get_weather: {str(e)}")
        return json.dumps({"error": f"Unable to fetch weather data: {str(e)}"})