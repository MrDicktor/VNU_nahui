from schedule_bot.repositories import (
    GroupRepo,
    TeacherRepo,
    RoomRepo,
    ScheduleRepo,
    LessonGroupRepo,
    UsersRepo,
    CacheUserRepo,
)
from schedule_bot.schedule_services import ScheduleService
from telegram import User
from redis.asyncio import Redis


class UserService:

    def __init__(self, session, redis: Redis):
        self.session = session
        self.redis = redis

        self.group_repo = GroupRepo(session=session)
        self.teacher_repo = TeacherRepo(session=session)
        self.room_repo = RoomRepo(session=session)
        self.lesson_group_repo = LessonGroupRepo(session=session)
        self.schedule_repo = ScheduleRepo(session=session)
        self.user_repo = UsersRepo(session=session)
        self.cache_repo = CacheUserRepo(redis)
        self.schedule_service = ScheduleService(session, redis)

    async def create_user(
        self, telegram_id: str, user_fullname: str, username: str, group: str
    ) -> None:
        if not await self.group_repo.check_group(group):
            await self.schedule_service.save_schedule_into_db(group)
        if not await self.user_repo.get_user_by_telegram_id(telegram_id):
            await self.user_repo.create_user(
                username, telegram_id, user_fullname, group
            )
        await self.cache_repo.set_cache_user(telegram_id, group)

    async def get_user_group(self, telegram_id: str) -> str | None:
        user = await self.cache_repo.get_cache_user(telegram_id)
        if not user:
            user = await self.user_repo.get_user_by_telegram_id(telegram_id)
            await self.cache_repo.set_cache_user(telegram_id, user.user_group)
            return user.user_group
        else:
            return user
