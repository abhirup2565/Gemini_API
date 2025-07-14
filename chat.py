import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"),)
chat = client.chats.create(model="gemini-2.5-flash")

while True:
    message=input()
    if message=="exit":
        break
    response = chat.send_message(message)
    print(response.text)

