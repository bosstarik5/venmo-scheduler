from backend.api import login
from backend.api.venmo_api_overrides import HTTPClient


def login_test():
    print("User id: ")
    userid = input()
    print("Pass: ")
    password = input()

    login(userid, password)


if __name__ == "__main__":
    login_test()
