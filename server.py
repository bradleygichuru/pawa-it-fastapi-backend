import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import FastAPI, Form
from google import genai
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/ask")
async def ask(query: Annotated[str, Form()]):
    response = client.models.generate_content(model="gemini-2.0-flash", contents=query)
    print(response)
    print(response.text)
    return response.text
