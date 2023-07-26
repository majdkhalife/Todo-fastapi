from sqlalchemy import Integer, Boolean, String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./tododatabase.db'  # HERE you put database name
engine = create_engine(SQLALCHEMY_DATABASE_URL)  # create the engine for it to run
SessionLocal = sessionmaker(autoflush=False, bind=engine)  # create a session
Base = declarative_base()  # create a base class. SQL Alchemy will handle underlying SQL table creation


class TodoItem(Base):  # define the actual database and columns, and will interact with sql alchemy
    __tablename__ = 'todo_items'  # this is where the data is contained. it is contained within database.db
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    difficulty = Column(Integer)
    importance = Column(Integer)
    completed = Column(String, default='False')


Base.metadata.create_all(bind=engine)  # always at the end
