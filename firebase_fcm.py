from firebase_admin import messaging, firestore


def send_multicast_message(message):
    try:
        print("Multicast message being sent", message)
        response = messaging.send_each_for_multicast(message)

        # Extract the relevant information from the BatchResponse object
        response_data = {
            "success_count": response.success_count,
            "failure_count": response.failure_count,
            "responses": []
        }

        failed_tokens = []  # Collect failed tokens for document deletion

        for idx, resp in enumerate(response.responses):
            token = message.tokens[idx]
            response_info = {
                "success": resp.success,
                "error": str(resp.exception) if resp.exception else None,
                "message_id": resp.message_id
            }

            # If the response failed, add token to the failed_tokens list
            if not resp.success:
                print(f"Failed token detected: {token}")
                failed_tokens.append(token)

            response_data["responses"].append(response_info)

        # Delete entire documents of users with failed tokens from the 'users' collection
        if failed_tokens:
            delete_documents_with_invalid_tokens(failed_tokens)

        return response_data

    except Exception as e:
        print(f"Error while sending multicast message: {str(e)}")
        return None


def delete_documents_with_invalid_tokens(tokens):
    db = firestore.client()
    for token in tokens:
        # Query Firestore for the document with the failed token
        query = db.collection('users').where('fcm_token', '==', token)
        docs = query.get()

        for doc in docs:
            # Delete the entire document
            doc.reference.delete()
            print(f"Deleted document with token: {token}")
