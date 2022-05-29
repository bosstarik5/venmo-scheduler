from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC65aee41608060b0e5c8f5289495ee5b4"
# Your Auth Token from twilio.com/console
auth_token  = "dfa268b9d423e60b994641f617c542a5"

def make_twilio_client():
    client = Client(account_sid, auth_token)
    return client

def send_success_message(client, request_sender_num, request_reciever_user, venmo_note, amount):
    if len(request_sender_num) == 10:
        request_sender_num = '1' + request_sender_num

    message = client.messages.create(
        to=f"+{request_sender_num}",
        from_="+18483052722",
        body=f"A Venmo request for the amount {amount} to {req} for {venmo_note} has been sent!")


def send_failure_message(client, request_sender_num, request_reciever_user, venmo_note, amount):
    if len(request_sender_num) == 10:
        request_sender_num = '1' + request_sender_num

    message = client.messages.create(
        to=f"+{request_sender_num}",
        from_="+18483052722",
        body=f"Your Venmo request for the amount {amount} to {request_sender_num} for {venmo_note} failed to be sent")

