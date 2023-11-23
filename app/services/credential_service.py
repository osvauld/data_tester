
from faker import Faker
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import random
import logging
from app.services.folder_service import FolderService
from app.services.user_service import UserService
from app.services.api_service import APIService
from app.services.db_service import fetch_private_key

fake = Faker()


class CredentialService:
    def __init__(self):
        self.fake = Faker()
        self.logger = logging.getLogger(__name__)
        self.folder_service = FolderService()
        self.user_service = UserService()
        self.api_service = APIService()

    def generate_credential_payload(self):

        name = fake.word(ext_word_list=None)
        description = fake.sentence(nb_words=6)
        unencrypted_fields = [{"fieldName": fake.word(), "fieldValue": fake.word()}
                              for _ in range(random.randint(1, 5))]
        encrypted_fields = [{"fieldName": fake.word(), "fieldValue": fake.word()}
                            for _ in range(random.randint(1, 3))]
        return {"name": name, "description": description,
                "unencryptedFields": unencrypted_fields,
                "encryptedFields": encrypted_fields}

    def encrypt_with_public_key(self, message, public_key):
        print('message', message)

        try:
            public_key = base64.b64decode(public_key)
            public_key = serialization.load_pem_public_key(
                public_key,
                backend=default_backend()
            )
            encrypted = public_key.encrypt(
                message.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            encrypted_base64 = base64.b64encode(encrypted).decode()
            return encrypted_base64 
        except Exception as e:
            self.logger.error(f"Error encrypting message: {e}")
            return None
    
    def get_credentails_by_folder(self, folder_id):
        try:
            response = self.api_service.get_credentails_by_folder(folder_id)
            return response['data']
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return None
    
    def fetch_credential_by_id(self, credential_id):
        try:
            response = self.api_service.fetch_credential_by_id(credential_id)
            return response['data']
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def share_credential(self):
        try:
            folders = self.folder_service.fetch_all_folders()
            users = self.user_service.fetch_all_users()
            user_private_key = fetch_private_key('josephsmith')
            folder = random.choice(folders)
            credentials = self.get_credentails_by_folder(folder['id'])
            credential = random.choice(credentials)
            credential_data = self.fetch_credential_by_id(credential['id'])
            credential_data['encryptedData'] = self.decrypt_fields(credential_data['encryptedData'], user_private_key)
            shared_user_ids = [user['id'] for user in credential_data['users']]
            users = [user for user in users if user['id'] not in shared_user_ids]
            selected_users = random.sample(users, random.randint(1, 10))
            users_payload = []
            for user in selected_users:
                fields = [{"fieldName": field['fieldName'], "fieldValue": self.encrypt_with_public_key(field['fieldValue'], user['publicKey'])} for field in credential_data['encryptedData']]
                users_payload.append({"userId": user['id'], "fields": fields, "accessType": "read"})
            payload = {"credentialId": credential['id'], "users": users_payload}
            print(payload)
            self.logger.info(f"Sharing credential {credential['id']} with users {', '.join([user['id'] for user in selected_users])}")
            share_response = self.api_service.share_credential({"credentialList":[payload]})
            self.logger.info(f"Shared credential: {share_response}")
        except Exception as e:
            self.logger.error(f"Error sharing credential: {e}")

    def decrypt_fields(self, encrypted_data, private_key):
        private_key = base64.b64decode(private_key)
        private_key = serialization.load_pem_private_key(
            private_key,
            password=None,
            backend=default_backend()
        )
        for field in encrypted_data:
            try:

                print(field['fieldValue'], 'valueee')
                encrypted_value = base64.b64decode(field['fieldValue'])
                decrypted_value = private_key.decrypt(
                    encrypted_value,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                field['fieldValue'] = decrypted_value.decode()
            except Exception as e:
                self.logger.error(f"Error decrypting field {field['fieldName']}: {e}")
                field['fieldValue'] = None
        return encrypted_data