from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC65aee41608060b0e5c8f5289495ee5b4"
# Your Auth Token from twilio.com/console
auth_token  = "4f92468cbd41456cacebba408616f526"

def make_twilio_client():
    client = Client(account_sid, auth_token)
    return client

def send_text_message(client, request_sender_num, request_reciever_user, venmo_note, amount):
    message = client.messages.create(
        to=f"+{request_sender_num}",
        from_="+18483052722",
        body=f"A Venmo request for the amount {amount} to {request_sender_num} for {venmo_note}")
