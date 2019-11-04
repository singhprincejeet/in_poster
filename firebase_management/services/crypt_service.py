from cryptography.fernet import Fernet

class CryptService():
    def encrypt(self, str):
        encoded_str = str.encode()
        key = self.__get_key()
        return key.encrypt(encoded_str).decode()


    def decrypt(self, str):
        encoded_str = str.encode()
        key = self.__get_key()
        return key.decrypt(encoded_str).decode()


    def __get_key(self):
        file = open('./assets/keys/key.key', 'rb')
        key = file.read()
        file.close()
        return Fernet(key)
