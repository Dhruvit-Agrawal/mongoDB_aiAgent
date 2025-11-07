from core.chain_builder import agent

from langchain_core.output_parsers import SimpleJsonOutputParser

output_parser = SimpleJsonOutputParser()

def run_agent(query):
    print("🤖 Mongo LLM Agent is ready! Type 'exit' to quit.")
    print(query)
    try:
        response = agent.invoke({"messages": [{"role": "user", "content": query}]})


        parsed = None
        try:
            parsed = output_parser.invoke(response)
        except Exception:
            parsed = response # fallback if parsing fails
        print("Agent >", parsed)
        return parsed
    except Exception as e:
        print(f"error: {e}")
        return str(e)