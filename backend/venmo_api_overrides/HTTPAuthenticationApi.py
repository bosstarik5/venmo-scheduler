from venmo_api import AuthenticationApi, random_device_id, warn, confirm, AuthenticationFailedError, ApiClient


class HTTPAuthenticationApi(AuthenticationApi):

    TWO_FACTOR_ERROR_CODE = 81109

    def __init__(self, api_client: ApiClient = None, device_id: str = None):
        self.__device_id = device_id or random_device_id()
        self.__api_client = api_client or ApiClient()
        super().__init__(api_client=self.__api_client, device_id=self.__device_id)

    def login_with_credentials_cli(self, username: str, password: str) -> str:
        """
        Pass your username and password to get an access_token for using the API.
        :param username: <str> Phone, email or username
        :param password: <str> Your account password to login
        :return: <str>
        """

        # Give warnings to the user about device-id and token expiration
        # warn("IMPORTANT: Take a note of your device-id to avoid 2-factor-authentication for your next login.")
        # print(f"device-id: {self.__device_id}")
        # warn("IMPORTANT: Your Access Token will NEVER expire, unless you logout manually (client.log_out(token)).\n"
        #     "Take a note of your token, so you don't have to login every time.\n")

        response = self.authenticate_using_username_password(username, password)

        # if two-factor error
        if response.get('body').get('error'):
            self.__send_otp_before_redirect(response)
            return False
            # access_token = self.__two_factor_process_cli(response=response)
            # self.trust_this_device()
        else:
            access_token = response['body']['access_token']

        confirm("Successfully logged in. Note your token and device-id")
        print(f"access_token: {access_token}\n"
             f"device-id: {self.__device_id}")

        return access_token

    def __send_otp_before_redirect(self, response: dict) -> None:
        # send OTP
        otp_secret = response['headers'].get('venmo-otp-secret')
        self.__otp_secret = otp_secret
        if not otp_secret:
            raise AuthenticationFailedError("Failed to get the otp-secret for the 2-factor authentication process. "
                                            "(check your password)")

        self.send_text_otp(otp_secret=otp_secret)

    def two_factor_login(self) -> str:
        """
        Get response from authenticate_with_username_password for a CLI two-factor process
        :param response:
        :return: <str> access_token
        """

        # otp_secret = response['headers'].get('venmo-otp-secret')
        # if not otp_secret:
        #     raise AuthenticationFailedError("Failed to get the otp-secret for the 2-factor authentication process. "
        #                                     "(check your password)")

        # self.send_text_otp(otp_secret=otp_secret)
        user_otp = self.__ask_user_for_otp_password()

        access_token = self.authenticate_using_otp(user_otp, self.__otp_secret)
        self.__api_client.update_access_token(access_token=access_token)
        self.trust_this_device()

        return access_token


    def trust_this_device(self, device_id=None):
        """
        Add device_id or self.device_id (if no device_id passed) to the trusted devices on Venmo
        :return:
        """
        device_id = device_id or self.__device_id
        header_params = {'device-id': device_id}
        resource_path = '/users/devices'

        self.__api_client.call_api(resource_path=resource_path,
                                   header_params=header_params,
                                   method='POST')

        confirm(f"Successfully added your device id to the list of the trusted devices.")
        print(f"Use the same device-id: {self.__device_id} next time to avoid 2-factor-auth process.")

    @staticmethod
    def __ask_user_for_otp_password():

        otp = ""
        while len(otp) < 6 or not otp.isdigit():
            otp = input("Enter OTP that you received on your phone from Venmo: (It must be 6 digits)\n")

        return otp
