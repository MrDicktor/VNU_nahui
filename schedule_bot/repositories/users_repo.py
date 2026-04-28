from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Users
from sqlalchemy import select

class UsersRepo(BaseAlchemyRepo):

    def __init__(self, session)->None:
        super().__init__(session)
        self.model = Users

    async def create_user(self, telegram_username: str, telegram_id: str, telegram_fullname, user_group: str)-> Users:
        new_user = Users(telegram_id=telegram_id,
                         telegram_username=telegram_username,
                         telegram_fullname=telegram_fullname,
                         user_group=user_group)
        self.session.add(new_user)
        await self.session.commit()

        return new_user

    async def get_group_by_telegram_id(self, telegram_id: int)->str:
        query = select(Users).where(Users.telegram_id == telegram_id)
        group = await self.session.execute(query)
        group = group.scalar_one_or_none()
        return group.user_group

    async def get_user_by_telegram_id(self, id: str)-> Users | None:
        query = select(Users).where(Users.telegram_id == id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()
        return result