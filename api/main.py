from flask import send_file

from main_controller import MainController

def generate(request):
    image_src = MainController().generate_image(request)
    return send_file(image_src)
