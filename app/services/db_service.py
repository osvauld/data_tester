
import logging
from app.models import User, Session

# Ensure that your logger is set up at the beginning of your application.
# If you've followed the previous advice, it will be in logger_config.py.
logger = logging.getLogger(__name__)


def write_to_db(user_id, username, private_key, public_key):
    """Write user data to the database."""
    session = Session()
    try:
        user = User(userId=user_id, username=username, privateKey=private_key, publicKey=public_key)
        session.add(user)
        session.commit()
        logger.info(f"User {username} with ID {user_id} has been created successfully.")
    except Exception as e:
        # Roll back any changes if something went wrong
        session.rollback()
        logger.error(f"Error occurred when writing to the database: {e}", exc_info=True)
    finally:
        session.close()
