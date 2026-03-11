from sqlalchemy import Boolean,Column,String,Integer,ForeignKey
from app.database import Base
from sqlalchemy.orm import Relationship

class Task(Base):
    __tablename__="tasks"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    completed=Column(Boolean,default=False)
    user_id=Column(Integer,ForeignKey("users.id"))

    #relation avec le user
    owner=Relationship("User",back_populates="tasks")