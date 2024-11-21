import datetime
import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

# Daily email limit
DAILY_EMAIL_LIMIT = 100
EMAIL_INTERVAL_MINUTES = 30  # Interval in minutes between emails

load_dotenv()

google_creds_str = os.getenv("GOOGLE_CREDS")

# Parse the JSON string into a Python dictionary
if google_creds_str:
    google_creds = json.loads(google_creds_str)

    # Use the credentials for Firebase or Google Cloud
    cred = credentials.Certificate(google_creds)
    initialize_app(cred)
    db = firestore.client()


def can_send_email():
    """Check if the daily email limit has been reached and enforce a 30-minute interval."""
    now = datetime.datetime.now()
    today = now.date().isoformat()

    # Reference to the Firestore document
    email_limit_doc = db.collection('email_limits').document('daily_limits')

    # Retrieve the document
    doc = email_limit_doc.get()

    if doc.exists:
        data = doc.to_dict()
        emails_sent = data.get('emails_sent', 0)
        last_sent_time_str = data.get('last_sent_time')
        last_sent_time = datetime.datetime.fromisoformat(
            last_sent_time_str) if last_sent_time_str else None

        # Check if the daily limit is reached
        if data.get('date') == today and emails_sent >= DAILY_EMAIL_LIMIT:
            print(f"No! Daily limit of {DAILY_EMAIL_LIMIT} emails reached.")
            return False  # Daily limit reached

        # Check if 30 minutes have passed since the last email was sent
        if last_sent_time:
            time_difference = (now - last_sent_time).total_seconds() / 60
            if time_difference < EMAIL_INTERVAL_MINUTES:
                print(f"No! Last email was sent {time_difference:.2f} minutes ago. "
                      f"Wait another {EMAIL_INTERVAL_MINUTES - time_difference:.2f} minutes.")
                return False  # 30-minute interval not reached yet

        # Update the counter and last sent time
        email_limit_doc.update({
            'emails_sent': emails_sent + 1,
            'last_sent_time': now.isoformat(),
            'date': today
        })

        print(f"""Yes! Last email was sent {
              time_difference:.2f} minutes ago. Sending another email now.""")
        return True
    else:
        # First time setting up the counter and last sent time
        email_limit_doc.set({
            'emails_sent': 1,
            'last_sent_time': now.isoformat(),
            'date': today
        })
        print("Yes! First email being sent now.")
        return True
