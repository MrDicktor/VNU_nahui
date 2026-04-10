from schedule_bot.db_models import Teacher
import pytest
from sqlalchemy import select
from schedule_bot.repositories.teacher_repo import TeacherRepo

@pytest.mark.asyncio
async def test_get_teacher(db_session):
    t_name = "Гришанович О.М"

    repo = TeacherRepo(db_session)

    new_teacher = Teacher(name= t_name)
    db_session.add(new_teacher)
    await db_session.commit()
    await db_session.refresh(new_teacher)
    new_teacher_id = new_teacher.id

    result = await repo.get(new_teacher_id)
    assert result.name == t_name


@pytest.mark.asyncio
async def test_get_teacher_not_found(db_session):
    repo = TeacherRepo(db_session)

    result = await repo.get(99999)

    assert result is None