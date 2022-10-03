import os
import requests
from flask import Flask, jsonify, request 
# from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'welcome home '
auth = HTTPDigestAuth()

users = {
    'vcu': 'rams'
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/ping', methods=['GET'])
#@auth.login_required
def pingService():
    ping = requests.get('https://eric-pong-app.herokuapp.com/pong')

    return jsonify({
    'pingpong_t': str(ping.elapsed.total_seconds()*1000)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50002)