import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from can_send_email import can_send_email
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

load_dotenv()


# Initialize Firebase
google_creds_str = os.getenv("GOOGLE_CREDS")

if google_creds_str:
    google_creds = json.loads(google_creds_str)
    cred = credentials.Certificate(google_creds)
    initialize_app(cred)
    db = firestore.client()


def send_email_to_lead(email, parsed_content):
    """Send an email to a single lead."""
    message = Mail(
        from_email='moneyclips@tradeklub.com',
        to_emails=email,
        subject='Your Latest Money Clips Update',
        html_content=parsed_content
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent to {email}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email to {email}: {str(e)}")


def send_to_email_list(parsed_content):
    """Read leads from Firestore and send emails."""
    if not can_send_email():
        print("Daily email limit reached. Emails not sent.")
        return

    # Retrieve all leads from Firestore
    leads_ref = db.collection('leads')
    leads = leads_ref.stream()

    for lead in leads:
        lead_data = lead.to_dict()
        email = lead_data.get('email')

        if email:
            print(f"Sending email to: {email}")
            send_email_to_lead(email, parsed_content)
        else:
            print(f"Skipping lead with no email: {lead_data}")
