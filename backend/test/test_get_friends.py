from backend.api import get_friend_from_user
from backend.api.venmo_api_overrides import HTTPClient


def get_friend_test():
    print("User id: ")
    userid = input()
    print("Pass: ")
    password = input()

    auth_api = HTTPClient.get_auth_api()

    access_token = auth_api.login_with_credentials_cli(username=userid, password=password)
    if not access_token:
        # ask for OTP
        access_token = auth_api.two_factor_login()

    print(get_friend_from_user(access_token))

    HTTPClient.log_out(access_token)


if __name__ == "__main__":
    get_friend_test()
