import logging
import random
from app.services.api_service import APIService
from app.services.folder_service import FolderService


class FolderController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()
        self.logger = logging.getLogger(__name__)

    def create_fake_folder(self, no_of_folders=1):
        print(no_of_folders)
        for _ in range(no_of_folders):
            folder_name, description = self.folder_service.generate_folder_data()
            self.logger.info(f"Creating fake folder: {folder_name}")
            folder = self.api_service.create_folder_api(folder_name, description)
            self.logger.info(f"Fake folder created: {folder}")

        return

    def fetch_all_folders(self):
        self.logger.info("Fetching all folders")
        folders = self.api_service.fetch_all_folders_api()
        self.logger.info("Fetched all folders")
        return folders['data']

    def fetch_all_users(self):
        self.logger.info("Fetching all users")
        users = self.api_service.fetch_all_users_api()
        self.logger.info("Fetched all users")
        return users['data']
    
    def fetch_shared_users(self, folder_id):

        self.logger.info(f"Fetching users for folder: {folder_id}")
        response = self.api_service.fetch_shared_users(folder_id)
        users = response['data']
        print(users)
        users = [{"userId": user['id'], "accessType": user['accessType']} for user in users]
        self.logger.info("Fetched users:")
        return users

    def share_folder_with_random_user(self, iterations=1):
        folders = self.fetch_all_folders()
        users = self.fetch_all_users()
        if not folders or not users:
            self.logger.error("No folders or users to share with")
            return None
        for _ in range(iterations):
            folder = random.choice(folders)
            shared_users = self.fetch_shared_users(folder['id'])
            shared_user_ids = [user['userId'] for user in shared_users]
            users = [user for user in users if user['id'] not in shared_user_ids]
            selected_users = random.sample(users, 3)
            access_types = ['owner', 'readonly', 'manage']
            users_payload = [{"userId": user['id'], "accessType": random.choice(access_types)} for user in selected_users]
            payload = {"folderId": folder['id'], "users": users_payload}
            self.logger.info(f"Sharing folder {folder['id']} with users {', '.join([user['id'] for user in selected_users])}")
            share_response = self.api_service.share_folder(payload)
            self.logger.info(f"Shared folder: {share_response}")
        return 
        