from library_code import connect, insert_or_update_user, get_phone_number
from venmo_api_overrides import HTTPClient


def connect_test():
    session = connect()
    insert_or_update_user(session, 12, 55555, '3312549003')
    # print(get_phone_number(session, 1))


if __name__ == "__main__":
    connect_test()
