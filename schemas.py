from pydantic import BaseModel
from typing import Literal, Optional, List
from datetime import time, datetime


SUBJECT_TYPE = Literal["(Л)", "(Пр)", "(Зал)", "(Екз)", "(Лаб)"]


class Subject(BaseModel):
    subject: str
    type: SUBJECT_TYPE

class LessonSchedule(BaseModel):
    lesson_number: int
    start_time: time
    end_time: time
    subject: Subject
    teacher: str
    room: str
    sub_group: Optional[str]
    groups: Optional[str]
    elimination: Optional[str]

class DaySchedule(BaseModel):
    date: str
    schedule: list[LessonSchedule]

class WeekSchedule(BaseModel):
    day_1: DaySchedule
    day_2: DaySchedule
    day_3: DaySchedule
    day_4: DaySchedule
    day_5: DaySchedule
    day_6: Optional[DaySchedule] #якщо сьогодні вихідний то парсяться 5 днів, якщо будній то 6

