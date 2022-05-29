from flask import Flask, render_template, make_response, request, jsonify
from . import venmo_login, get_friend_from_user
from backend.database import connect, insert_or_update_user, get_access_token, get_scheduled

app = Flask(__name__)


@app.route('/api/')
@app.route('/api')
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
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response


@app.route('/api/friends', methods=['POST'])
def get_friends():
    body = request.get_json()
    session = connect()
    acc_token = get_access_token(session, body["user_id"])
    friend_list = get_friend_from_user(acc_token)
    response = make_response(friend_list, 200,)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response


# body = request.json()
@app.route('/api/get_scheduled', methods=['GET'])
def get_scheduled_requests():
    resp_code = 400
    user_id = request.get_json()["user_id"]
    with connect() as session:
        scheduled_requests = get_scheduled(session, user_id)
        resp_code = 200
        response = make_response(jsonify({"requests" : scheduled_requests}), resp_code,)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

app.run(host='0.0.0.0', port=5000, use_reloader=False)
