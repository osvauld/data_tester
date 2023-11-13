from app.services.api_service import APIService
from app.services.folder_service import FolderService


class FolderController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()

    def create_fake_folder(self):
        folder_name, description = self.folder_service.generate_folder_data()
        print(folder_name)
        return self.api_service.create_folder_api(folder_name, description)

    def fetch_all_folders(self):
        return self.api_service.fetch_all_folders_api()