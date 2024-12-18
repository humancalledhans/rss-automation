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

from firebase_fcm import send_multicast_message
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

if os.getenv("ENV") == "production":
    # Initialize Firebase only if not already initialized
    if not firebase_admin._apps:
        google_creds_str = os.getenv("GOOGLE_CREDS")

        if google_creds_str:
            google_creds = json.loads(google_creds_str)
            cred = credentials.Certificate(google_creds)
            firebase_admin.initialize_app(cred)

    db = firestore.client()  # Firestore client outside initialization block


else:
    if not firebase_admin._apps:
        type_value = os.getenv("GOOGLE_TYPE")
        project_id = os.getenv("GOOGLE_PROJECT_ID")
        private_key_id = os.getenv("GOOGLE_PRIVATE_KEY_ID")
        private_key = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")
        client_email = os.getenv("GOOGLE_CLIENT_EMAIL")
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        auth_uri = os.getenv("GOOGLE_AUTH_URI")
        token_uri = os.getenv("GOOGLE_TOKEN_URI")
        auth_provider_x509_cert_url = os.getenv(
            "GOOGLE_AUTH_PROVIDER_X509_CERT_URL")
        client_x509_cert_url = os.getenv("GOOGLE_AUTH_CLIENT_X509_CERT_URL")
        universe_domain = os.getenv("GOOGLE_AUTH_UNIVERSE_DOMAIN")

        google_creds = {
            "type": type_value,
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
            "universe_domain": universe_domain
        }

        if google_creds:
            # Pass the credentials dictionary directly without JSON serialization
            cred = credentials.Certificate(google_creds)
            firebase_admin.initialize_app(cred)

    db = firestore.client()  # Firestore client outside initialization block


@app.post("/kajabi")
async def kajabi():
    pass

subscriptions = []


# Define a Pydantic model for the request body
class Subscription(BaseModel):
    token: str


@app.post("/updateToken")
async def update_token(subscription: Subscription):
    """
    Update the FCM token in Firestore.
    """
    try:
        token = subscription.token

        # Here you would check if the token already exists, update or insert accordingly
        users_ref = db.collection("users")
        query = users_ref.where("fcm_token", "==", token).stream()

        if any(query):  # Token is already stored, update if needed
            # Update logic here, e.g., update timestamp or other user data
            return {"message": "Token already exists, updated if necessary"}
        else:
            # If not found, add the new token
            user_ref = db.collection("users").document()
            user_ref.set({"fcm_token": token})
            return {"message": "Token updated"}
    except Exception as e:
        return {"error": f"Failed to update token: {str(e)}"}


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

        response = send_multicast_message(message)

        return {"message": f"Notifications sent to {response.get('success_count')} users"}
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
