from backend.api.venmo_api_overrides import HTTPClient


def get_friend_from_user(access_tkn: str):
    client = HTTPClient(access_token=access_tkn)
    venmo_id = str(client.user.get_my_profile().id)
    friends = client.user.get_user_friends_list(user_id=venmo_id)

    friend_arr = []
    for f in friends:
        friend_arr.append(f.__dict__)
    return friend_arr
