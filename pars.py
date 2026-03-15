import logging
import re
from telegram import Update
from schemas import *
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote, quote
from exceptions import GroupNotFoundException
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)






# клас з константами вроді так треба
class ParserConstants:
    URL = "https://ps.vnu.edu.ua/cgi-bin/timetable.cgi?n=700"


# мейн
class Parser:
    def parse(self, lesson_number: int, lesson_start: time, lesson_end: time, row: str) ->LessonSchedule:
        """парсер і тут формуємо LessonSchedule"""
        subject = re.search(r"^.+?(?=\s*\((?:Л|Пр|Зал|Екз|Лаб)\))", row).group(0)
        subject_type = re.search(r"\((Л|Пр|Зал|Екз|Лаб)\)", row).group()
        teacher = re.search(r"[А-ЯІЇЄҐЬ][а-яіїєґ'ь]+(?:\s+\([а-я\.]+\))?\s+[А-ЯІЇЄҐЬ]\.[А-ЯІЇЄҐЬ]\.", row)
        #якшо якийсь кончений викладач не пройде по регулярці шоб не зламалось
        if not teacher:
            logging.info(f"{row} is not a teacher")
            teacher = "Не вказано"
        else:
            teacher = teacher.group()
        room = re.search(r"ауд\.\s*[А-ЯA-Z]-\d+", row).group()
        sub_group = re.search(r"\(підгр\.\s?(\d+)\)", row)
        if sub_group:
            sub_group = sub_group.group()
        groups = re.search(r"(Збірна група|Потік).*?(?=\s*Ліквідація|$)", row)
        if groups:
            groups = groups.group()
        elimination = re.search(r"Ліквідація.*", row)
        if elimination:
            elimination = elimination.group()

        lesson = LessonSchedule(
            lesson_number=lesson_number,
            start_time=datetime.strptime(lesson_start, "%H:%M").time(),
            end_time=datetime.strptime(lesson_end, "%H:%M").time(),
            subject=Subject(subject=subject, subject_type=subject_type),
            teacher=teacher,
            room=room,
            sub_group=sub_group,
            groups=groups,
            elimination=elimination
        )
        return lesson



    def get_lessons_data(self,  group: str) -> WeekSchedule:
        encoded_group = quote(group, encoding='cp1251')
        data = "faculty=0&teacher=&course=0&group=" + encoded_group + "&sdate=&edate=&n=700"
        response = requests.post(ParserConstants.URL, data=data)
        response.encoding = 'cp1251'
        soup = BeautifulSoup(response.text, "lxml")
        tables = soup.find_all("div", class_="container")
        week_html = tables[1]
        week_days = week_html.find_all("div", class_="col-md-6 col-sm-6 col-xs-12 col-print-6")
        if not week_days:
            raise GroupNotFoundException
        week: list[DaySchedule] = []

        for weekday in week_days:
            date = weekday.find("h4").text
            today_date = date[:10]
            today_date = datetime.strptime(today_date, "%d.%m.%Y").date()
            week_day = date[11:]
            schedule = weekday.find_all("tr")
            day: list[LessonSchedule] = []

            for tr in schedule:
                row = tr.text
                row = row.replace('\xa0', ' ')
                #щоб скіпнути рядок в якому немає пари або практика
                if len(row) < 25:
                    continue
                lesson_number = int(row[0])
                lesson_start = row[1:6]
                lesson_end = row[6:11]
                row = row[11:]
                lessons_at_one_time = len(re.findall(r"ауд\.\s*[А-ЯA-Z]-\d+", row))
                #якщо дві пари в один час то це 100% або 2 підгрупи або вибіркові тому розділяємо ці пари і окремо розпрашую
                if lessons_at_one_time > 1:
                    logging.info("далбайоб")
                    if "(підгр. 1)" in row:
                        row = row.replace("(підгр. 1)", "(підгр. 1)\n", 1)
                    #ВОК абревіатура вибіркової дисципліни і її я використовуюю як маркер щоб розділити 2 пари
                    if row.count("ВОК") > 1:
                        row = row.replace("ВОК", "\nВОК")
                    if "БЗВП." in row:
                        row = row.replace("БЗВП.","\nБЗВП.")
                    if lessons_at_one_time >= 4:
                        row = row.replace("ОНПВ", "\nОНПВ")

                    row = row.split("\n")
                    for sub_row in row:
                        if sub_row == "":
                            continue
                        lesson = self.parse(lesson_number, lesson_start, lesson_end, sub_row)
                        day.append(lesson)
                else:
                    lesson = self.parse(lesson_number, lesson_start, lesson_end, row)
                    day.append(lesson)
            day_scheme = DaySchedule(
                today_date=today_date,
                week_day=week_day,
                schedule= day
            )
            week.append(day_scheme)
        if len(week) <6:
            week.append(None)

#отут ти мабуть доїбешся але я не придумав як тут краще зробити
        week_schema = WeekSchedule(
            day_1=week[0],
            day_2=week[1],
            day_3=week[2],
            day_4=week[3],
            day_5=week[4],
            day_6=week[5],
        )

        for i in week_schema:
            logging.debug(i)

        return week_schema

if __name__ == "__main__":
    Parser.get_lessons_data()