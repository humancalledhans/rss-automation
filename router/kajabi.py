from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Dict, Any
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json


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


router = APIRouter()


class KajabiPayload(BaseModel):
    id: str
    event: str
    payload: dict


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


@router.post('/kajabi')
async def create_custom_campaign(
    # req_body: dict = Body(...),
    req_body: KajabiPayload
    # files: Optional[List[UploadFile]] = File([])
):

    print("req bdoy 3920993", req_body)

    """
    example data:

    {
    'id': 'f0c62864-b5e2-11ef-9d81-2d9395bb1f70', 
    'event': 'purchase.created', 
    'payload': {
        'affiliate_conversion_id': 0, 
        'affiliate_user_id': 0, 
        'affiliate_user_name': 'Kajabi Test Affiliate', 
        'affiliate_user_email': 'nobody.affiliate@kajabi.com', 
        'contact_address_line_1': '100 Example Drive', 
        'contact_address_line_2': 'Suite 200G', 
        'contact_address_city': 'Irvine', 
        'contact_address_country': 'US', 
        'contact_address_country_name': 'United States of America', 
        'contact_address_state': 'CA', 
        'contact_address_zip': '92620', 
        'contact_phone_number': '949-555-1212', 
        'offer_id': 0, 'offer_title': 'Kajabi Test Offer', 
        'offer_reference': 'kajabi_offer_0', 
        'opt_in': False, 'trial': False, 
        'member_id': 0, 'member_email': 'nobody@kajabi.com', 
        'member_name': 'Kajabi Test', 'member_first_name': 'Kajabi', 
        'member_last_name': 'Test', 'transaction_id': 1234567890, 
        'transaction_created_at': '2024-12-09T04:06:17.847+00:00', 
        'offer_type': 'subscription', 
        'subtotal': 1250, 'subtotal_decimal': 12.5, 
        'discount_amount': 0, 'discount_amount_decimal': 0.0, 
        'amount_paid': 1250, 'amount_paid_decimal': 12.5, 'currency': 'USD', 
        'payment_method': 'visa', 'payment_processor': 'Kajabi Payments', 
        'coupon_code': '10OFF', 'subscription_id': 1234567890, 
        'subscription_created_at': '2024-12-09T04:06:17.847+00:00', 'interval_payment_amount': 1250, 
        'interval_payment_amount_decimal': 12.5, 'interval_count': 1, 'interval': 'month', 
        'trial_period_days': None, 'setup_fee': 0, 
        'setup_fee_decimal': 0.0, 'quantity': 1}}
    """

    event = req_body.payload.event
    user_email = req_body.payload.member_email
    user_first_name = req_body.payload.member_first_name
    user_last_name = req_body.payload.member_last_name

    if event == 'purchase.created':
        lead_data = {
            "email": user_email,
            "first_name": user_first_name,
            "last_name": user_last_name,
            "date_added": firestore.SERVER_TIMESTAMP
        }
        add_to_firestore(lead_data)

    print(f"""new subscriber created {user_email} at {
          firestore.SERVER_TIMESTAMP}!!""")

    return {"status": "success", "data": f"new subscriber created {user_email}"}
