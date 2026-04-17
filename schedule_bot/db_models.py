from sqlalchemy import create_engine, Column, Integer, String, DateTime, Time, ForeignKey, func, Date, BigInteger
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv
import os
import uuid


load_dotenv()

# engine = create_engine(os.getenv("DB_URL"))
# Session = sessionmaker(bind=engine)
# session = Session()
Base = declarative_base()

class DataBaseConstants:
    MAX_WEEK_DAY = 10
    MAX_SUBJECT = 100
    MAX_SUBJECT_TYPE = 10
    MAX_SUB_GROUP = 20
    MAX_ELIMINATION = 500
    MAX_ROOM_NAME = 10
    MAX_TEACHER_NAME = 100
    MAX_GROUP_NAME = 10
    MAX_USERNAME = 33
    MAX_FULL_NAME = 65
    MAX_TELEGRAM_ID = 32


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    creation_date = Column(DateTime, server_default=func.timezone('utc', func.now()))


class Schedule(BaseModel):
    __tablename__ = 'lesson_schedule'
    date = Column(Date)
    week_day = Column(String(DataBaseConstants.MAX_WEEK_DAY))
    lesson_number = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    subject = Column(String(DataBaseConstants.MAX_SUBJECT))
    subject_type = Column(String(DataBaseConstants.MAX_SUBJECT_TYPE))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    room_id = Column(Integer, ForeignKey('room.id'))
    sub_group = Column(String(DataBaseConstants.MAX_SUB_GROUP), nullable=True)
    elimination = Column(String(DataBaseConstants.MAX_ELIMINATION), nullable=True)
    actualization_date = Column(DateTime, nullable=True, onupdate=func.timezone('utc', func.now()))

class Room(BaseModel):
    __tablename__ = 'room'
    name = Column(String(DataBaseConstants.MAX_ROOM_NAME), unique=True)


class Teacher(BaseModel):
    __tablename__ = 'teacher'
    name = Column(String(DataBaseConstants.MAX_TEACHER_NAME))


class Group(BaseModel):
    __tablename__ = 'group'
    name = Column(String(DataBaseConstants.MAX_GROUP_NAME), unique=True)


class LessonsGroup(BaseModel):
    __tablename__ = 'lessons_group'
    lesson_id = Column(Integer, ForeignKey('lesson_schedule.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


class Users(BaseModel):
    __tablename__ = 'users'
    telegram_id = Column(String(DataBaseConstants.MAX_TELEGRAM_ID))
    telegram_username = Column(String(DataBaseConstants.MAX_USERNAME))
    telegram_fullname = Column(String(DataBaseConstants.MAX_FULL_NAME))
    user_group = Column(String, ForeignKey('group.name'))




