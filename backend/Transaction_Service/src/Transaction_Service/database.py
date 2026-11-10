import os
from pathlib import Path

from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


#Create a base class for all the tables in the database.
class Base(DeclarativeBase):
    pass

password_file = os.environ["DB_PASSWORD_FILE"]

# Read the password from the file
with open(password_file, "r") as f:
    password = f.read().strip()

#databes+driver+user+password+host+port+database_name
SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql+psycopg ",
    username="toni",
    password=password,
    host="localhost",
    port=5432,
    database="account_db"
)
#create the database engine using the SQLALCHEMY_DATABASE_URL. 
# The engine is responsible for managing the connection to the database and executing SQL statements.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)



#Create a sessionmaker instance that will be used to create sessions for interacting with the database.
#No autocommit and no autoflush is set to ensure that changes are explicitly committed 
# and that the session does not automatically flush changes to the database.
#bind = engine is set to associate the session with the database engine created earlier.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#create table in the database using the metadata from the Base class.



#Generator function that creates a new database session and yields it to the caller.Clear close after the session is used
#to ensure that the connection to the database is properly closed and resources are released.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()