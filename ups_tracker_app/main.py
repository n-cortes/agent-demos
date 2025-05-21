from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random

app = FastAPI()

class TrackingRequest(BaseModel):
    tracking_number: str

mock_db = {}

@app.post("/track")
def start_tracking(request: TrackingRequest):
    tracking_number = request.tracking_number
    mock_db[tracking_number] = {
        "carrier": "UPS",
        "status": random.choice(["In Transit", "Out for Delivery", "Delivered"]),
        "last_updated": datetime.utcnow().isoformat(),
        "estimated_delivery": (datetime.utcnow() + timedelta(days=2)).date().isoformat()
    }
    return {"message": "Tracking started"}

@app.get("/track/{tracking_number}")
def get_tracking_info(tracking_number: str):
    if tracking_number not in mock_db:
        return {"error": "Tracking number not found"}
    return mock_db[tracking_number]
