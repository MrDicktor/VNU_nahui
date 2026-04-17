from pydantic import BaseModel
from typing import Literal, Optional, List
from datetime import time, datetime, date


subject_type = Literal["(Л)", "(Пр)", "(Зал)", "(Екз)", "(Лаб)"]


class Subject(BaseModel):
    subject: str
    subject_type: subject_type

class LessonSchedule(BaseModel):
    today_date: date
    week_day: str
    lesson_number: int
    start_time: time
    end_time: time
    subject: Subject
    teacher: str
    room: str
    sub_group: Optional[str]
    groups: Optional[str]
    elimination: Optional[str]


class WeekSchedule(BaseModel):
    day_1: list[LessonSchedule]
    day_2: list[LessonSchedule]
    day_3: list[LessonSchedule]
    day_4: list[LessonSchedule]
    day_5: list[LessonSchedule]
    day_6: Optional[list[LessonSchedule]] #якщо сьогодні вихідний то парсяться 5 днів, якщо будній то 6

