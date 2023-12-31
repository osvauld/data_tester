from sqlalchemy import Column, String
from .database import Base


class User(Base):

    __tablename__ = "users"
    userId = Column(String, primary_key=True)
    username = Column(String)
    privateKey = Column(String)
    publicKey = Column(String)
    
    def to_dict(self):
        return {
            'id': self.userId,
            'username': self.username,
            'privateKey': self.privateKey
        }