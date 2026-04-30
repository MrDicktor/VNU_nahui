import pytest
from schedule_bot.repositories.lessons_group_repo import LessonGroupRepo
from schedule_bot.repositories.room_repo import RoomRepo
from schedule_bot.repositories.schedule_repo import ScheduleRepo
from schedule_bot.repositories.group_repo import GroupRepo
from datetime import time, datetime

from schedule_bot.repositories.teacher_repo import TeacherRepo


@pytest.mark.asyncio
async def test_create_full_lesson(db_session):

    group_repo = GroupRepo(db_session)
    schedule_repo = ScheduleRepo(db_session)
    lesson_group_repo = LessonGroupRepo(db_session)
    teacher_repo = TeacherRepo(db_session)
    room_repo = RoomRepo(db_session)

    teacher = await teacher_repo.create_teacher("Павленко Ю.С.")
    room = await room_repo.create_room("C-508")
    group = await group_repo.create_group("КНІТ-24")
    schedule = await schedule_repo.create_lesson(
        date=datetime(2026, 9, 1),
        weekday="Понеділок",
        lesson_number=1,
        start_time=time(8, 30),
        end_time=time(9, 50),
        subject="Бази даних",
        subject_type="(Л)",
        teacher_id=teacher.id,
        room_id=room.id,
        sub_group="(підгр. 1)",
        elimination=None,
    )

    lesson_group = await lesson_group_repo.create_lesson_group(
        lesson_id=schedule.id,
        group_id=group.id,
    )

    assert lesson_group.id is not None
    assert lesson_group.uuid is not None
    assert lesson_group.lesson_id == schedule.id
    assert lesson_group.group_id == group.id
