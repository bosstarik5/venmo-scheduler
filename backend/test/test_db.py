from library_code import connect, insert_or_update_user
from venmo_api_overrides import HTTPClient


def connect_test():
    session = connect()
    insert_or_update_user(session, 12, 55555, 3312540000)


if __name__ == "__main__":
    connect_test()
