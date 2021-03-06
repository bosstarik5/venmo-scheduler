from flask import Flask, render_template, make_response, request, jsonify
from . import venmo_login, get_friend_from_user
from backend.database import *

app = Flask(__name__)


@app.route('/api')
@app.route('/api/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200

@app.route('/api/login', methods=['POST'])
def login():
    resp_code = 400
    user_id = None

    # Gets the user and pass
    body = request.get_json()

    # Get access token from venmo
    acc_token, venmo_id, phone = venmo_login(body["username"], body["password"])
    if acc_token:
        session = connect()
        user_id = insert_or_update_user(session, venmo_id, acc_token, phone)
        resp_code = 200

    # Return with make response
    response = make_response(jsonify({"user_id": user_id}), resp_code)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/api/schedule', methods=['POST'])
def schedule_request():
    body = request.get_json()
    session = connect()
    freq_unit = body["frequency_unit"]
    if freq_unit == "days":
        freq = body["frequency"] * 3600 * 24
    elif freq_unit == "months":
        freq = body["frequency"] * 3600 * 24 * 30
    elif freq_unit == "minutes":
        freq = body["frequency"] * 60
    elif freq_unit == "seconds":
        freq = body["frequency"]
    else:
        response = make_response(jsonify({ "message": "Invalid frequency unit."}), 400)
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response

    # get user info from DB
    # *** need to authenticate requests later on with JWTs
    # access_token = get_access_token(session, body["id"])
    insert_request(session, body["user_id"], body["target_user_venmo_id"], body["amount"],
        body["text"], freq, body["start_date"], body["end_date"])

    response = make_response(jsonify({ "message": "success"}), 200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/api/friends', methods=['POST'])
def get_friends():
    body = request.get_json()
    session = connect()
    acc_token = get_access_token(session, body["user_id"])
    friend_list = get_friend_from_user(acc_token)
    response = make_response({ "friends": [f["_json"] for f in friend_list] }, 200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/api/get-scheduled', methods=['POST'])
def get_scheduled_requests():
    resp_code = 400
    user_id = request.get_json()["user_id"]
    with connect() as session:
        scheduled_requests = get_scheduled(session, user_id)
        print(scheduled_requests)
        resp_code = 200
        response = make_response(jsonify({"requests" : [req.to_dict() for req in scheduled_requests]}), resp_code)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

app.run(host='0.0.0.0', port=5000, use_reloader=False)
