
import logging
import random
from app.services.api_service import APIService
from app.services.folder_service import FolderService
from app.services.credential_service import CredentialService


class CredentialController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()
        self.credential_service = CredentialService()
        self.logger = logging.getLogger(__name__)

    def create_credential(self, no_of_creds=1):

        folders = self.folder_service.fetch_all_folders()
        if not folders:
            self.logger.error("No folders to create credentials in")
            return None
        for _ in range(no_of_creds):
            folder = random.choice(folders)
            shared_users = self.folder_service.fetch_shared_users(folder['id'])
            payload = self.credential_service.generate_credential_payload()
            print(payload)
            payload['folderId'] = folder['id']
            new_encrypted_fields = []
            for user in shared_users:
                public_key = user['publicKey']
                new_field = {}
                new_field['userId'] = user['id']
                new_field['fields'] = []
                for field in payload['encryptedFields']:
                    temp_field = field.copy()
                    temp_field['fieldValue'] = self.credential_service.encrypt_with_public_key(temp_field['fieldValue'], public_key)
                    print(temp_field, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    new_field['fields'].append(temp_field)
                new_encrypted_fields.append(new_field)
            payload['encryptedFields'] = new_encrypted_fields
            print(payload)
            self.logger.info(f"Creating credential in folder {folder['id']}")
            credential = self.api_service.create_credential(payload)

    def share_credential(self, no_of_times=1):
        for _ in range(no_of_times):
            self.credential_service.share_credential()