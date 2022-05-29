from flask import Flask, render_template, make_response, request, jsonify
from backend import login
from backend import connect, insert_or_update_user

app = Flask(__name__)


@app.route('/api/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    error = None
    e = 200

    if request.method == "POST":
        # Gets the user and pass
        body = request.get_json()

        # Get access token from venmo
        acc_token, venmo_id, phone = login(body["username"], body["password"])
        user_exist = False
        if acc_token:
            user_exist = True

        # check for error, set error if exists
        if user_exist:
            # session = connect()
            # userid = update_user(session, venmo_id, acc_token, phone)
            userid = body["username"]

            # Return with make response
            response = make_response(jsonify({"userid": userid}), 200,)
            return response
        else:
            error = 'Invalid username/password'
            e = 400

    # renders the page
    return render_template('login.html', error=error), e


# body = request.json()

app.run(host='0.0.0.0', port=12345, use_reloader=False)
