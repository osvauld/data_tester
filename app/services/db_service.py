import logging
from app.models import User, Session

# Ensure that your logger is set up at the beginning of your application.
# If you've followed the previous advice, it will be in logger_config.py.
logger = logging.getLogger(__name__)


def write_to_db(user_id, username, private_key, public_key):
    """Write user data to the database."""
    session = Session()
    try:
        user = User(
            userId=user_id,
            username=username,
            privateKey=private_key,
            publicKey=public_key,
        )
        session.add(user)
        session.commit()
        logger.info(f"User {username} with ID {user_id} has been created successfully.")
    except Exception as e:
        # Roll back any changes if something went wrong
        session.rollback()
        logger.error(f"Error occurred when writing to the database: {e}", exc_info=True)
    finally:
        session.close()

        
def fetch_private_key(username):
    """Fetch the private key of a user from the database."""
    session = Session()
    try:
        user = session.query(User).filter_by(username=username).first()
        if user:
            return user.privateKey
        else:
            logger.error(f"No user found with username {username}")
            return None
    except Exception as e:
        logger.error(f"Error occurred when fetching from the database: {e}", exc_info=True)
        return None
    finally:
        session.close()
    

def fetch_all_users():
    """Fetch all users from the database."""
    session = Session()
    try:
        users = session.query(User).all()
        return [user.to_dict() for user in users]
    except Exception as e:
        logger.error(f"Error occurred when fetching from the database: {e}", exc_info=True)
        return None
    finally:
        session.close()