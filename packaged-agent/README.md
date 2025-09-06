# Packaged Agent

A packaged Python app using the OpenAI Agents SDK and uv. This agent exposes a CLI entry point and prints a model-generated greeting.

## Features
- Loads API key from `.env` (never hardcoded)
- Uses `python-dotenv` for environment variables
- Packaged structure with `src/` and script entry in `pyproject.toml`
- Output screenshot included below

## Usage
1. Copy `.env.example` to `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
2. Install dependencies:
   ```sh
   uv sync
   ```
3. Run the agent via script entry:
   ```sh
   uv run hello-agent
   ```
   Or directly:
   ```sh
   uv run -m hello_agent.main
   ```

## Output

![Agent Output](output.PNG)

## Security
- `.env` is ignored by `.gitignore` and never committed
- Only `.env.example` is tracked

## References
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [uv Docs](https://docs.astral.sh/uv/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
