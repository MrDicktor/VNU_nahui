from datetime import date

from schedule_bot.parser import Parser
from schedule_bot.repositories import GroupRepo, TeacherRepo, RoomRepo, ScheduleRepo, LessonGroupRepo, UsersRepo


class ScheduleServices:
    def __init__(self, session)->None:
        self.session = session
        self.group_repo = GroupRepo(session=session)
        self.teacher_repo = TeacherRepo(session=session)
        self.room_repo = RoomRepo(session=session)
        self.lesson_group_repo = LessonGroupRepo(session=session)
        self.schedule_repo = ScheduleRepo(session=session)
        self.user_repo = UsersRepo(session=session)
        self.parser = Parser()

    async def save_schedule_into_db(self, group: str)-> None:
        week_schema =  await self.parser.get_lessons_data(group)
        week_schemas = [week_schema.day_1, week_schema.day_2, week_schema.day_3, week_schema.day_4,
                        week_schema.day_5,  week_schema.day_6, week_schema.day_7]

        db_group = await self.group_repo.check_group(group)
        if db_group:
            new_group = db_group
        else:
            new_group = await self.group_repo.create_group(group)

        for today in week_schemas:
            if not today:
                continue
            for lesson in today:

                db_teacher = await self.teacher_repo.get_teacher_by_name(lesson.teacher)
                if db_teacher:
                    new_teacher = db_teacher
                else:
                    new_teacher =await self.teacher_repo.create_teacher(lesson.teacher)

                db_room = await self.room_repo.get_room_by_name(lesson.room)
                if db_room:
                    new_room = db_room
                else:
                    new_room = await self.room_repo.create_room(lesson.room)
                new_lesson = await self.schedule_repo.create_lesson(lesson.today_date,
                                                  lesson.week_day.strip(),
                                                  lesson.lesson_number,
                                                  lesson.start_time,
                                                  lesson.end_time,
                                                  lesson.subject.subject,
                                                  lesson.subject.subject_type,
                                                  new_teacher.id,
                                                  new_room.id,
                                                  lesson.sub_group,
                                                  lesson.elimination,
                                                  )
                await self.lesson_group_repo.create_lesson_group(new_lesson.id, new_group.id)
        await self.session.commit()



    async def get_schedule(self, group: str, day_command: date)-> str:
        day_today = await self.schedule_repo.get_schedule_by_params(group, day_command)

        if not day_today:
            if await self.group_repo.check_group(group):
                await self.delete_schedule(group)

            await self.save_schedule_into_db(group)
            day_today = await self.schedule_repo.get_schedule_by_params(group, day_command)

        if not day_today:
            return []

        return day_today

    async def delete_schedule(self, group: str)-> None:
        group_obj = await self.group_repo.check_group(group)
        group_id = group_obj.id
        await self.schedule_repo.delete_schedule_by_group(group_id)
        await self.session.commit()