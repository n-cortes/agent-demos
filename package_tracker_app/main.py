from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random

app = FastAPI()

fake_db = {}

class TrackRequest(BaseModel):
    tracking_number: str
    carrier: str

@app.post("/track")
def track_package(data: TrackRequest):
    fake_db[data.tracking_number] = {
        "carrier": data.carrier,
        "status": random.choice(["In Transit", "Out for Delivery", "Delivered"]),
        "last_updated": datetime.utcnow().isoformat(),
        "estimated_delivery": (datetime.utcnow() + timedelta(days=2)).date().isoformat()
    }
    return {"message": "Tracking started"}

@app.get("/track/{tracking_number}")
def get_status(tracking_number: str):
    return fake_db.get(tracking_number, {"error": "Not found"})