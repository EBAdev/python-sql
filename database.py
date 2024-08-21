"""
Database connection
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

# DB engine
engine = create_engine(f"mysql+pymysql://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@" +
                       f"{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}", echo=True)

# Base table class
Base = declarative_base()


# Create a session
Session = sessionmaker(bind=engine)

