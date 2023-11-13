import requests
import json
import os
import logging


class APIService:
    def __init__(self):
        self.token = os.getenv("TOKEN")  # Replace with your actual token
        self.base_url = os.getenv("BASE_URL")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "User-Agent": "YourAppName/1.0",
        }
        self.logger = logging.getLogger(__name__)

    def create_user_api(self, username, name, public_key):
        try:
            url = f"{self.base_url}/user/"
            data = {"username": username, "name": name, "publicKey": public_key}
            self.logger.info(f"Creating user with data: {data}")
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            self.logger.info(f"User created: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def create_folder_api(self, folder_name, description):
        try:
            url = f"{self.base_url}/folder"
            data = {"name": folder_name, "description": description}
            self.logger.info(f"Creating folder with data: {data}")
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            self.logger.info(f"Folder created: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def fetch_all_folders_api(self):
        try:
            url = f"{self.base_url}/folders"
            self.logger.info(f"Fetching all folders")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched all folders: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def fetch_all_users_api(self):
        try:
            url = f"{self.base_url}/users"
            self.logger.info("Fetching all users")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched all users: {respdata_tester}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None
    
    def get_users_for_folder(self, folder_id):
        try:
            url = f"{self.base_url}/folder/{folder_id}"
            self.logger.info(f"Fetching users for folder: {folder_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched users: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def share_secret(self, data):
        try:
            url = f"{self.base_url}/secrets"
            headers = {**self.headers, 'Content-Type': 'application/json'}
            self.logger.info(f"Sharing secret with data: {data}")
            response = requests.put(url, headers=headers, data=json.dumps(data))
            self.logger.info(f"Secret shared: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def create_secret(self, data):
        try:
            url = f"{self.base_url}/credential/"
            headers = {**self.headers, 'Content-Type': 'application/json'}
            self.logger.info(f"Creating secret with data: {data}")
            response = requests.post(url, headers=headers, data=json.dumps(data))
            self.logger.info(f"Secret created: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def get_secrets(self, folder_id):
        try:
            url = f"{self.base_url}/secrets?folderId={folder_id}"
            self.logger.info(f"Fetching secrets for folder: {folder_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched secrets: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def fetch_credential_by_id(self, credential_id):
        try:
            url = f"{self.base_url}/credential/{credential_id}"
            self.logger.info(f"Fetching credential by id: {credential_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched credential: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None