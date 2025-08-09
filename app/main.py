from fastapi import FastAPI
from pydantic import BaseModel
from app.model import SentimentModel

app = FastAPI()
model = SentimentModel()

class TextIn(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(input: TextIn):
    prediction = model.predict(input.text)
    return prediction
