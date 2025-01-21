from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
from backend import openai_service
from typing import List

# Database setup
DATABASE_URL = "sqlite:///./cooking_conversations.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    role = Column(String)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class Query(BaseModel):
    session_id: str
    content: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/chat")
async def chat(query: Query, db: SessionLocal = Depends(get_db)):
    # Retrieve conversation history
    history = db.query(Conversation).filter(Conversation.session_id == query.session_id).order_by(Conversation.timestamp).all()
    messages = [{"role": conv.role, "content": conv.content} for conv in history]
    messages.append({"role": "user", "content": query.content})

    # Get AI response
    ai_response = await openai_service.get_ai_response(messages)

    # Save user message and AI response to database
    db.add(Conversation(session_id=query.session_id, role="user", content=query.content))
    db.add(Conversation(session_id=query.session_id, role="assistant", content=ai_response))
    db.commit()

    return {"response": ai_response}

@app.get("/history/{session_id}")
async def get_history(session_id: str, db: SessionLocal = Depends(get_db)):
    history = db.query(Conversation).filter(Conversation.session_id == session_id).order_by(Conversation.timestamp).all()
    return [{"role": conv.role, "content": conv.content, "timestamp": conv.timestamp} for conv in history]
