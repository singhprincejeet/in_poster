import firebase_admin
from firebase_admin import db

class FirebaseService:
    def __init__(self):
        firebase_admin.initialize_app(options={
            'databaseURL': 'https://inposter.firebaseio.com',
        })


    def write(self, doc):
        self.__posts().push(doc)


    def __posts(self):
        return db.reference('posts')