from fastapi import FastAPI, Depends
from datetime import date

from sqlalchemy.ext.asyncio import async_sessionmaker

from schedule_bot.constants import TelegramBotConstants
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from schedule_bot.schemas import DBSchedule
from schedule_bot.schedule_services import ScheduleServices


app = FastAPI()

engine = create_async_engine(TelegramBotConstants.DATABASE_URL, echo=True)
session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def get_session()->AsyncSession:
    async with session_factory() as session:
        yield session

@app.get("/schedule", response_model=list[DBSchedule])
async def get_schedule(group: str, target_date: date, session: AsyncSession = Depends(get_session))-> list[DBSchedule]:
        services = ScheduleServices(session)
        schedule = await services.get_schedule(group, target_date)
        return schedule

