import os
import openai
import requests
import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, Request
from dotenv import load_dotenv

from get_prompt import get_email_remix_system_prompt
from helpers.parse_with_gpt import parse_with_chatgpt
from helpers.send_to_email_list import send_to_email_list

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Firebase setup
cred = credentials.Certificate("/path/to/your/firebase-credentials.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()
email_limit_doc = db.collection('settings').document('email_limits')

# OpenAI API setup
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


@app.post("/webhook")
async def webhook(request: Request):
    """Handle incoming webhook from RSS.app."""
    data = await request.json()
    if not data:
        return {"error": "No data received"}

    # Extract article details
    title = data.get("title", "No Title")
    description = data.get("description", "No Description")
    url = data.get("url", "No URL")
    news_content = f"Title: {title}\n\nDescription: {description}"

    # Parse the news content with ChatGPT
    parsed_content = parse_with_chatgpt(news_content)

    print("parsed content check it out", parsed_content)

    # Send the parsed content to the email list
    # send_to_email_list(email_limit_doc, parsed_content, url)

    return {"message": "Webhook received and processed successfully"}

# To run the app, use: uvicorn your_script_name:app --reload
