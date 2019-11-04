from services.crypt_service import CryptService
from services.firebase_service import FirebaseService

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
    def update(self, request):
        doc = self.__generate_doc(request.get_json())
        FirebaseService().write(doc)
        return 'JSON posted!'


    def __generate_doc(self, request):
        request['read'] = False
        request['user_info']['password'] = CryptService().encrypt(request['user_info']['password'])
        return request
