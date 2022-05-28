# from venmo_api import Client
from venmo_api_overrides import HTTPClient

print("User id: ")
userid = input()
print("Pass: ")
password = input()
# access_token = HTTPClient.get_access_token(username=userid,
#                                         password=password)

auth_api = HTTPClient.get_auth_api()
access_token = auth_api.login_with_credentials_cli(username=userid, password=password)
if not access_token:
    # ask for OTP
    access_token = auth_api.two_factor_login()

print("My token:", access_token)

# ML_ACCESS_TOKEN = '243697ea70e559b2fa5c376255af72dd941277102d988cab3a4605787eb9bfa6'
# IN_ACCESS_TOKEN = 'b2b034a9c46ad9e5bffbaefe4102439dfc871213e8fd72373f87c9ae398c391f'
# IN_DEV_ID = '15792840-64E5-8F71-30N3-5BL08G922RH5'
# DEVICE_ID = '81807627-18U3-2S70-25K9-7IO59Q989JQ2'

# # Initialize api client using an access-token
# client = HTTPClient(access_token=ACCESS_TOKEN)

# amnt = int(input("Enter amount: "))
# request_id = input("Enter requestee id: ")
# client.payment.request_money(amount=amnt, note="yo", target_user_id=request_id)

# HTTPClient.log_out(ML_ACCESS_TOKEN)
# HTTPClient.log_out(IN_ACCESS_TOKEN)

