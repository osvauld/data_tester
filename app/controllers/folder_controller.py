
from ..api.api_service import APIService
from ..services.folder_service.folder import FolderService

class FolderController:
    def __init__(self):
        self.api_service = APIService()
        self.folder_service = FolderService()

    def create_fake_folder(self):
        folder_name, description = self.folder_service.generate_folder_data()
        return self.api_service.create_folder_api(folder_name, description)
