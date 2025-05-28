from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use mysql+mysqlconnector because you're using MySQL Connector driver
DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/yolov8"



# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Session and Base
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
