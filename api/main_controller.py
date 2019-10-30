from media.generator import Generator
from style.text_style import TextStyle
from components.text import Text
from instapy_cli import client

# {
#     "caption": "we did it",
#     "user_info": {
# 			"username": "poetjeet",
# 			"password": "mein ni dasna"
# 		},
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
#     }
# }

class MainController:
    def post(self, request):
        request_json = request.get_json()
        image_src = self.generate_image(request_json)
        username, password = self.get_user_info(request_json)
        print("Posting for: " + str(username))
        with client(username, password) as cli:
            cli.upload(image_src, request_json['caption'])
        return 'Image posted!'


    def generate_image(self, request_json):
        body_text = self.get_text_from_request(request_json['body'])
        footer_text = self.get_text_from_request(request_json['footer'])

        image_src = Generator(body_text, footer_text).generate()
        return image_src


    def get_text_from_request(self, text_json):
        text_style=TextStyle(
            size=int(text_json['size']),
            align=text_json['align'],
            color=int(text_json['color'])
        )
        return Text(text_json['text'], text_style)


    def get_user_info(self, request_json):
        user_info = request_json['user_info']
        username = user_info['username']
        password = user_info['password']
        return username, password
