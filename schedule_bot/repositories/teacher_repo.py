from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Teacher

class TeacherRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Teacher

    async def create_teacher(self, teacher: str):
        new_teacher = Teacher(name=teacher)
        self.session.add(new_teacher)
        await self.session.commit()
        await self.session.refresh(new_teacher)
        return new_teacher
