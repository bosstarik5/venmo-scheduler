from venmo_api import Client, ApiClient, UserApi, PaymentApi, AuthenticationApi, validate_access_token


class HTTPClient(Client):

    def __init__(self, access_token: str):
        """
        VenmoAPI Client
        :param access_token: <str> Need access_token to work with the API.
        """
        super().__init__(access_token)

    # override the parent method
    @staticmethod
    def get_access_token(username: str, password: str, device_id: str = None) -> str:
        """
        Log in using your credentials and get an access_token to use in the API
        :param username: <str> Can be username, phone number (without +1) or email address.
        :param password: <str> Account's password
        :param device_id: <str> [optional] A valid device-id.

        :return: <str> access_token
        """
        authn_api = AuthenticationApi(api_client=ApiClient(), device_id=device_id)
        return authn_api.login_with_credentials_cli(username=username, password=password)
