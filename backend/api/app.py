from flask import Flask, render_template, make_response, request, jsonify
from backend import venmo_login
from backend import connect, insert_or_update_user

app = Flask(__name__)


@app.route('/api/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200


@app.route('/api/login', methods=['POST'])
def login():
    resp_code = 400
    userid = None

    # Gets the user and pass
    body = request.get_json()

    # Get access token from venmo
    acc_token, venmo_id, phone = venmo_login(body["username"], body["password"])
    if acc_token:
        session = connect()
        userid = insert_or_update_user(session, venmo_id, acc_token, phone)
        resp_code = 200

    # Return with make response
    response = make_response(jsonify({"userid": userid}), resp_code,)
    return response


# body = request.json()

app.run(host='0.0.0.0', port=5000, use_reloader=False)
