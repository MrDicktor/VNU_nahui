from datetime import date, time, datetime, timedelta
from sqlalchemy import select
from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import  Schedule, Room, Teacher, Group, LessonsGroup

UKR_TO_DB = {
    "Понеділок": "MONDAY",
    "Вівторок": "TUESDAY",
    "Середа": "WEDNESDAY",
    "Четвер": "THURSDAY",
    "П'ятниця": "FRIDAY",
    "Субота": "SATURDAY",
    "Неділя": "SUNDAY"
}
class ScheduleRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Schedule

    async def create_lesson(self,
                              date: datetime,
                              weekday: str,
                              lesson_number: int,
                              start_time: time,
                              end_time: time,
                              subject: str,
                              subject_type: str,
                              teacher_id: int,
                              room_id: int,
                              sub_group: str = None,
                              elimination: int = None):
        new_lesson = Schedule(
            date=date,
            week_day=UKR_TO_DB.get(weekday),
            lesson_number=lesson_number,
            start_time=start_time,
            end_time=end_time,
            subject=subject,
            subject_type=subject_type,
            teacher_id=teacher_id,
            room_id=room_id,
            sub_group=sub_group,
            elimination=elimination
        )
        self.session.add(new_lesson)
        await self.session.flush()
        return new_lesson


    async def get_schedule_by_params(self, group_name: str, day_command: date):

        query = (
            select(
                Schedule.date,
                Schedule.week_day,
                Schedule.lesson_number,
                Schedule.start_time,
                Schedule.end_time,
                Schedule.subject,
                Schedule.subject_type,
                Schedule.sub_group,
                Teacher.name.label("teacher_name"),
                Room.name.label("room_name"),
                Group.name.label("group_name"),
                Schedule.creation_date
            )
            .join(LessonsGroup, Schedule.id == LessonsGroup.lesson_id)
            .join(Group, LessonsGroup.group_id == Group.id)
            .join(Teacher, Schedule.teacher_id == Teacher.id)
            .join(Room, Schedule.room_id == Room.id)
            .where(
                Group.name == group_name,
                Schedule.date == day_command,
            ).order_by(Schedule.lesson_number)
        )

        result = await self.session.execute(query)
        return result.all()
