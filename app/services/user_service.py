import base64
from faker import Faker
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from app.services.api_service import APIService
import logging


class UserService:
    def __init__(self):
        self.fake = Faker()
        self.api_service = APIService()
        self.logger = logging.getLogger(__name__)

    def generate_user_data(self):
        """Generate fake user data and a key pair."""
        username = self.fake.user_name()
        name = self.fake.name()
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        encoded_public_key = base64.b64encode(public_pem).decode("utf-8")
        encoded_private_key = base64.b64encode(private_pem).decode("utf-8")
        return username, name, encoded_private_key, encoded_public_key

    def fetch_all_users(self):
        self.logger.info("Fetching all users")
        users = self.api_service.fetch_all_users_api()
        self.logger.info("Fetched all users")
        return users['data']