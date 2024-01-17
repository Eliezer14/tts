from fastapi import FastAPI
import torch
from IPython.display import Audio, display

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/tts")
async def tts():
    return {"message": "Hello World"}