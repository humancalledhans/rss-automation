import re
import json
import os
import csv
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


load_dotenv()

# google_creds_str = os.getenv("GOOGLE_CREDS")

# # Parse the JSON string into a Python dictionary
# if not firebase_admin._apps:
#     google_creds_str = os.getenv("GOOGLE_CREDS")

#     if google_creds_str:
#         google_creds = json.loads(google_creds_str)
#         cred = credentials.Certificate(google_creds)
#         firebase_admin.initialize_app(cred)

# db = firestore.client()  # Firestore client outside initialization block

# Load credentials from google_creds.json
google_creds_file = "google_creds.json"

if not firebase_admin._apps:
    if os.path.exists(google_creds_file):
        # Load the credentials JSON file
        with open(google_creds_file, "r") as f:
            google_creds = json.load(f)

        # Use the credentials to initialize Firebase
        cred = credentials.Certificate(google_creds)
        firebase_admin.initialize_app(cred)
    else:
        raise FileNotFoundError(f"""Credentials file '{
                                google_creds_file}' not found.""")

# Firestore client outside initialization block
db = firestore.client()


# Define the CSV file path
# Update this path
csv_file_path = '(NEW) Trade Like The Pros Program - Subscriptions Master Tracker - TradeKlub.csv'
# csv_file_path = 'testing.csv'

# Function to add data to Firestore


def add_to_firestore(data):
    """Add a new lead to the Firestore 'leads' collection if the email doesn't already exist."""
    # Check if the email already exists in the 'leads' collection
    existing_lead = db.collection('leads').where(
        'email', '==', data['email']).get()

    if existing_lead:
        print(f"Email {data['email']} already exists. Skipping...")
        return  # Skip adding this lead if the email already exists

    # Add lead data to Firestore
    lead_ref = db.collection('leads').add(data)

    # Use the generated document ID to track email limits for this lead
    lead_id = lead_ref[1].id

    # Initialize 'last_sent_time' in the 'email_limits' collection
    db.collection('email_limits').document(lead_id).set({
        'last_sent_time': None  # No email sent yet
    })

    print(f"Added lead: {data['first_name']} with ID {lead_id}")


# Read the CSV file and transfer data to Firestore
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        lead_data = {
            "email": row["Email Address"],
            "first_name": row["First Name"],
            "last_name": row["Last Name"],
            "date_added": firestore.SERVER_TIMESTAMP
        }

        add_to_firestore(lead_data)

print("Data transfer complete!")
