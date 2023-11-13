from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

# Database setup
engine = create_engine("sqlite:///users.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    try:

        Base.metadata.create_all(engine)
        logger.info("database tables created")
    except Exception as e:
        logger.error("Error initing db %s", e)
