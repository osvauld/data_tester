from app.services.api_service import APIService
from app.services.user_service import UserService
from app.services.db_service import write_to_db
from concurrent.futures import ThreadPoolExecutor, as_completed 


class UserController:
    def __init__(self):
        self.api_service = APIService()
        self.user_service = UserService()

    def create_fake_user_old(self, no_of_users=1):
        for _ in range(no_of_users):
            try:
                username, name, private_key, public_key = self.user_service.generate_user_data()
                response = self.api_service.create_user_api(username, name, public_key)
                print(response)
                write_to_db(response['data'], username, private_key, public_key)
            except Exception as e:
                print(f"An error occurred while creating a fake user: {str(e)}")

    def fetch_all_users(self):
        return self.api_service.fetch_all_users_api()
    

    def create_fake_user(self, no_of_users=1):
        with ThreadPoolExecutor() as executor:
            futures = []
            for _ in range(no_of_users):
                futures.append(executor.submit(self.create_user_task))
            for future in as_completed(futures):
                try:
                    print(future.result())
                except Exception as e:
                    print(f"An error occurred while creating a fake user: {str(e)}")

    def create_user_task(self):
        username, name, private_key, public_key = self.user_service.generate_user_data()
        response = self.api_service.create_user_api(username, name, public_key)
        write_to_db(response['data'], username, private_key, public_key)
        return response