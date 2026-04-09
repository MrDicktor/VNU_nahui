from schedule_bot.db_models import Teacher
import pytest
from sqlalchemy import select
from schedule_bot.repositories.teacher_repo import TeacherRepo

@pytest.mark.asyncio
async def test_update(db_session):

    repo = TeacherRepo(db_session)

    new_teacher = Teacher(name="Гришанович О.В")
    db_session.add(new_teacher)
    await db_session.commit()
    await db_session.refresh(new_teacher)
    teacher_id = new_teacher.id

    await repo.update(teacher_id, name= "Павленко Ю.С")


    query = select(Teacher).where(Teacher.id == teacher_id)
    result = (await db_session.execute(query)).scalar_one_or_none()

    assert result.name == "Павленко Ю.С"

@pytest.mark.asyncio
async def test_delete_fail(db_session):
    repo = TeacherRepo(db_session)

    result = await repo.update(obj_id = 9999999)

    assert result is None
