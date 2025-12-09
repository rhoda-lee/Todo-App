from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# Acess databe credentials
database_username = os.getenv('DB_USERNAME')
database_password = os.getenv('DB_PASSWORD')
database_name = os.getenv('DB_NAME')

# print(database_username, database_password, database_name)

connection_str = f"postgresql+psycopg2://{database_username}:{database_password}@localhost: 5432/{database_name}"

class Base(DeclarativeBase):
    pass

# Create engine
engine = create_engine(connection_str, echo=True)

# Connect to database
try:
    connection = engine.connect()
    print("Located and connected to database")
    connection.close()
except Exception as e:
    print(f"An error occured: {e}")

# Create session factory
DBSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = DBSession