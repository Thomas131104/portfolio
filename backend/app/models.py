from sqlalchemy import Column, Integer, String
from .database import Base

class Mail(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)   # tên mail
    content = Column(String)             # nội dung bên trong
    method = Column(String)              # "email" hoặc "outlook"
