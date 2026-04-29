import logging
import re
from schedule_bot.schemas import *
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from schedule_bot.exceptions import GroupNotFoundException
from datetime import datetime
from schedule_bot.constants import ParserConstants

logging.basicConfig(level=logging.INFO)


# мейн
class Parser:
    async def parse(
        self,
        today_date: str,
        week_day: str,
        lesson_number: int,
        lesson_start: str,
        lesson_end: str,
        row: str,
    ) -> LessonSchedule:
        """парсер і тут формуємо LessonSchedule"""
        subject = (
            re.search(r"^.+?(?=\s*\((?:Л|Пр|Зал|Екз|Лаб)\))", row).group(0).strip()
        )
        subject_type = re.search(r"\((Л|Пр|Зал|Екз|Лаб)\)", row).group()
        teacher = re.search(r"(?<=\)\s)([А-ЩЬЮЯҐЄІЇа-щьюяґєії'].+?)(?=\sауд\.)", row)
        # якшо якийсь кончений викладач не пройде по регулярці шоб не зламалось
        if not teacher:
            logging.info(f"{row} is not a teacher")
            teacher = "Не вказано"
        else:
            teacher = teacher.group()
        room = re.search(r"ауд\.\s*[А-ЯA-Z]-[А-Яа-я0-9]+", row).group()
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
            today_date=datetime.strptime(today_date, "%d.%m.%Y").date(),
            week_day=week_day,
            lesson_number=lesson_number,
            start_time=datetime.strptime(lesson_start, "%H:%M").time(),
            end_time=datetime.strptime(lesson_end, "%H:%M").time(),
            subject=Subject(subject=subject, subject_type=subject_type),
            teacher=teacher,
            room=room,
            sub_group=sub_group,
            groups=groups,
            elimination=elimination,
        )
        return lesson

    async def get_lessons_data(self, group: str) -> WeekSchedule:
        encoded_group = quote(group, encoding="cp1251")
        data = (
            "faculty=0&teacher=&course=0&group="
            + encoded_group
            + "&sdate=&edate=&n=700"
        )
        response = requests.post(ParserConstants.URL, data=data)
        response.encoding = "cp1251"
        soup = BeautifulSoup(response.text, "lxml")
        tables = soup.find_all("div", class_="container")
        week_html = tables[1]
        week_days = week_html.find_all(
            "div", class_="col-md-6 col-sm-6 col-xs-12 col-print-6"
        )
        if not week_days:
            raise GroupNotFoundException
        week: list[list[LessonSchedule]] = []

        for weekday in week_days:
            date = weekday.find("h4").text
            today_date = date[:10]
            week_day = date[11:]
            schedule = weekday.find_all("tr")
            day: list[LessonSchedule] = []

            for tr in schedule:
                row = tr.text
                row = row.replace("\xa0", " ")
                # щоб скіпнути рядок в якому немає пари або практика
                if len(row) < 25:
                    continue
                lesson_number = int(row[0])
                lesson_start = row[1:6]
                lesson_end = row[6:11]
                row = row[11:]
                lessons_at_one_time = len(re.findall(r"ауд\.\s*[А-ЯA-Z]-\d+", row))
                # якщо дві пари в один час то це 100% або 2 підгрупи або вибіркові тому розділяємо ці пари і окремо розпрашую
                if lessons_at_one_time > 1:
                    logging.info("далбайоб")
                    if "(підгр. 1)" in row:
                        row = row.replace("(підгр. 1)", "(підгр. 1)\n", 1)
                        row = row.split("\n")
                    # ВОК абревіатура вибіркової дисципліни і її я використовуюю як маркер щоб розділити 2 пари
                    if row.count("ВОК") > 1:
                        row = row.replace("ВОК", "\nВОК")
                        row = row.split("\n")
                        row = row[1:]

                    for sub_row in row:
                        lesson = await self.parse(
                            today_date,
                            week_day,
                            lesson_number,
                            lesson_start,
                            lesson_end,
                            sub_row,
                        )
                        day.append(lesson)
                else:
                    lesson = await self.parse(
                        today_date,
                        week_day,
                        lesson_number,
                        lesson_start,
                        lesson_end,
                        row,
                    )
                    day.append(lesson)
            week.append(day)

        if len(week) < 6:
            week.append(None)

        if len(week) < 7:
            week.append(None)

        # отут ти мабуть доїбешся але я не придумав як тут краще зробити
        week_schema = WeekSchedule(
            day_1=week[0],
            day_2=week[1],
            day_3=week[2],
            day_4=week[3],
            day_5=week[4],
            day_6=week[5],
            day_7=week[6],
        )

        for i in week_schema:
            logging.debug(i)

        return week_schema
