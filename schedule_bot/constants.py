import os
from dotenv import load_dotenv
load_dotenv()

class TelegramBotConstants:
    TOKEN: str = os.getenv("TOKEN")
    ENTER_GROUP_HANDLER_CODE: int = 2
    MENU_HANDLER_CODE: int = 3
    CANCEL_HANDLER_COMMAND: int = 4
    START_HANDLER_COMMAND: str = 'start'
    MAX_MESSAGE_LENGTH: int = 4000
    DATABASE_URL = os.getenv("DB_URL")
    DB_TO_UKR = {
        "MONDAY": "Понеділок",
        "TUESDAY": "Вівторок",
        "WEDNESDAY": "Середа",
        "THURSDAY": "Четвер",
        "FRIDAY": "П'ятниця",
        "SATURDAY": "Субота",
        "SUNDAY": "Неділя"
    }

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

class ParserConstants:
    URL = "https://ps.vnu.edu.ua/cgi-bin/timetable.cgi?n=700"



class ScheduleRepoConstants:
    UKR_TO_DB = {
        "Понеділок": "MONDAY",
        "Вівторок": "TUESDAY",
        "Середа": "WEDNESDAY",
        "Четвер": "THURSDAY",
        "П'ятниця": "FRIDAY",
        "Субота": "SATURDAY",
        "Неділя": "SUNDAY"
    }
