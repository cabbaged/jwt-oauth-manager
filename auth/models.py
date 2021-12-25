from sqlalchemy import Column, Integer, String
from auth.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(50))


    def __repr__(self):
        return f'<User {self.username!r}>'