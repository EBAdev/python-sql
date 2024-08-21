"""
Functions for generating random data
"""

from database import Base, engine, Session
from models import User

from faker import Faker

# Drop all tables and recreate them
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)


# Generate fake data
fake = Faker()


def populate_tabels(users: int = 10):
    session = Session()
    for _ in range(users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            password=fake.password(length=10)
        )
        session.add(user)

    # Commit the transaction
    session.commit()


if __name__ == "__main__":
    populate_tabels()
