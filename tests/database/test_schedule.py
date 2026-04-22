import pytest
from datetime import datetime, time
from schedule_bot.repositories.schedule_repo import ScheduleRepo
from schedule_bot.repositories.teacher_repo import TeacherRepo
from schedule_bot.repositories.room_repo import RoomRepo

@pytest.mark.asyncio
async def test_create_lesson_full_logic(db_session):

    s_repo = ScheduleRepo(db_session)
    t_repo = TeacherRepo(db_session)
    r_repo = RoomRepo(db_session)


    teacher = await t_repo.create_teacher(name="Дмитро Іванович")
    room = await r_repo.create_room(name="C-505")


    new_lesson = await s_repo.create_lesson(
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
        elimination=None
    )

    assert new_lesson.id is not None
    assert new_lesson.uuid is not None
    assert new_lesson.date == datetime(2026, 9, 1)
    assert new_lesson.week_day == "MONDAY"
    assert new_lesson.lesson_number == 1
    assert new_lesson.start_time == time(8, 30)
    assert new_lesson.end_time == time(9, 50)
    assert new_lesson.subject == "Бази даних"
    assert new_lesson.subject_type == "(Л)"
    assert new_lesson.teacher_id == teacher.id
    assert new_lesson.room_id == room.id
    assert new_lesson.sub_group == "(підгр. 1)"
    assert new_lesson.elimination is None