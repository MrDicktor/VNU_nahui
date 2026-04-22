from fastapi import FastAPI
from datetime import date

from sqlalchemy.ext.asyncio import async_sessionmaker

from schedule_bot.constants import TelegramBotConstants
from sqlalchemy.ext.asyncio.engine import create_async_engine

from schedule_bot.services import Services


app = FastAPI()

engine = create_async_engine(TelegramBotConstants.DATABASE_URL, echo=True)
session_factory = async_sessionmaker(engine, expire_on_commit=False)

@app.get("/schedule")
async def get_schedule(group: str, target_date: date):
    async  with session_factory() as session:
        services = Services(session)
        schedule = await services.get_schedule(group, target_date)
        return schedule