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

def transfer_to_analytics_agent():
    from agents.analytics_agent import analytics_agent
    return analytics_agent

def get_weather(location, time="now"):
    """Get the current weather in a given location using OpenWeatherMap API."""
    logger.info(f"get_weather called with location: {location}, time: {time}")
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        logger.error("API key not found. Make sure it's set in the .env file.")
        return json.dumps({"error": "API key not found"})
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
    

import sqlite3

def run_sql_select_statement(sql_statement: str) -> str:
    """Executes a SQL SELECT statement and returns formatted results."""
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()
    
    try:
        print(f"Executing SQL statement: {sql_statement}")
        cursor.execute(sql_statement)
        records = cursor.fetchall()

        if not records:
            return "No results found."
        
        # Get column names
        column_names = [description[0] for description in cursor.description]
        
        # Calculate column widths
        col_widths = [len(name) for name in column_names]
        for row in records:
            for i, value in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(value)))
        
        # Format the results
        result_str = ""
        
        # Add header
        header = " | ".join(name.ljust(width) for name, width in zip(column_names, col_widths))
        result_str += header + "\n"
        result_str += "-" * len(header) + "\n"
        
        # Add rows
        for row in records:
            row_str = " | ".join(str(value).ljust(width) for value, width in zip(row, col_widths))
            result_str += row_str + "\n"
        
    except sqlite3.Error as e:
        result_str = f"An error occurred: {e}"
    
    finally:
        conn.close()
    
    return result_str
