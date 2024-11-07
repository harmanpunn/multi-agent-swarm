from swarm import Agent
import json
from agents.tools import transfer_back_to_triage
from prompts import TASK_MANAGER_INSTRUCTIONS
import sqlite3


def add_task(description: str) -> str:
    print(f"Adding task: {description}")
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO tasks (description, status) VALUES (?, 'open')", (description,))
    conn.commit()
    conn.close()
    
    return f"Task added: {description}"


def list_tasks() -> str:
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, description, status FROM tasks")
    tasks = [{"id": row[0], "task": row[1], "status": row[2]} for row in cursor.fetchall()]
    
    conn.close()
    return json.dumps(tasks, indent=2)


task_manager_agent = Agent(
    name="Task Manager Agent",
    instructions=TASK_MANAGER_INSTRUCTIONS,
    tools=[add_task, list_tasks],   
    model='gpt-4o'
)

task_manager_agent.functions = [add_task, list_tasks, transfer_back_to_triage]