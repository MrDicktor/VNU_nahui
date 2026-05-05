from schedule_bot.repositories.base_alchemy import BaseAlchemyRepo
from schedule_bot.db_models import Users
from sqlalchemy import select
from redis.asyncio import Redis



class UsersRepo(BaseAlchemyRepo):

    def __init__(self, session) -> None:
        super().__init__(session)
        self.model = Users

    async def create_user(
        self,
        telegram_username: str,
        telegram_id: str,
        telegram_fullname,
        user_group: str,
    ) -> Users:
        new_user = Users(
            telegram_id=telegram_id,
            telegram_username=telegram_username,
            telegram_fullname=telegram_fullname,
            user_group=user_group,
        )
        self.session.add(new_user)
        await self.session.commit()

        return new_user

    async def get_group_by_telegram_id(self, telegram_id: int) -> str:
        query = select(Users).where(Users.telegram_id == telegram_id)
        group = await self.session.execute(query)
        group = group.scalar_one_or_none()
        return group.user_group

    async def get_user_by_telegram_id(self, id: str) -> Users | None:
        query = select(Users).where(Users.telegram_id == id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()
        return result


class CacheUserRepo:
    CACHE_KEY_FORMAT = "{user}"

    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def get_cache_user(self, telegram_id: str) -> str:
        cache_key = self.CACHE_KEY_FORMAT.format(user=telegram_id)
        cache_data = await self.redis_client.get(cache_key)
        if cache_data:
            return cache_data
        else:
            return None

    async def set_cache_user(self, telegram_id: str, group_name: str) -> None:
        cache_key = self.CACHE_KEY_FORMAT.format(user=telegram_id)
        await self.redis_client.set(cache_key, group_name, 3600)

    async def clear_group_cache(self, telegram_id: str):
        pattern = f"{telegram_id}:*"
        async for key in self.redis_client.scan_iter(match=pattern):
            await self.redis_client.delete(key)