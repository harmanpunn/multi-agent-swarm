from swarm import Agent
import json
from agents.tools import transfer_back_to_triage
from prompts import TASK_MANAGER_INSTRUCTIONS

tasks = []

def add_task(description: str) -> str:
    print(f"Adding task: {description}")
    task = {"task": description, "status": "open"}
    tasks.append(task)
    print(f"Number of tasks: {len(tasks)}")
    return f"Task added: {description}"

def list_tasks():
    return json.dumps(tasks, indent=2)

task_manager_agent = Agent(
    name="Task Manager Agent",
    instructions=TASK_MANAGER_INSTRUCTIONS,
    tools=[add_task, list_tasks],   
    model='llama3.1'
)

task_manager_agent.functions = [add_task, list_tasks, transfer_back_to_triage]