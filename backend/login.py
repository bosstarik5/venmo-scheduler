# from venmo_api import Client
from venmo_api_overrides import HTTPClient
from venmo_api.models.exception import HttpCodeError


def login(user, passw):

    auth_api = HTTPClient.get_auth_api()
    try:
        access_token = auth_api.login_with_credentials_cli(username=user, password=passw)
        if not access_token:
            # ask for OTP
            access_token = auth_api.two_factor_login()

        client = HTTPClient(access_token)
        phone = client.user.get_my_profile().phone
        venmo_id = client.user.get_my_profile().id

        HTTPClient.log_out(access_token)
        return access_token, venmo_id, phone
    except HttpCodeError:
        return None, None, None


"""
print("User id: ")
userid = input()
print("Pass: ")
password = input()
# access_token = HTTPClient.get_access_token(username=userid,
#                                         password=password)

# DEVICE_ID = '81807627-18U3-2S70-25K9-7IO59Q989JQ2'

# # Initialize api client using an access-token
# client = HTTPClient(access_token=ACCESS_TOKEN)

# HTTPClient.log_out(ML_ACCESS_TOKEN)
# HTTPClient.log_out(IN_ACCESS_TOKEN)
"""
