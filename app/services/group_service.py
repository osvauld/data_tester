from faker import Faker
from app.services.api_service import APIService
from app.services.user_service import UserService
import logging
import random


class GroupService:

    def __init__(self):
        self.fake = Faker()
        self.logger = logging.getLogger(__name__)
        self.api_service = APIService()
        self.user_service = UserService()

    def generate_fake_group_name(self):
        """Generate fake group name """
        return self.fake.word()
    
    def fetch_all_groups(self):
        """Fetch all groups"""
        response = self.api_service.fetch_all_groups()
        return response['data']
    
    def fetch_group_users(self, group_id):
        """Fetch all users in a group"""
        response = self.api_service.fetch_group_users(group_id)
        return response['data']
    
    def add_user_to_group(self):
        """Add user to group"""
        all_users = self.user_service.fetch_all_users()
        groups = self.fetch_all_groups()
        group_id = random.choice(groups)['id']
        group_users = self.fetch_group_users(group_id)
        # Fetch random number of user ids
        group_user_ids = [user['id'] for user in group_users]
        # Filter out users that are not in the group
        users_not_in_group = [user for user in all_users if user['id'] not in group_user_ids]

        # Get random number of user IDs
        num_users = random.randint(1, len(users_not_in_group))
        user_ids = [user['id'] for user in users_not_in_group]

        # Get random sample of user IDs
        sample_user_ids = random.sample(user_ids, num_users)
        
        self.api_service.add_members_to_group(group_id, sample_user_ids)
        