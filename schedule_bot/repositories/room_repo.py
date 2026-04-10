from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Room

class RoomRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Room

    async def create_room(self, name: str):
        new_room = Room(name=name)
        self.session.add(new_room)
        await self.session.commit()
        await self.session.refresh(new_room)
        return new_room
