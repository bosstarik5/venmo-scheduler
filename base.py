from flask import Flask
from flask_apscheduler import APScheduler
import atexit
import time
from apscheduler.schedulers.background import BackgroundScheduler

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

    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    print("penis")

@app.before_first_request
def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=execute_scheduled_payments, trigger="interval", seconds=3)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))

app.run(host='0.0.0.0', port=12345)
