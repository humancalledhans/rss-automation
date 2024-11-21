
from helpers.can_send_email import can_send_email


def send_to_email_list(email_limit_doc, parsed_content, url):
    """Send the parsed content and article URL to the email list."""
    if not can_send_email(email_limit_doc):
        print("Daily email limit reached. Email not sent.")
        return

    # Example email content
    email_content = f"{parsed_content}\n\nRead more: {url}"
    # Implement your email sending logic here
    print("Sending email:", email_content)
