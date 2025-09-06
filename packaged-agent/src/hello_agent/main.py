# packaged-agent/src/packaged_agent/main.py
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

def run():
    # 1) Load API key
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    # 2) Gemini model
    model = "gemini-2.5-flash-lite"

    # 3) OpenAI-compatible Gemini client
    external_client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=api_key,
    )
    set_default_openai_client(external_client)

    # 4) Register Chat Completions model
    llm_model = OpenAIChatCompletionsModel(
        model=model,
        openai_client=external_client,
    )

    set_tracing_disabled(True)

    # 5) Agent
    agent = Agent(
        name="packaged_agent",
        instructions="You are a concise assistant. Reply in one short sentence.",
        model=llm_model,
    )

    # 6) Run and print result
    response = Runner.run_sync(agent, "Say hello in one short sentence.")
    print(response.final_output)
