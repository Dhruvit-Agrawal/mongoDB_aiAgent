from core.chain_builder import agent

def run_agent():
    print("Mongo LLM Agent is ready! Type 'exit' to quit.")
    while True:
        query = input("\nYou > ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = agent.invoke({"messages": [("user", query)]})
            print("Agent >", response)
        except Exception as e:
            print(f"Error: {e}")
