from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # أضف هذا السطر
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

votes = {"Python": 0, "JavaScript": 0}

# This function will serve your HTML file
@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.get("/stats")
def get_stats():
    return {
        "container_id": os.getenv("HOSTNAME", "Cloud-Node"),
        "votes": votes
    }

@app.post("/vote/{language}")
def process_vote(language: str):
    if language in votes:
        votes[language] += 1
        return {"status": "Success"}
    return {"status": "Error"}