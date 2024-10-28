from swarm import Swarm
from agents.triage_agent import triage_agent
from agents.news_agent import news_agent
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from swarm.repl import run_demo_loop


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# model_name = os.getenv("OPENAI_MODEL_NAME")
# base_url = os.getenv("OPENAI_BASE_URL")
current_date = datetime.now().strftime("%Y-%m")

client = Swarm()

def pretty_print_messages(messages) -> None:
    for message in messages:
        if message["role"] != "assistant":
            continue

        # print agent name in blue
        print(f"\033[94m{message['sender']}\033[0m:", end=" ")

        # print response, if any
        if message["content"]:
            print(message["content"])

        # print tool calls in purple, if any
        tool_calls = message.get("tool_calls") or []
        if len(tool_calls) > 1:
            print()
        for tool_call in tool_calls:
            f = tool_call["function"]
            name, args = f["name"], f["arguments"]
            arg_str = json.dumps(json.loads(args)).replace(":", "=")
            print(f"\033[95m{name}\033[0m({arg_str[1:-1]})")

def process_user_request(user_input, messages):

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.run(
        agent=triage_agent,
        messages=messages,
    )

    if not response.messages:
        raise Exception("No response from the agents")

    # Use pretty_print_messages to print the messages nicely
    pretty_print_messages(response.messages)

    last_message = response.messages[-1]["content"]
    agent_name = response.agent.name
    messages.extend(response.messages)

    print(f"Response from {agent_name}: {last_message}")

    return last_message

if __name__ == "__main__":
    print("Welcome to the Swarm Mind! How can I help you today?")
    # messages = []
    # while True:
    #     user_input = input("\033[90mUser\033[0m: ")
    #     if user_input.lower() == "exit":
    #         print("Exiting the Swarm Mind. Goodbye!")
    #         break
    #     process_user_request(user_input, messages)
    run_demo_loop(triage_agent)