import datetime
import time

from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Room, Schedule


class ScheduleRepo(BaseAlchemyRepo):
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
            week_day=weekday,
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
        await self.session.commit()
        await self.session.refresh(new_lesson)
        return new_lesson

