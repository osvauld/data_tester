import dotenv

from app.controllers.user_controller import UserController
from app.controllers.folder_controller import FolderController

dotenv.load_dotenv()


def main():

    user_controller = UserController()
    #folder_controller = FolderController()

    # Creating a fake user
    #fake_user_response = user_controller.create_fake_user()
    #print("Fake User Created:", fake_user_response)

    # Creating a fake folder
    #fake_folder_response = folder_controller.create_fake_folder()
    #print("Fake Folder Created:", fake_folder_response)
    #folders = folder_controller.fetch_all_folders()
    #print(folders)
    users = user_controller.fetch_all_users()
    # Additional application logic can be added here


if __name__ == "__main__":
    main()
