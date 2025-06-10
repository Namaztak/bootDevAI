import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
input = sys.argv
messages = [
    types.Content(role="user", parts=[types.Part(text=input[1])]),
]

if len(input) < 2:
    print("Usage: python main.py <input>")
    os._exit(1)

res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

print(res.text)
if input[2] == "--verbose":
    print(f"User prompt: {input[1]}")
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")