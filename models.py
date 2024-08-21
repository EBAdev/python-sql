"""
Table structure in database
"""


from database import Base
from sqlalchemy import ForeignKey, Column, String, Integer, CHAR


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(255), unique=True)
    password = Column("password", String(255))
    email = Column("email", String(255), unique=True)
    firstname = Column("firstname", String(255))
    lastname = Column("lastname", String(255))

    def __init__(self, username, password, email, firstname, lastname):
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"({self.id}, {self.username}) {self.firstname} {self.lastname} "
