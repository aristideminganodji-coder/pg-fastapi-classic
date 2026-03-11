from sqlalchemy import Boolean,Column,Integer,String
from app.database import Base
from sqlalchemy.orm import Relationship

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)

    tasks=Relationship("Task",back_populates="owner")