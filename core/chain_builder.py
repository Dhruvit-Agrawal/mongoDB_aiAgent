# core/chain_builder.py

import os
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI  # Correct import
from core.tool_registry import crud_tools

# Load API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)

# Load your tools
tools = crud_tools

# Create the agent
agent = create_react_agent(
    model=llm,
    tools=tools
)