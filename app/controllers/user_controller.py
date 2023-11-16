from app.services.api_service import APIService
from app.services.user_service import UserService
from app.services.db_service import write_to_db

class UserController:
    def __init__(self):
        self.api_service = APIService()
        self.user_service = UserService()

    def create_fake_user(self, no_of_users=1):
        for _ in range(no_of_users):
            username, name, private_key, public_key = self.user_service.generate_user_data()
            response = self.api_service.create_user_api(username, name, public_key)
            print(response)
            write_to_db(response['data'], username, private_key, public_key)

    def fetch_all_users(self):
        return self.api_service.fetch_all_users_api()