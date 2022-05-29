from backend.api import request_payment
from backend.api.venmo_api_overrides import HTTPClient


def request_payment_test():
    print("User id: ")
    userid = input()
    print("Pass: ")
    password = input()

    auth_api = HTTPClient.get_auth_api()

    access_token = auth_api.login_with_credentials_cli(username=userid, password=password)
    if not access_token:
        # ask for OTP
        access_token = auth_api.two_factor_login()

    amnt = float(input("Enter amount: "))
    request_id = input("Enter requestee id: ")
    note = input("Enter a note for the request: ")

    request_payment(access_token, amnt, note, request_id)

    # HTTPClient.log_out(access_token)


if __name__ == "__main__":
    request_payment_test()
