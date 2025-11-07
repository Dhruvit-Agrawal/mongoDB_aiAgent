from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from agent.agent_logic_two import run_agent

app = FastAPI(
    title="MongoDB LLM Agent API",
    description="An API that lets you interact with MongoDB using natural language queries.",
    version="1.0"
)

class QueryRequest(BaseModel):
    query: str

def safe_serialize_agent_response(result):
    """Turn agent result into something JSON-friendly."""
    # Try to handle dict, string, or agent messages.
    if isinstance(result, dict):
        return result
    elif hasattr(result, 'dict'):
        return result.dict()
    else:
        return str(result)

@app.post("/query")
async def handle_query(request: QueryRequest):
    try:
        print(f"request:{request}")
        print(f"query: {request.query}")
        # Use threadpool for sync agent call to avoid blocking event loop.
        #result = await run_in_threadpool(run_agent, request.query)
        query=request.query
        result = run_agent(query)
        return {"status": "success", "response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})

@app.get("/")
async def root():
    return {"message": "MongoDB AI Agent API is running 🚀"}
