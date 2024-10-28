from swarm import Agent
import json
from agents.tools import transfer_back_to_triage, get_weather
import requests
import logging
from prompts import WEATHER_INSTRUCTIONS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

weather_agent = Agent(
    name="Weather Agent",
    instructions=WEATHER_INSTRUCTIONS,
    model="llama3.1",
    tools=[get_weather]
)

weather_agent.functions = [get_weather, transfer_back_to_triage]