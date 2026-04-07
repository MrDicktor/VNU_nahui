from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Group

class GroupRepo(BaseAlchemyRepo):
    async def create_group(self, group: str):
        new_group = Group(name=group)
        self.session.add(new_group)
        await self.session.commit()
        await self.session.refresh(new_group)
        return new_group
