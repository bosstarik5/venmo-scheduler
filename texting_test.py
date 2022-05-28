from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC65aee41608060b0e5c8f5289495ee5b4"
# Your Auth Token from twilio.com/console
auth_token  = "4f92468cbd41456cacebba408616f526"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18479621760",
    from_="+18483052722",
    body="TEXT FOR STUFF GOES HERE")

print(message.sid)