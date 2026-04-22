from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

# Dummy ML model logic
def predict(text):
    return {"prediction": f"Processed: {text}"}

@app.post("/predict/")
def get_prediction(data: InputData):
    return predict(data.text)