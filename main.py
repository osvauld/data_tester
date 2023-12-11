import dotenv

from app.controllers.user_controller import UserController
from app.controllers.folder_controller import FolderController
from app.controllers.credential_controller import CredentialController
from app.controllers.group_controller import GroupController
from app.logger_config import setup_logging
from app.models.database import init_db
from app.services.db_service import fetch_all_users

dotenv.load_dotenv()


def main():
    setup_logging()
    init_db()
    user_controller = UserController()
    credentail_controller = CredentialController()
    folder_controller = FolderController()
    group_controller = GroupController()

    # Creating a fake user
    #fake_user_response = user_controller.create_fake_user(1000)
    # Creating a fake folder
    #fake_folder_response = folder_controller.create_fake_folder(50)
    folder_controller.share_folder_with_random_user(150)
    credentail_controller.create_credential(1000)
    credentail_controller.share_credential(450)
    group_controller.create_fake_group(50)
    group_controller.add_user_to_group(200)

if __name__ == "__main__":
    main()
