import json
from datetime import date, datetime, timedelta

from redis.asyncio import Redis

from schedule_bot.schemas import DBSchedule


class CacheScheduleRepo:
    def __init__(self, redis_client: Redis):
        self.redis = redis_client

    async def get_cache_schedule(self, group: str, day_command:date)->list[DBSchedule] | None:
        cache_key = f"{group.lower()}:{str(day_command).lower()}"
        cache_data = await self.redis.get(cache_key)
        if cache_data:
            data_dict = json.loads(cache_data)
            print("З КЕША !!!!")
            return [DBSchedule.model_validate(data) for data in data_dict]
        else:
            return None

    async def set_cache_schedule(self, group:str, day_command:date, day_schedule: list[DBSchedule])->None:
        cache_key = f"{group.lower()}:{str(day_command).lower()}"
        now = datetime.now()
        midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        seconds_left = int((midnight - now).total_seconds())
        json_data = json.dumps([obj.model_dump(mode='json') for obj in day_schedule])
        await self.redis.set(cache_key, json_data, seconds_left)

    async def clear_group_cache(self, group: str):
        pattern = f"{group.lower()}:*"
        async for key in self.redis.scan_iter(match=pattern):
            await self.redis.delete(key)