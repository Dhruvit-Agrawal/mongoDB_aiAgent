import os
from langchain.chat_models import ChatGoogleGemini

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGemini(
    model="gemini-2.5-pro",
    temperature=0,
    api_key=GOOGLE_API_KEY
)
