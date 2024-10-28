from swarm import Agent
import json
from agents.tools import transfer_back_to_triage
from duckduckgo_search import DDGS
from datetime import datetime
from prompts import NEWS_INSTRUCTIONS


current_date = datetime.now().strftime("%Y-%m")

# Create Internet Search Tool
def get_news_articles(topic: str):
    print(f"Running DuckDuckGo search for {topic}")

    # Initialize DuckDuckGo search client
    ddgs = DDGS()

    # Search for news articles
    search_results = ddgs.text(f'{topic} {current_date}', max_results=5)

    if search_results:
        news_results = "\n\n".join([f"Title: {result['title']}\nURL: {result['href']}\nDescription: {result['body']}" for result in search_results])
        return news_results
    else:
        return f"Not able to find any news articles for {topic} on {current_date}"

# News agent that will fetch news
news_agent = Agent(
    name="News Agent",
    instructions=NEWS_INSTRUCTIONS,
    tools=[get_news_articles, transfer_back_to_triage],
    model='llama3.1',
)

news_agent.functions = [get_news_articles, transfer_back_to_triage]