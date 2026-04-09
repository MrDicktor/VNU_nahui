from sqlalchemy import select

class BaseAlchemyRepo:
    def __init__(self, session):
        self.session = session
        self.model = None

    async def delete(self, obj_id: int):
        query = select(self.model).where(self.model.id == obj_id)
        result = await self.session.execute(query)
        db_obj = result.scalar_one_or_none()

        if db_obj:
            await self.session.delete(db_obj)
            await self.session.commit()
            return True
        return False

    async def get(self, obj_id: int):
        query = select(self.model).where(self.model.id == obj_id) #noqa
        result = await self.session.execute(query)
        db_obj = result.scalar_one_or_none()

        return db_obj

    async def update(self, obj_id: int, **kwargs):
        query = select(self.model).where(self.model.id == obj_id)
        result = await self.session.execute(query)
        db_obj = result.scalar_one_or_none()
        if not db_obj:
            return None
        for key, value in kwargs.items():
            if hasattr(db_obj, key):
                setattr(db_obj, key, value)

        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj