import re
import json
import random
import string
import os
import csv
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, auth, initialize_app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

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


def send_email(to_email, subject, body):
    # Get email credentials from environment variables
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))

    if not all([sender_email, sender_password]):
        raise ValueError(
            "Email credentials are missing from environment variables.")

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)


def generate_temporary_password(user_name, user_email):
    name_part = ''.join(
        char for char in user_name if char.isalnum()).lower()[:3]
    email_part = ''.join(char for char in user_email.split(
        '@')[0] if char.isalnum()).lower()[:3]

    random_string = ''.join(random.choices(
        string.ascii_letters + string.digits, k=4))
    password = f"{name_part}{email_part}{random_string}!@#"

    return password[:12]


def send_email(to_email, subject, body):
    message = Mail(
        from_email=os.getenv('SENDGRID_SENDER_EMAIL',
                             'moneyclips@tradeklub.com'),
        to_emails=to_email,
        subject=subject,
        html_content=body  # Note: SendGrid uses HTML, so we keep it as HTML here
    )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent to {to_email}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")


def create_users_from_leads():
    db = firestore.client()
    leads_ref = db.collection('leads')

    print("CRFL 1")

    # Query all leads
    leads = leads_ref.stream()

    for lead in leads:
        lead_data = lead.to_dict()
        print("lead data", lead_data)
        if 'email' in lead_data and 'first_name' in lead_data:
            email = lead_data['email']
            name = lead_data['first_name']

            # Check if the user already exists
            try:
                user = auth.get_user_by_email(email)
                print(f"""User with email {
                      email} already exists. Skipping creation.""")
                lead.reference.update({'userId': user.uid})
            except auth.UserNotFoundError:
                # if email == "workhansyap@gmail.com":
                temp_password = generate_temporary_password(name, email)

                try:
                    user = auth.create_user(
                        email=email,
                        password=temp_password,
                        display_name=name
                    )
                    print(f"""Successfully created new user: {
                        user.uid} for {email}""")
                    lead.reference.update({'userId': user.uid})

                    # Send email notification
                    email_subject = "Your Temporary Password for Access"
                    email_body = f"""
                    <p>Hello {name},</p>
                    <p>Your temporary password for your account is: <strong>{temp_password}</strong></p>
                    <p>Please log in using this password and change it immediately for security reasons.</p>
                    <p>Best regards,<br>Tradeklub.com</p>
                    """
                    send_email(email, email_subject,
                               email_body.replace("\n", "<br>"))
                    print(f"Email sent to {email} with temporary password.")

                except auth.EmailAlreadyExistsError:
                    print(f"User with email {email} already exists.")
                except Exception as e:
                    print(f"""An error occurred while creating user for {
                        email}: {e}""")
                # else:
                #     print(f"""Skipping user creation for {
                #           email} since it's not the test email.""")


if __name__ == "__main__":
    create_users_from_leads()
