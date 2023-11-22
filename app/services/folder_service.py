from faker import Faker
import random
import logging
from app.services.api_service import APIService


class FolderService:
    def __init__(self):
        self.fake = Faker()
        self.logger = logging.getLogger(__name__)
        self.api_service = APIService()

    def generate_folder_data(self):
        """Generate fake folder data."""
        folder_name = (
            self.fake.word(ext_word_list=None)
            + " "
            + self.fake.word(ext_word_list=None)
        )
        description = self.fake.sentence(nb_words=6)
        return folder_name, description

    def fetch_all_folders(self):
        self.logger.info("Fetching all folders")
        folders = self.api_service.fetch_all_folders_api()
        self.logger.info("Fetched all folders")
        return folders['data']

    def fetch_shared_users(self, folder_id):

        self.logger.info(f"Fetching users for folder: {folder_id}")
        response = self.api_service.fetch_shared_users(folder_id)
        users = response['data']
        self.logger.info("Fetched users:")
        return users
    
    def share_folder(self, folders, users):
        try:
            print(folders)
            folder = random.choice(folders)
            shared_users = self.fetch_shared_users(folder['id'])
            shared_user_ids = [user['id'] for user in shared_users]
            print(shared_user_ids)
            users = [user for user in users if user['id'] not in shared_user_ids]
            selected_users = random.sample(users, random.randint(0, 1))
            access_types = ['owner', 'readonly', 'manage']
            users_payload = [{"userId": user['id'], "accessType": random.choice(access_types)} for user in selected_users]
            payload = {"folderId": folder['id'], "users": users_payload}
            self.logger.info(f"Sharing folder {folder['id']} with users {', '.join([user['id'] for user in selected_users])}")
            share_response = self.api_service.share_folder(payload)
            self.logger.info(f"Shared folder: {share_response}")
        except Exception as e:
            self.logger.error(f"Error sharing folder: {e}")