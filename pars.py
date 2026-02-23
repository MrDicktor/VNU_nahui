import logging
import bs4
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote, quote
from exceptions import GroupNotFoundException
from pydantic import BaseModel
from typing import Literal, Optional, List
from datetime import time

logging.basicConfig(level=logging.INFO)

# модель всі діла
SUBJECT_TYPE_VARIANTS = Literal["(Л)", "(Пр)", "(Зал)", "(Екз)", "(Лаб)"]
TEACHER_STATUS = Literal["зав", "ст. викл.", "ст.викл.", "проф.", "доц.", "асист.", "зав.каф.,доц", "доц. "]


class Subject(BaseModel):
    subject: str
    type: SUBJECT_TYPE_VARIANTS


class Teacher(BaseModel):
    status: TEACHER_STATUS
    teacher: str


class DaySchedule(BaseModel):
    lesson_number: int
    start_time: time
    end_time: time
    subject: Subject
    teacher: Teacher
    room: str
    groups: Optional[str]
    elimination: Optional[str]


class Schedule(BaseModel):
    group_name: str
    monday: List[DaySchedule]
    tuesday: List[DaySchedule]
    wednesday: List[DaySchedule]
    thursday: List[DaySchedule]
    friday: List[DaySchedule]
    saturday: List[DaySchedule]


# клас з константами вроді так треба
class ParserConstants:
    LESSON_MARKERS = ["(Л)", "(Пр)", "(Зал)", "(Екз)", " (Лаб)"]
    TEACHER_MARKERS = ["ст. викл.", "ст.викл.", "проф.", "доц.", "асист.", "зав.каф.,доц", "доц. "]
    AUDITORY_MARKER = 'ауд.'
    GROUP_MARKER = ['Збірна група', 'Потік']
    SPECIAL_MARKER = "Ліквідація"
    URL = "https://ps.vnu.edu.ua/cgi-bin/timetable.cgi?n=700"


# мейн
class Parser:
    @staticmethod
    def main() -> Schedule:
        raw_days: List[List[List[str]]] = []
        writing = ""
        group = "КНІТ-24"
        encoded_group = quote(group, encoding='cp1251')
        data = "faculty=0&teacher=&course=0&group=" + encoded_group + "&sdate=&edate=&n=700"
        response = requests.post(ParserConstants.URL, data=data)
        response.encoding = 'cp1251'
        soup = BeautifulSoup(response.text, "lxml")
        tables = soup.find_all("div", class_="container")
        week = tables[1]
        week_days = week.find_all("div", class_="col-md-6 col-sm-6 col-xs-12 col-print-6")
        for weekday in week_days:
            raw_lessons: List[List[str]] = []
            date = weekday.find("h4")
            writing += date.text + "\n" + "\n"
            schedule = weekday.find_all("tr")
            for tr in schedule:
                row = tr.text
                row = row.replace('\xa0', ' ')
                if len(row) < 13:
                    continue
                lesson_number = row[0]
                start_time = row[1:6].strip()
                end_time = row[6:11]
                row = lesson_number + "\n" + row[1:6].strip() + "\n" + row[6:11] + "\n" + row[11:]
                for marker in ParserConstants.LESSON_MARKERS:
                    if marker in row:
                        row = row.replace(marker, "\n" + marker + "\n", 1)
                        break
                for marker in ParserConstants.TEACHER_MARKERS:
                    if marker in row:
                        row = row.replace(marker, marker + "\n", 1)
                        break
                row = row.replace(ParserConstants.AUDITORY_MARKER, "\n" + ParserConstants.AUDITORY_MARKER, 1)
                row = row.replace(ParserConstants.SPECIAL_MARKER, "\n" + ParserConstants.SPECIAL_MARKER, 1)
                for gr in ParserConstants.GROUP_MARKER:
                    row = row.replace(gr, "\n" + gr, 1)
                writing += row + "\n"
                test = row.split("\n")
                test = [i.strip() for i in test]
                raw_lessons.append(test)
                print(test)
            raw_days.append(raw_lessons)
            with open(group + ".txt", "w", encoding="utf-8") as f:
                f.write(writing)
        # створюєм словники і їх в модель запихаєм
        days: List[List[DaySchedule]] = []
        for day in raw_days:
            lessons: List[DaySchedule] = []
            for data in day:
                lesson_data = {
                    "lesson_number": data[0],
                    "start_time": data[1],
                    "end_time": data[2],
                    "subject": {
                        "subject": data[3],
                        "type": data[4]
                    },
                    "teacher": {
                        "status": data[5],
                        "teacher": data[6]
                    },
                    "room": data[7],
                    "groups": data[8] if len(data) > 8 else None,
                    "elimination": data[9] if len(data) > 9 else None
                }
                lesson = DaySchedule(**lesson_data)
                lessons.append(lesson)
            days.append(lessons)
        # фінальна модель, але з понеділок, вівторок і тд погана ідея бо тиждень всеодно починається на з понеділка а з дня який сьогодні то треба буде перейменувати
        week = Schedule(
            group_name=group,
            monday=days[0],
            tuesday=days[1],
            wednesday=days[2],
            thursday=days[3],
            friday=days[4],
            saturday=days[5],
        )
        logging.info(week)
        return week


if __name__ == "__main__":
    Parser.main()