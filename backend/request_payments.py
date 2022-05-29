from venmo_api_overrides import HTTPClient
from venmo_api import GeneralPaymentError, NotEnoughBalanceError


def request_payment(access_tkn: str, amt: float, note: str, target_user_id: str):
    client = HTTPClient(access_token=access_tkn)
    try:
        client.payment.request_money(amt, note, target_user_id)
    except GeneralPaymentError:
        return GeneralPaymentError
    except NotEnoughBalanceError:
        return NotEnoughBalanceError

