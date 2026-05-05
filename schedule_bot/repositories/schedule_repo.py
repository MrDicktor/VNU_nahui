from datetime import date, time, datetime, timedelta
from sqlalchemy import select, delete
from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Schedule, Room, Teacher, Group, LessonsGroup
from schedule_bot.constants import ScheduleRepoConstants
from schedule_bot.schemas import DBSchedule
import json
from redis.asyncio import Redis


class ScheduleRepo(BaseAlchemyRepo):

    def __init__(self, session) -> None:
        super().__init__(session)
        self.model = Schedule

    async def create_lesson(
        self,
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
        elimination: int = None,
    ):
        new_lesson = Schedule(
            date=date,
            week_day=ScheduleRepoConstants.UKR_TO_DB.get(weekday),
            lesson_number=lesson_number,
            start_time=start_time,
            end_time=end_time,
            subject=subject,
            subject_type=subject_type,
            teacher_id=teacher_id,
            room_id=room_id,
            sub_group=sub_group,
            elimination=elimination,
        )
        self.session.add(new_lesson)
        await self.session.flush()
        return new_lesson

    async def get_schedule_by_params(
        self, group_name: str, day_command: date
    ) -> list[DBSchedule]:

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
                Schedule.creation_date,
            )
            .join(LessonsGroup, Schedule.id == LessonsGroup.lesson_id)
            .join(Group, LessonsGroup.group_id == Group.id)
            .join(Teacher, Schedule.teacher_id == Teacher.id)
            .join(Room, Schedule.room_id == Room.id)
            .where(
                Group.name == group_name,
                Schedule.date == day_command,
            )
            .order_by(Schedule.lesson_number)
        )

        result = await self.session.execute(query)
        return [DBSchedule.model_validate(row) for row in result]

    async def delete_schedule_by_group(self, group_id) -> None:
        deleted_links_cte = (
            delete(LessonsGroup)
            .where(LessonsGroup.group_id == group_id)
            .returning(LessonsGroup.lesson_id)
            .cte("deleted_links")
        )
        stmt = delete(Schedule).where(
            Schedule.id.in_(select(deleted_links_cte.c.lesson_id))
        )
        await self.session.execute(stmt)
        await self.session.flush()

class CacheScheduleRepo:

    CACHE_KEY_FORMAT = "{university}:{group_name}:{day_date}"

    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def get_cache_schedule(self, group_name: str, day_date:date)-> list[DBSchedule] | None:
        cache_key = self.CACHE_KEY_FORMAT.format(university="vnu",
                                                 group_name=group_name.lower(),
                                                 day_date=day_date.strftime("%Y-%m-%d"))
        cache_data = await self.redis_client.get(cache_key)
        if cache_data:
            data_dict = json.loads(cache_data)
            return [DBSchedule.model_validate(data) for data in data_dict]
        else:
            return None

    async def set_cache_schedule(self, group_name:str, day_date:date, day_schedule: list[DBSchedule])->None:
        #хай поки так буде якшо добавляться університети тоді поміняю
        cache_key = self.CACHE_KEY_FORMAT.format(university = "vnu",
                                                 group_name =group_name.lower(),
                                                 day_date =day_date.strftime("%Y-%m-%d"))
        now = datetime.now()
        midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        seconds_left = int((midnight - now).total_seconds())
        json_data = json.dumps([obj.model_dump(mode='json') for obj in day_schedule])
        await self.redis_client.set(cache_key, json_data, seconds_left)

    async def clear_group_cache(self, group: str):
        pattern = f"{group.lower()}:*"
        async for key in self.redis_client.scan_iter(match=pattern):
            await self.redis_client.delete(key)

