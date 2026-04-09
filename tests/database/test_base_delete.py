from schedule_bot.db_models import Teacher
import pytest
from sqlalchemy import select
from schedule_bot.repositories.teacher_repo import TeacherRepo


@pytest.mark.asyncio
async def test_delete(db_session):

    repo = TeacherRepo(db_session)

    new_teacher = Teacher(name="Артемук О.Л.")
    db_session.add(new_teacher)
    await db_session.commit()
    await db_session.refresh(new_teacher)

    teacher_id = new_teacher.id
    result = await repo.delete(teacher_id)

    assert result is True

    query = select(Teacher).where(Teacher.id == teacher_id)
    result = (await db_session.execute(query)).scalar_one_or_none()
    assert result is None

@pytest.mark.asyncio
async def test_delete_fail(db_session):
    repo = TeacherRepo(db_session)

    result = await repo.delete(obj_id = 9999999)

    assert result is False


