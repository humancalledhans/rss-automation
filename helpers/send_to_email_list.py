import datetime
import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from can_send_email import can_send_email
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

load_dotenv()


# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    google_creds_str = os.getenv("GOOGLE_CREDS")

    if google_creds_str:
        google_creds = json.loads(google_creds_str)
        cred = credentials.Certificate(google_creds)
        firebase_admin.initialize_app(cred)

db = firestore.client()  # Firestore client outside initialization block


def send_email_to_lead(email, first_name, parsed_content):
    """Send an email to a single lead."""
    message = Mail(
        from_email='moneyclips@tradeklub.com',
        to_emails=email,
        subject=parsed_content.get('subject'),
        html_content=parsed_content.get('email_body').replace('\n', '<br>')
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent to {email}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email to {email}: {str(e)}")


def send_to_email_list(parsed_content):
    """Read leads from Firestore and send emails with individual email limits."""

    EMAIL_INTERVAL_MINUTES = 30

    # Retrieve all leads from Firestore
    leads_ref = db.collection('leads')
    leads = leads_ref.stream()

    for lead in leads:
        lead_data = lead.to_dict()
        email = lead_data.get('email')
        first_name = lead_data.get('first_name')
        user_id = lead.id  # Use the document ID as the unique user ID

        if email:
            # Check the last sent time for this user
            user_email_limit_doc = db.collection(
                'email_limits').document(user_id)
            doc = user_email_limit_doc.get()
            now = datetime.datetime.now()

            if doc.exists:
                data = doc.to_dict()
                last_sent_time_str = data.get('last_sent_time')
                last_sent_time = datetime.datetime.fromisoformat(
                    last_sent_time_str) if last_sent_time_str else None

                # Check if 30 minutes have passed since the last email
                if last_sent_time:
                    time_difference = (
                        now - last_sent_time).total_seconds() / 60
                    if time_difference < EMAIL_INTERVAL_MINUTES:
                        print(f"Skipping {email}: Last email sent {time_difference:.2f} minutes ago. "
                              f"Wait another {EMAIL_INTERVAL_MINUTES - time_difference:.2f} minutes.")
                        continue

            # Send the email
            print(f"Sending email to: {email}")
            send_email_to_lead(email, first_name, parsed_content)

            # Update Firestore with the new last sent time
            user_email_limit_doc.set({
                'last_sent_time': now.isoformat()
            }, merge=True)

        else:
            print(f"Skipping lead with no email: {lead_data}")
