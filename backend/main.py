import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import openai
import json
import requests


app = FastAPI()

# CORS setup to allow requests from our Vue.js frontend
origins = [
    "http://localhost:8080",
    "http://localhost",  # Adjust this to your Vue.js app's address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/openai/")
async def generate(prompt: str = Form(...)):

    load_dotenv()

    client = openai.OpenAI(
        # This is the default and can be omitted
        api_key = os.getenv("OPENAI_API_KEY"),
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
        temperature=0.7,
        
    )
    return {"response": response.choices[0].message.content}

@app.post("/together/")
async def generate(prompt: str = Form(...)):

    load_dotenv()

    together_api_key = '8611bb406f5361dacac101d986fa079dd2be8cf51fd20b0e2203ca0f3712fc83'

    url = "https://api.together.xyz/inference"

    payload = {
        "model": "togethercomputer/llama-2-70b-chat",
        "prompt": prompt,
        "top_p": 1,
        "stop": ["F:", "Neue Frage:", "Q:", "New Question:"],
        "temperature": 0.7,
        # "max_tokens": 100,
        
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {together_api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    json_object = json.loads(response.text)
    
    return {"response": (json_object["output"]["choices"][0]["text"])}
