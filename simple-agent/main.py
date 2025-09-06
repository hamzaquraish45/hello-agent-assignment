# simple-agent/main.py
# Simple Agents SDK demo using Gemini via OpenAI-compatible Chat Completions

import os
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

# 1) Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# 2) Choose Gemini model
model = "gemini-2.5-flash-lite"

# 3) Define an OpenAI-compatible client for Gemini
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)
set_default_openai_client(external_client)

# 4) Register the Chat Completions style model
llm_model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)

# Disable tracing (not supported with Gemini)
set_tracing_disabled(True)

# 5) Define the agent
agent = Agent(
    name="simple_agent",
    instructions="You are a helpful assistant, specialized in providing single-line responses.",
    model=llm_model,
)

# 6) Run the agent and print the answer
response = Runner.run_sync(agent, "Say hello in one short sentence.")
print(response.final_output)
