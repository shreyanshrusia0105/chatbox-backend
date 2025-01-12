from fastapi import FastAPI, Query
import json

app = FastAPI(
    title="CDP Chatbot API",
    description="A chatbot API to answer questions about CDPs (e.g., Segment, mParticle, Zeotap).",
    version="1.0.0"
)

# Load data from cdp_data.json
with open("cdp_data.json") as f:
    cdp_data = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CDP Chatbot API"}

@app.get("/query")
def query_cdp(platform: str, query: str = Query(...)):
    platform = platform.capitalize()
    if platform in cdp_data:
        answers = cdp_data[platform]
        for key, answer in answers.items():
            if query.lower() in key:
                return {"response": answer}
        return {"response": f"No specific answer found for '{query}' in {platform}."}
    else:
        return {"response": f"Platform '{platform}' is not supported."}
