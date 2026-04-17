from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Group
from sqlalchemy import select
class GroupRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Group

    async def create_group(self, name: str):
        db_group = await self.check_group(name)
        if db_group:
            return db_group
        else:
            new_group = Group(name=name)
            self.session.add(new_group)
            await self.session.flush()
            return new_group

    async def check_group(self, name: str):
        query = select(Group).where(Group.name == name)
        res = await self.session.execute(query)
        db_group = res.scalar_one_or_none()
        return db_group

