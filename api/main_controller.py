from instapy_cli import client
from PIL import Image
import json

from media.generator import Generator
from style.text_style import TextStyle
from components.text import Text

# {
#     "body": {
# 			"text": "I will take stars from sky\nPut them on her dress\nTake Saturn rings\nAnd crown her a princess",
#         "size": "36",
#         "align": "center",
#         "color": "0"
#     }, "footer":  {
#         "text": "@poetjeet",
#         "size":"15",
#         "align": "center",
#         "color": "0"
#     },
#     "imageBase64": "blank" | base64 image
# }


class MainController:
  def generate_image(self, request):
    body_text, footer_text, image = self.refine_input(request)
    image_src = Generator(body_text, footer_text, image).generate()
    return image_src

  def refine_input(self, request):
    request_json = json.loads(request.form['info'])

    body_text = self.get_text_from_request(request_json['body'])
    footer_text = self.get_text_from_request(request_json['footer'])
    image = self.get_image_from_request(request.files)

    return body_text, footer_text, image

  def get_text_from_request(self, text_json):
    text_style = TextStyle(
      size=int(text_json['size']),
      align=text_json['align'],
      color=text_json['color']
    )
    return Text(text_json['text'], text_style)

  def get_image_from_request(self, images):
    if not bool(images): # check if images is empty
      return None
    image = images['image'].stream
    return Image.open(image)
