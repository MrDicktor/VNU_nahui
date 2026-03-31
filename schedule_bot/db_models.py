from sqlalchemy import create_engine, Column, Integer, String, DateTime, Time, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

engine = create_engine('postgresql+psycopg2://stas_admin:1280@localhost:5432/vnu_bot')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'Lesson_schedule'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    date = Column(DateTime)
    week_day = Column(String)
    lesson_number = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    subject = Column(String)
    subject_type = Column(String)
    teacher_id = Column(Integer, ForeignKey('Teacher.id'))
    room_id = Column(Integer, ForeignKey('Room.id'))
    sub_group = Column(String, nullable=True)
    elimination = Column(String, nullable=True)
    creation_date = Column(DateTime)
    actualization_date = Column(DateTime, nullable=True)

class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)
    creation_date = Column(DateTime)

class Teacher(Base):
    __tablename__ = 'Teacher'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)
    creation_date = Column(DateTime)

class Group(Base):
    __tablename__ = 'Group'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)
    creation_date = Column(DateTime)

class LessonsGroup(Base):
    __tablename__ = 'Lessons_group'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    lesson_id = Column(Integer, ForeignKey('Lesson_schedule.id'))
    group_id = Column(Integer, ForeignKey('Group.id'))
    creation_date = Column(DateTime)



Base.metadata.create_all(engine)