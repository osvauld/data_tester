import dotenv

from app.controllers.user_controller import UserController
from app.controllers.folder_controller import FolderController
from app.logger_config import setup_logging

dotenv.load_dotenv()


def main():
    setup_logging()
    user_controller = UserController()
    folder_controller = FolderController()

    # Creating a fake user
    fake_user_response = user_controller.create_fake_user()

    # Creating a fake folder
    #fake_folder_response = folder_controller.create_fake_folder()
    #print("Fake Folder Created:", fake_folder_response)
    #folders = folder_controller.fetch_all_folders()
    #print(folders)
    #users = user_controller.fetch_all_users()
    # Additional application logic can be added here
    #folder_controller.share_folder_with_random_user()


if __name__ == "__main__":
    main()
