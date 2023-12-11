from app.services.api_service import APIService
from app.services.user_service import UserService
from app.services.group_service import GroupService


class GroupController:
    def __init__(self):
        self.api_service = APIService()
        self.user_service = UserService()
        self.group_service = GroupService()

    def create_fake_group(self, no_of_groups=1):
        for _ in range(no_of_groups):
            group_name = self.group_service.generate_fake_group_name()
            self.api_service.create_group(group_name)
    
    def add_user_to_group(self, no_of_groups=1):
        for _ in range(no_of_groups):
            self.group_service.add_user_to_group()
