from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory statistics
stats = {
    "total_transactions": 0,
    "approvals": 0,
    "declines": 0,
    "reviews": 0,
    "frauds": 0,
    "sum_latency": 0.0
}

class Event(BaseModel):
    decision: str
    latency: float

@app.post("/event")
def ingest_event(event: Event):
    """Ingest a decision event and update metrics."""
    stats["total_transactions"] += 1
    decision = event.decision.lower()
    if decision == "approve":
        stats["approvals"] += 1
    elif decision == "decline":
        stats["declines"] += 1
    elif decision == "review":
        stats["reviews"] += 1
    else:
        stats["frauds"] += 1
    stats["sum_latency"] += event.latency
    return {"status": "event received"}

@app.get("/stats")
def get_stats():
    """Return aggregated statistics, including average latency."""
    avg_latency = 0.0
    if stats["total_transactions"] > 0:
        avg_latency = stats["sum_latency"] / stats["total_transactions"]
    return {
        "total_transactions": stats["total_transactions"],
        "approvals": stats["approvals"],
        "declines": stats["declines"],
        "reviews": stats["reviews"],
        "frauds": stats["frauds"],
        "average_latency": avg_latency
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}.py
