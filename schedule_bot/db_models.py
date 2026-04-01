from sqlalchemy import create_engine, Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

engine = create_engine(os.getenv("DB_URL"))
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class ScheduleConstants:
    MAX_WEEK_DAY = 10
    MAX_SUBJECT = 100
    MAX_SUBJECT_TYPE = 5
    MAX_SUB_GROUP = 20
    MAX_ELIMINATION = 500
    MAX_ROOM_NAME = 10
    MAX_TEACHER_NAME = 100
    MAX_GROUP_NAME = 10

class Schedule(Base):
    __tablename__ = 'Lesson_schedule'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    date = Column(DateTime)
    week_day = Column(String(ScheduleConstants.MAX_WEEK_DAY))
    lesson_number = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    subject = Column(String(ScheduleConstants.MAX_SUBJECT))
    subject_type = Column(String(ScheduleConstants.MAX_SUBJECT_TYPE))
    teacher_id = Column(Integer, ForeignKey('Teacher.id'))
    room_id = Column(Integer, ForeignKey('Room.id'))
    sub_group = Column(String(ScheduleConstants.MAX_SUB_GROUP), nullable=True)
    elimination = Column(String(ScheduleConstants.MAX_ELIMINATION), nullable=True)
    creation_date = Column(DateTime)
    actualization_date = Column(DateTime, nullable=True)

class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(ScheduleConstants.MAX_ROOM_NAME))
    creation_date = Column(DateTime)

class Teacher(Base):
    __tablename__ = 'Teacher'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(ScheduleConstants.MAX_TEACHER_NAME))
    creation_date = Column(DateTime)

class Group(Base):
    __tablename__ = 'Group'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(ScheduleConstants.MAX_GROUP_NAME))
    creation_date = Column(DateTime)

class LessonsGroup(Base):
    __tablename__ = 'Lessons_group'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    lesson_id = Column(Integer, ForeignKey('Lesson_schedule.id'))
    group_id = Column(Integer, ForeignKey('Group.id'))
    creation_date = Column(DateTime)


