from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Teacher
from sqlalchemy import select

class TeacherRepo(BaseAlchemyRepo):

    def __init__(self, session):
        super().__init__(session)
        self.model = Teacher

    async def create_teacher(self, name: str):
        new_teacher = Teacher(name=name)
        self.session.add(new_teacher)
        await self.session.flush()

        return new_teacher

    async def check_teacher(self, name: str):
        query = select(Teacher).where(Teacher.name == name)
        res = await self.session.execute(query)
        db_group = res.scalar_one_or_none()
        return db_group