from faker import Faker


class FolderService:
    def __init__(self):
        self.fake = Faker()

    def generate_folder_data(self):
        """Generate fake folder data."""
        folder_name = self.fake.word(ext_word_list=None) + " " + self.fake.word(ext_word_list=None)
        description = self.fake.sentence(nb_words=6)
        return folder_name, description
