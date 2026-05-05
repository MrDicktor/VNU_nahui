from fastapi import FastAPI, Depends
from datetime import date

from sqlalchemy.ext.asyncio import async_sessionmaker

from schedule_bot.constants import TelegramBotConstants
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from schedule_bot.schemas import DBSchedule
from schedule_bot.schedule_services import ScheduleService
from redis.asyncio import Redis
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

engine = create_async_engine(TelegramBotConstants.DATABASE_URL, echo=True)
session_factory = async_sessionmaker(engine, expire_on_commit=False)
redis_client = Redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)


async def get_session() -> AsyncSession:
    async with session_factory() as session:
        yield session

async def get_redis() -> Redis:
    yield redis_client

@app.get("/schedule", response_model=list[DBSchedule])
async def get_schedule(
    group: str, target_date: date, session: AsyncSession = Depends(get_session), redis_client: Redis = Depends(get_redis)
) -> list[DBSchedule]:
    services = ScheduleService(session, redis_client)
    schedule = await services.get_schedule(group, target_date)
    return schedule
