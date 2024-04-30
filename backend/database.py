from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

# database configuration
_user = os.getenv("DB_USER")
_password = os.getenv("DB_PASSWORD")
_host = os.getenv("DB_HOST")
_port = os.getenv("DB_PORT", 3306)
_dbName = os.getenv("DB_NAME")

URL_DATABASE = f"mysql+pymysql://{_user}:{_password}@{_host}:{_port}/{_dbName}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()