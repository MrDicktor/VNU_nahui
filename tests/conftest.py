import asyncio
import pytest
import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from schedule_bot.db_models import Base
from dotenv import load_dotenv
load_dotenv()
import os


NAME = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
SERVER = os.getenv('DB_SERVER')
PORT = os.getenv('DB_PORT')


TEST_DB_NAME = f"{NAME}_test"
ASYNC_TEST_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{SERVER}:{PORT}/{TEST_DB_NAME}"



@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_db():
    admin_url = f"postgresql+asyncpg://{USER}:{PASSWORD}@{SERVER}:{PORT}/postgres"
    admin_engine = create_async_engine(admin_url, isolation_level="AUTOCOMMIT")

    async with admin_engine.connect() as conn:
        await conn.execute(text(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)"))
        await conn.execute(text(f"CREATE DATABASE {TEST_DB_NAME}"))
    await admin_engine.dispose()

    test_engine = create_async_engine(ASYNC_TEST_DATABASE_URL)

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await test_engine.dispose()
    admin_engine = create_async_engine(admin_url, isolation_level="AUTOCOMMIT")
    async with admin_engine.connect() as conn:
        await conn.execute(text(f"DROP DATABASE IF EXISTS {TEST_DB_NAME} WITH (FORCE)"))
    await admin_engine.dispose()

@pytest_asyncio.fixture
async def db_session():
    engine = create_async_engine(ASYNC_TEST_DATABASE_URL)
    async with engine.connect() as connection:
        transaction = await connection.begin()

        session_factory = async_sessionmaker(
            bind=connection,
            expire_on_commit=False,
            class_=AsyncSession
        )
        session = session_factory()

        yield session

        await session.close()

        if transaction.is_active:
            await transaction.rollback()

    await engine.dispose()
