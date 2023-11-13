import logging
import random
from app.services.api_service import APIService
from app.services.folder_service import FolderService


class FolderController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()
        self.logger = logging.getLogger(__name__)

    def create_fake_folder(self):
        folder_name, description = self.folder_service.generate_folder_data()
        self.logger.info(f"Creating fake folder: {folder_name}")
        folder = self.api_service.create_folder_api(folder_name, description)
        self.logger.info(f"Fake folder created: {folder}")
        return folder

    def fetch_all_folders(self):
        self.logger.info("Fetching all folders")
        folders = self.api_service.fetch_all_folders_api()
        self.logger.info(f"Fetched all folders: {folders}")
        return folders

    def fetch_all_users(self):
        self.logger.info("Fetching all users")
        users = self.api_service.fetch_all_users_api()
        self.logger.info(f"Fetched all users: {users}")
        return users

    def share_folder_with_random_user(self):
        folders = self.fetch_all_folders()
        users = self.fetch_all_users()
        print(folders)
        print(users)
        if not folders or not users:
            self.logger.error("No folders or users to share with")
            return None
        folder = random.choice(folders)
        user = random.choice(users)
        self.logger.info(f"Sharing folder {folder['id']} with user {user['id']}")
        share_response = self.api_service.share_secret({"folderId": folder['id'], "userId": user['id']})
        self.logger.info(f"Shared folder: {share_response}")
        return share_response