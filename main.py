from fastapi.middleware.cors import CORSMiddleware
import os
import json
import openai
import requests
import datetime
import firebase_admin
from firebase_admin import credentials, firestore, messaging
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from router import kajabi
from get_prompt import get_email_remix_system_prompt
from helpers.parse_with_gpt import parse_with_chatgpt
from helpers.send_to_email_list import send_to_email_list

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()
app.include_router(kajabi.router)

app.add_middleware(
    CORSMiddleware,
    # Replace "*" with specific origins in production, e.g., ["http://localhost:8080"]
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Firebase setup
# cred = credentials.Certificate("/path/to/your/firebase-credentials.json")
# if not firebase_admin._apps:
#     firebase_admin.initialize_app(cred)
# db = firestore.client()
# email_limit_doc = db.collection('settings').document('email_limits')

firebase_creds = {
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    # Ensure newlines are preserved
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token",
}

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_creds)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


@app.post("/kajabi")
async def kajabi():
    pass

subscriptions = []


# Define a Pydantic model for the request body
class Subscription(BaseModel):
    token: str


@app.post("/subscribe")
async def subscribe(subscription: Subscription):
    """
    Store or update the FCM token in Firestore.
    """
    try:
        # Extract the token from the request body
        token = subscription.token

        # Check if the token already exists in Firestore
        users_ref = db.collection("users")
        query = users_ref.where("fcm_token", "==", token).stream()

        if any(query):  # Token is already stored
            return {"message": "Already subscribed"}

        # Add new token to Firestore
        user_ref = db.collection("users").document()
        user_ref.set({"fcm_token": token})
        return {"message": "Subscription successful"}
    except Exception as e:
        return {"error": f"Failed to subscribe user: {str(e)}"}


class NotificationPayload(BaseModel):
    title: str
    body: str


@app.post("/sendNotification")
async def send_notification(payload: NotificationPayload):
    """
    Send push notifications to all users stored in Firestore.
    """
    try:
        # Extract title and body from the request payload
        title = payload.title
        body = payload.body

        # Fetch all FCM tokens from Firestore
        users_ref = db.collection("users")
        users = users_ref.stream()

        tokens = [user.to_dict().get("fcm_token")
                  for user in users if user.to_dict().get("fcm_token")]

        if not tokens:
            raise HTTPException(status_code=400, detail="No subscribed users")

        print("check out tokens obtained", tokens)

        # Send notifications via Firebase Admin SDK
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            tokens=tokens,
        )

        print("multi cast message being sent", message)
        response = messaging.send_multicast(message)

        return {"message": f"Notifications sent to {response.success_count} users"}
    except Exception as e:
        return {"error": f"Failed to send notification: {str(e)}"}


# OpenAI API setup
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


@app.post("/webhook")
async def webhook(request: Request):
    """Handle incoming webhook from RSS.app."""
    data = await request.json()
    if not data:
        return {"error": "No data received"}

    print("Data received:", data)

    # Extract the list of new items
    items_new = data.get('data', {}).get('items_new', [])

    # Create a list of dictionaries for each article
    news_content_list = [{'title': item['title'],
                          'description': item['description_text']} for item in items_new]

    # Parse the news content with ChatGPT
    parsed_content = await parse_with_chatgpt(news_content_list)

    print("parsed content check it out", parsed_content)

    # Send the parsed content to the email list
    send_to_email_list(parsed_content)

    return {"message": "Webhook received and processed successfully"}

# To run the app, use: uvicorn your_script_name:app --reload
