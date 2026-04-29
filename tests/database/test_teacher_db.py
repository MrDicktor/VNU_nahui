import pytest
from schedule_bot.repositories.teacher_repo import TeacherRepo


@pytest.mark.asyncio
async def test_create_teacher(db_session):
    repo = TeacherRepo(db_session)
    test_name = "Павленко Ю.С."

    new_teacher = await repo.create_teacher(name=test_name)

    assert new_teacher.id is not None
    assert new_teacher.name == test_name
    assert new_teacher.uuid is not None
