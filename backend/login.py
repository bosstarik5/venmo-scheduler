from venmo_api import Client

print("User id: ")
userid = input()
print("Pass: ")
password = input()
access_token = Client.get_access_token(username=userid,
                                        password=password)
print("My token:", access_token)

ACCESS_TOKEN = 'd6b9f1c2621c5d8b6d59da60e28a8e0c05913ec84be5a75f11b8da76847cd3f2'
DEVICE_ID = '57584824-38A6-6A74-44H4-4QJ95A225UJ2'

# Initialize api client using an access-token
client = Client(access_token=ACCESS_TOKEN)

amnt = int(input("Enter amount: "))
request_id = input("Enter requestee id: ")
client.payment.request_money(amount=amnt, note="yo", target_user_id=request_id)