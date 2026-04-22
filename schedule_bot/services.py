#from sqlalchemy.ext.asyncio import async_session
from datetime import date

from schedule_bot.parser import Parser
from schedule_bot.repositories import GroupRepo, TeacherRepo, RoomRepo, ScheduleRepo, LessonGroupRepo, UsersRepo
from schedule_bot.constants import ServiceConstants

class Services:
    def __init__(self, session):
        self.session = session
        self.group_repo = GroupRepo(session=session)
        self.teacher_repo = TeacherRepo(session=session)
        self.room_repo = RoomRepo(session=session)
        self.lesson_group_repo = LessonGroupRepo(session=session)
        self.schedule_repo = ScheduleRepo(session=session)
        self.user_repo = UsersRepo(session=session)
        self.parser = Parser()

    async def save_schedule_into_db(self, group: str):
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

                db_teacher = await self.teacher_repo.check_teacher(lesson.teacher)
                if db_teacher:
                    new_teacher = db_teacher
                else:
                    new_teacher =await self.teacher_repo.create_teacher(lesson.teacher)

                db_room = await self.room_repo.check_room(lesson.room)
                if db_room:
                    new_room = db_room
                else:
                    new_room = await self.room_repo.create_room(lesson.room)
                print(lesson.week_day)
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
            if not self.group_repo.check_group(group):
                await self.delete_schedule(group)

            await self.save_schedule_into_db(group)
            day_today = await self.schedule_repo.get_schedule_by_params(group, day_command)

        if not day_today:
            return []

        return day_today

    async def beautiful_message(self, group: str, day_command: date)-> str:
        day_schedule = await self.get_schedule(group, day_command)
        if not day_schedule:
            return "Вихідний"
        else:
            message: str = ""
            message += f"{day_schedule[0].date.strftime("%d.%m.%Y")} {ServiceConstants.DB_TO_UKR.get(day_schedule[0].week_day)}\n\n"
            for lesson in day_schedule:
                message += f"{lesson.lesson_number}\ufe0f\u20e3 {lesson.start_time.strftime('%H:%M')}—{lesson.end_time.strftime('%H:%M')}\n"
                message += f"📚{lesson.subject}{lesson.subject_type}\n"
                message += f"👨‍🏫{lesson.teacher_name}\n"
                message += f"🏫{lesson.room_name}\n"
                if lesson.sub_group:
                    message += f"{lesson.sub_group}\n"
                if lesson.group_name:
                    message += f"🥷{lesson.group_name}\n"
                # if lesson.elimination:
                #     message += f"{lesson.elimination}\n"
                message += "\n"
            return message



    async def new_user(self, user_info, group):
        if not await self.group_repo.check_group(group):
            await self.save_schedule_into_db(group)
        user_id = str(user_info.id)
        user_fullname = user_info.full_name
        username = user_info.username
        await self.user_repo.create_user(username,user_id, user_fullname, group)


    async def user_exists(self, telegram_id):
        return await self.user_repo.exist_user(telegram_id)



    async def delete_schedule(self, group):
        group_obj = await self.group_repo.check_group(group)
        group_id = group_obj.id
        await self.schedule_repo.delete_schedule_by_group(group_id)
        await self.session.commit()