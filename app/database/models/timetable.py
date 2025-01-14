from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from app.database.models.base import Base
from app.database.models.subjects import Subjects
from app.database.models.classes import Classes


class Timetable(Base):
    __tablename__ = "timetable"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey(Subjects.id))
    class_id = Column(Integer, ForeignKey(Classes.id))
    start_time = Column(DateTime)
    duration = Column(Integer)
    day = Column(String(30))
