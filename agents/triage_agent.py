from swarm import Agent
from agents.tools import transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather
from prompts import TRIAGE_INSTRUCTIONS

def instructions(context_variables):
    user_name = context_variables["user_name"]
    print(f"User name is: {user_name}")
    return (f"Help {user_name} with their request. "
            "If it's a news-related request, call the 'news_agent' to fetch articles. "
            "For task management, use the 'task_manager_agent'."
            "If its weather related, call the 'weather_agent'.")

triage_agent = Agent(
    name = "Triage Agent",
    instructions = TRIAGE_INSTRUCTIONS,
    model = "llama3.1",
    tools = [transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather]
)

triage_agent.functions = [transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather]
