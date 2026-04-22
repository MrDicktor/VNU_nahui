from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Room
from sqlalchemy import select

class RoomRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Room

    async def create_room(self, name: str):
        new_room = Room(name=name)
        self.session.add(new_room)
        await self.session.flush()
        return new_room

    async def check_room(self, name: str):
        query = select(Room).where(Room.name == name)
        res = await self.session.execute(query)
        db_room = res.scalar_one_or_none()
        return db_room