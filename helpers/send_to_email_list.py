import ast
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

# Construct HTML content
# html_content = (
#     email_body.replace('\n', '<br>') +
#     '<br><br><footer>'
#     '<p>For more financial news and updates, visit '
#     '<a href="https://www.tradeklub.com">TradeKlub</a></p>'
#     '<p>Want to learn how to trade and invest? Check out our courses at '
#     '<a href="https://www.tradelikethepros.com">Trade Like The Pros</a></p>'
#     '<p>Follow us on '
#     '<a href="https://instagram.com/yourpage">Instagram</a>, '
#     '<a href="https://twitter.com/yourpage">Twitter</a>, and '
#     '<a href="https://facebook.com/yourpage">Facebook</a>.</p>'
#     '</footer>'
# )


def send_email_to_lead(email, first_name, parsed_content):
    """Send an email to a single lead."""

    parsed_content = ast.literal_eval(parsed_content)
    email_body = parsed_content.get('email_body')
    message = Mail(
        from_email='moneyclips@tradeklub.com',
        to_emails=email,
        subject=(ast.literal_eval(parsed_content)).get('subject'),
        html_content=email_body.replace('\n', '<br>') + '<br><br><footer>'
        '<p>For more financial news and updates, visit '
        '<a href="https://www.tradeklub.com">TradeKlub</a></p>'
        '<p>Want to learn how to trade and invest? Check out our courses at '
        '<a href="https://www.tradelikethepros.com">Trade Like The Pros</a></p>'
        '</footer>'
        # TODO: add a footer that suggests other articles, and redirects users to other platforms (instagram, twitter, fb, etc.)
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
