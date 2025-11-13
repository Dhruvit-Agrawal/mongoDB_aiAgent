# core/chain_builder.py

import os
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from core.tool_registry import crud_tools
from agent.prompt_templates import SYSTEM_PROMPT
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder("messages"),
    ]
)


# Create the agent
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt= prompt
)