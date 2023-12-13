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
            self.logger.info("Fetched all folders:")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def fetch_all_users_api(self):
        try:
            url = f"{self.base_url}/users"
            self.logger.info("Fetching all users")
            response = requests.get(url, headers=self.headers)
            self.logger.info("Fetched all users: ")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None
    
    def get_users_for_folder(self, folder_id):
        try:
            url = f"{self.base_url}/folder/{folder_id}"
            self.logger.info(f"Fetching users for folder: {folder_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info(f"Fetched users: ")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def share_credential(self, data):
        try:
            url = f"{self.base_url}/credentials"
            headers = {**self.headers, 'Content-Type': 'application/json'}
            self.logger.info(f"Sharing secret with data: {data}")
            response = requests.put(url, headers=headers, data=json.dumps(data))
            self.logger.info(f"Secret shared: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def create_credential(self, data):
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

    def get_credentails_by_folder(self, folder_id):
        try:
            url = f"{self.base_url}/folder/{folder_id}/credential"
            self.logger.info(f"Fetching secrets for folder: {folder_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info("Fetched secrets: ")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def fetch_credential_by_id(self, credential_id):
        try:
            url = f"{self.base_url}/credential/{credential_id}"
            self.logger.info(f"Fetching credential by id: {credential_id}")
            response = requests.get(url, headers=self.headers)
            self.logger.info("Fetched credential ")
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def share_folder(self, payload):
        url = f"{self.base_url}/folder"
        response = requests.put(url, headers=self.headers, data=json.dumps(payload))
        self.logger.info(f"Shared folder: {response.json()}")
        return response.json()

    def fetch_shared_users(self, folder_id):
        url = f"{self.base_url}/folder/{folder_id}/users"
        response = requests.get(url, headers=self.headers)
        self.logger.info("Fetched shared users: ")
        return response.json()

    def create_group(self, name):
        url = f"{self.base_url}/group"
        payload = {
            'name': name
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        self.logger.info(f"Created group: {response.json()}")
        return response.json()
    
    def add_members_to_group(self, group_id, members):
        url = f"{self.base_url}/group/members"
        payload = {
            'groupId': group_id,
            'members': members
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        self.logger.info(f"Added members to group: {response.json()}")
        return response.json()

    def fetch_all_groups(self):
        url = f"{self.base_url}/groups"
        response = requests.get(url, headers=self.headers)
        self.logger.info(f"Fetched all groups: {response.json()}")
        return response.json()
    
    def fetch_group_users(self, group_id):
        url = f"{self.base_url}/group/{group_id}"
        response = requests.get(url, headers=self.headers)
        self.logger.info(f"Fetched group: ")
        return response.json()