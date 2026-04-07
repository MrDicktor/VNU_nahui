from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Room

class RoomRepo(BaseAlchemyRepo):
    async def create_room(self, room: str):
        new_room = Room(name=room)
        self.session.add(new_room)
        await self.session.commit()
        await self.session.refresh(new_room)
        return new_room
