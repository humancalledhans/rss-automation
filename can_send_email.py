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

        # # Check if the daily limit is reached
        # if data.get('date') == today and emails_sent >= DAILY_EMAIL_LIMIT:
        #     print(f"No! Daily limit of {DAILY_EMAIL_LIMIT} emails reached.")
        #     return False  # Daily limit reached

        # Check if 30 minutes have passed since the last email was sent
        if last_sent_time:
            time_difference = (now - last_sent_time).total_seconds() / 60
        #     if time_difference < EMAIL_INTERVAL_MINUTES:
        #         print(f"No! Last email was sent {time_difference:.2f} minutes ago. "
        #               f"Wait another {EMAIL_INTERVAL_MINUTES - time_difference:.2f} minutes.")
        #         return False  # 30-minute interval not reached yet

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
