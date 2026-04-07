from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import LessonsGroup

class LessonGroupRepo(BaseAlchemyRepo):
    async def create_lesson_group(self, lesson_id: int, group_id: int):
        new_group = LessonsGroup(lesson_id=lesson_id, group_id=group_id)
        self.session.add(new_group)
        await self.session.commit()
        await self.session.refresh(new_group)
        return new_group