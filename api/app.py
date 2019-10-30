from flask import Flask, request
from main_controller import MainController

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    return MainController().post(request)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
