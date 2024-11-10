from swarm import Swarm
from agents.triage_agent import triage_agent
from agents.news_agent import news_agent
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from utils import run_demo_loop

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = Swarm()

if __name__ == "__main__":
    print("Welcome to the Swarm Mind! How can I help you today?")
    run_demo_loop(triage_agent)
