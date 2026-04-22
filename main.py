from fastapi import FastAPI
from auth import router as auth_router
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
#from agent import process_message
from db import collection

app = FastAPI()
app.include_router(auth_router)

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

# ✅ Chat API
@app.post("/chat")
def chat(data: Message):
    message = data.message

    result = {"message": message}

    # ✅ Ensure dictionary
    if not isinstance(result, dict):
        result = {"raw": str(result)}

    # ✅ Save to MongoDB
    collection.insert_one({
        "input": message,
        "output": result
    })

    return {"reply": result}

# ✅ Dashboard API
@app.get("/interactions")
def get_interactions():
    data = list(collection.find({}, {"_id": 0}))
    return data

@app.post("/add-interaction")
def add_interaction(data: dict):
    collection.insert_one({
        "doctor": data.get("doctor"),
        "hospital": data.get("hospital"),
        "notes": data.get("notes"),
        "follow_up": data.get("follow_up")
    })
    return {"message": "Saved successfully"}
