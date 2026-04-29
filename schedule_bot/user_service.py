from schedule_bot.repositories import (
    GroupRepo,
    TeacherRepo,
    RoomRepo,
    ScheduleRepo,
    LessonGroupRepo,
    UsersRepo,
)
from schedule_bot.schedule_services import ScheduleService
from telegram import User


class UserService:

    def __init__(self, session):
        self.session = session
        self.group_repo = GroupRepo(session=session)
        self.teacher_repo = TeacherRepo(session=session)
        self.room_repo = RoomRepo(session=session)
        self.lesson_group_repo = LessonGroupRepo(session=session)
        self.schedule_repo = ScheduleRepo(session=session)
        self.user_repo = UsersRepo(session=session)
        self.schedule_service = ScheduleService(session)

    async def create_user(
        self, telegram_id: str, user_fullname: str, username: str, group: str
    ) -> None:
        if not await self.group_repo.check_group(group):
            await self.schedule_service.save_schedule_into_db(group)
        if await self.user_repo.get_user_by_telegram_id(telegram_id):
            pass
        else:
            await self.user_repo.create_user(
                username, telegram_id, user_fullname, group
            )

    async def get_user(self, telegram_id: str) -> str | None:
        return await self.user_repo.get_user_by_telegram_id(telegram_id)
