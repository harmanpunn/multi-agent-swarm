# Multi-Agent System with OpenAI's Swarm Framework

This project demonstrates a multi-agent system utilizing OpenAI's Swarm framework. The system comprises specialized agents—News Agent, Task Manager Agent, Weather Agent, Analytics Agent, and Triage Agent—that collaborate to handle diverse user requests efficiently.

## Project Overview

OpenAI's Swarm framework facilitates the creation of modular, stateless agents capable of seamless handoffs. Each agent in this project is designed for a specific function:

- **News Agent**: Fetches relevant news articles.
- **Task Manager Agent**: Assists in organizing and managing tasks.
- **Weather Agent**: Provides real-time weather updates.
- **Analytics Agent**: Accesses a database schema, interprets user queries (e.g., "Show me the revenue of each product"), generates, and executes queries to display results.
- **Triage Agent**: Routes user queries to the appropriate agent, ensuring efficient task handling.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`)

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/harmanpunn/swarm-mind.git
   cd swarm-mind
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt    
3. **Configure Environment Variables**:
   ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    OPENWEATHER_API_KEY=your_openweather_api_key_here
Replace your_openai_api_key and your_openweather_api_key with your actual API keys.

4. **Running the Application**:
To run the application, execute the following command in your terminal:
    ```bash
    python3 app.py
The system will prompt you for input, and the Triage Agent will direct your request to the appropriate agent based on the query.