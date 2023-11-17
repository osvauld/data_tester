import logging
import random
from app.services.api_service import APIService
from app.services.folder_service import FolderService
from app.services.user_service import UserService
from app.services.credential_service import CredentialService


class FolderController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()
        self.credential_service = CredentialService()
        self.user_service = UserService()
        self.logger = logging.getLogger(__name__)

    def create_fake_folder(self, no_of_folders=1):
        print(no_of_folders)
        for _ in range(no_of_folders):
            folder_name, description = self.folder_service.generate_folder_data()
            self.logger.info(f"Creating fake folder: {folder_name}")
            folder = self.api_service.create_folder_api(folder_name, description)
            self.logger.info(f"Fake folder created: {folder}")

        return
    
    def share_folder_with_random_user(self, iterations=1):
        folders = self.folder_service.fetch_all_folders()
        users = self.user_service.fetch_all_users()
        if not folders or not users:
            self.logger.error("No folders or users to share with")
            return None
        for _ in range(iterations):
            self.folder_service.share_folder(folders, users)
        return
