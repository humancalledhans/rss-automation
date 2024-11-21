import datetime

# Daily email limit
DAILY_EMAIL_LIMIT = 100
EMAIL_INTERVAL_MINUTES = 30  # Interval in minutes between emails


def can_send_email(email_limit_doc):
    """Check if the daily email limit has been reached and enforce a 30-minute interval."""
    now = datetime.datetime.now()
    today = now.date().isoformat()
    doc = email_limit_doc.get()

    if doc.exists:
        data = doc.to_dict()
        emails_sent = data.get('emails_sent', 0)
        last_sent_time_str = data.get('last_sent_time')
        last_sent_time = datetime.datetime.fromisoformat(
            last_sent_time_str) if last_sent_time_str else None

        # Check if the daily limit is reached
        if data.get('date') == today and emails_sent >= DAILY_EMAIL_LIMIT:
            return False  # Daily limit reached

        # Check if 30 minutes have passed since the last email was sent
        if last_sent_time:
            time_difference = (now - last_sent_time).total_seconds() / 60
            if time_difference < EMAIL_INTERVAL_MINUTES:
                return False  # 30-minute interval not reached yet

        # Update the counter and last sent time
        email_limit_doc.update({
            'emails_sent': emails_sent + 1,
            'last_sent_time': now.isoformat(),
            'date': today
        })
        return True
    else:
        # First time setting up the counter and last sent time
        email_limit_doc.set({
            'emails_sent': 1,
            'last_sent_time': now.isoformat(),
            'date': today
        })
        return True
