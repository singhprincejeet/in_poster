from flask import Flask, request, send_file
from main_controller import MainController

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    return MainController().post(request)

@app.route('/generate', methods=['POST'])
def generate():
    image_src = MainController().generate_image(request)
    return send_file(image_src)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
