from ..api.api_service import APIService
from ..services.user_service.user import UserService

class UserController:
    def __init__(self):
        self.api_service = APIService()
        self.user_service = UserService()

    def create_fake_user(self):
        username, name, private_key, public_key = self.user_service.generate_user_data()
        return self.api_service.create_user_api(username, name, public_key)