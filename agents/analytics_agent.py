from swarm import Agent
import json
from agents.tools import transfer_back_to_triage, run_sql_select_statement
from prompts import get_sql_agent_instructions
import sqlite3
import logging

with open("sales_and_customer_schema.sql", "r") as table_schema_file:
    table_schemas = table_schema_file.read()


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


analytics_agent = Agent(
    name="Analytics Agent",
    instructions=get_sql_agent_instructions(table_schemas) + "\n\nHelp the user gain insights from the data with analytics. Be super accurate in reporting numbers and citing sources.",
    model='gpt-4o-mini',
    tools=[run_sql_select_statement]
)

analytics_agent.functions = [run_sql_select_statement, transfer_back_to_triage]