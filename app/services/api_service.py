import requests
import json
import os


class APIService:
    def __init__(self):
        self.token = os.getenv('TOKEN')  # Replace with your actual token
        self.base_url = os.getenv('BASE_URL')
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'User-Agent': 'YourAppName/1.0'
        }

    def create_user_api(self, username, name, public_key):
        """Execute the API call to create a user."""
        url = f'{self.base_url}/user/'
        data = {
            'username': username,
            'name': name,
            'publicKey': public_key
        }
        response = requests.post(url, headers=self.headers,
                                 data=json.dumps(data))

        return response.json()

    def create_folder_api(self, folder_name, description):
        """Execute the API call to create a folder."""
        url = f'{self.base_url}/folder'
        data = {
            'name': folder_name,
            'description': description
        }
        response = requests.post(url, headers=self.headers,
                                 data=json.dumps(data))
        return response.json()
