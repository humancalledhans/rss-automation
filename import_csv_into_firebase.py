import re
import json
import os
import csv
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


def format_phone_number(number):
    # Remove '='
    cleaned_number = number.replace('=', '').strip()

    # Extract digits
    digits = re.sub(r'[^0-9]', '', cleaned_number)

    # Check the length of the cleaned digits
    if len(digits) <= 1:
        return ''

    # If there's a '+' sign in the cleaned_number, keep it
    if '+' in cleaned_number:
        formatted_number = '+' + digits
    # If there's a '(' or ')' and no '+1', prepend with '+1'
    elif '(' in cleaned_number or ')' in cleaned_number and not cleaned_number.startswith('+1'):
        formatted_number = '+1' + digits
    else:
        formatted_number = digits

    return formatted_number


load_dotenv()

google_creds_str = os.getenv("GOOGLE_CREDS")

# Parse the JSON string into a Python dictionary
if not firebase_admin._apps:
    google_creds_str = os.getenv("GOOGLE_CREDS")

    if google_creds_str:
        google_creds = json.loads(google_creds_str)
        cred = credentials.Certificate(google_creds)
        firebase_admin.initialize_app(cred)

db = firestore.client()  # Firestore client outside initialization block


# Define the CSV file path
# Update this path
# csv_file_path = '(NEW) Trade Like The Pros Program - Subscriptions Master Tracker - TradeKlub'
csv_file_path = 'testing.csv'

# Function to add data to Firestore


def add_to_firestore(data):
    db.collection('leads').add(data)


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
        print(f"Added lead: {lead_data['first_name']}")

print("Data transfer complete!")
