from swarm import Agent
from agents.tools import transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather, transfer_to_analytics_agent
from prompts import TRIAGE_INSTRUCTIONS

triage_agent = Agent(
    name = "Triage Agent",
    instructions = TRIAGE_INSTRUCTIONS,
    model = "gpt-4o",
    tools = [transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather, transfer_to_analytics_agent]
)

triage_agent.functions = [transfer_to_task_manager, transfer_to_news_agent, transfer_to_weather, transfer_to_analytics_agent]
