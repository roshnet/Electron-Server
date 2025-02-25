from sqlalchemy import Column, Integer, String
from app.database.models.base import Base


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30), unique=True)
    password_hash = Column(String(512))
