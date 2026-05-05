import json
from datetime import date, datetime, timedelta

from redis.asyncio import Redis

from schedule_bot.schemas import DBSchedule


class CacheScheduleRepo:

    CACHE_KEY_FORMAT = "{university}:{group_name}:{day_date}"

    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def get_cache_schedule(self, group_name: str, day_date:date)-> list[DBSchedule] | None:
        cache_key = self.CACHE_KEY_FORMAT.format(university="vnu",
                                                 group_name=group_name.lower(),
                                                 day_date=day_date.strftime("%Y-%m-%d"))
        cache_data = await self.redis_client.get(cache_key)
        if cache_data:
            data_dict = json.loads(cache_data)
            return [DBSchedule.model_validate(data) for data in data_dict]
        else:
            return None

    async def set_cache_schedule(self, group_name:str, day_date:date, day_schedule: list[DBSchedule])->None:
        #хай поки так буде якшо добавляться університети тоді поміняю
        cache_key = self.CACHE_KEY_FORMAT.format(university = "vnu",
                                                 group_name =group_name.lower(),
                                                 day_date =day_date.strftime("%Y-%m-%d"))
        now = datetime.now()
        midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        seconds_left = int((midnight - now).total_seconds())
        json_data = json.dumps([obj.model_dump(mode='json') for obj in day_schedule])
        await self.redis_client.set(cache_key, json_data, seconds_left)

    async def clear_group_cache(self, group: str):
        pattern = f"{group.lower()}:*"
        async for key in self.redis_client.scan_iter(match=pattern):
            await self.redis_client.delete(key)