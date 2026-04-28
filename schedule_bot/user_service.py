from schedule_bot.repositories import GroupRepo, TeacherRepo, RoomRepo, ScheduleRepo, LessonGroupRepo, UsersRepo
from schedule_bot.schedule_services import ScheduleServices
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
        self.schedule_service = ScheduleServices(session)


    async def new_user(self, user_info: User, group: str)->None:
        if not await self.group_repo.check_group(group):
            await self.schedule_service.save_schedule_into_db(group)
        user_id = str(user_info.id)
        user_fullname = user_info.full_name
        username = user_info.username
        await self.user_repo.create_user(username, user_id, user_fullname, group)


    async def user_exists(self, telegram_id: str)-> str | None:
        return await self.user_repo.get_user_by_telegram_id(telegram_id)