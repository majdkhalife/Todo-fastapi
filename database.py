from sqlalchemy import Integer, Boolean, String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./tododatabase.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


class TodoItem(Base):
    __tablename__ = 'todo_items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    difficulty = Column(Integer)
    importance = Column(Integer)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)#always at the end
