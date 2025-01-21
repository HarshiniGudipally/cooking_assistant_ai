from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///interactions.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Interaction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    query = Column(String, nullable=False)
    response = Column(String, nullable=False)

Base.metadata.create_all(engine)

def save_interaction(query: str, response: str):
    interaction = Interaction(query=query, response=response)
    session.add(interaction)
    session.commit()

def get_interaction_history():
    return session.query(Interaction).all()
