import click
from app.services.data_generation import generate_user_data
from app.services.api_service import create_user_api
from app.services.db_service import write_to_db
from app.models import init_db, User
from dotenv import load_dotenv
from app.logger_config import setup_logging

setup_logging()
load_dotenv()


@click.command()
def create_user():
    """Create a user and send data to the local server."""
    username, name, private_key, public_key = generate_user_data()
    response_data = create_user_api(username, name, public_key)

    if response_data.get('success'):
        user_id = response_data.get('data')
        write_to_db(user_id, username, private_key, public_key)
        print(f"User {username} created with ID {user_id}")
    else:
        print("Failed to create user")


if __name__ == "__main__":
    init_db()
    create_user()
