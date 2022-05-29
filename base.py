from flask import Flask
import atexit
import time
import datetime
from sms_functions import make_twilio_client, send_text_message
from venmo_api import GeneralPaymentError, NotEnoughBalanceError
from apscheduler.schedulers.background import BackgroundScheduler
from backend import request_payment, get_requests, update_next, Users, Requests, connect, get_access_token
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200

def execute_scheduled_payments():
    # more code will go here
    # functions to build/have run here:
    # - check_requests: look at the requests table at get all the schedueld requests that need to get sent out
    # - send_requests: send the requests via venmo, get a response
    # - send text message: send a text message to the person who scheduled the payment, letting them know if the request was sent or not
    # - update the requests table
    session = connect()
    cur_time = datetime.datetime.now().timestamp()
    requests_to_handle = get_requests(session, cur_time)
    twilio_client = make_twilio_client()
    for req in requests_to_handle:
        access_token_venmo = get_access_token(session, req.sender_id)
        try:
            sender_num = None
            request_payment(access_token_venmo, req.amount, req.note, req.rec_id)
            send_text_message(twilio_client, sender_num, req.rec_id, req.note, req.amount)
            update_next(session, req.id)
            print(f"payment for {req.id} successful!!!")
        except GeneralPaymentError:
            pass
    return 

@app.before_first_request
def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=execute_scheduled_payments, trigger="interval", seconds=3)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))
    return



app.run(host='0.0.0.0', port=12345)