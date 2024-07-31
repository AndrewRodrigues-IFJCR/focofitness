from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

ENGINE = create_async_engine(
    'postgresql+asyncpg://admin:admin123@127.0.0.1:5432/database'
)


def get_async_session_maker() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(ENGINE, class_=AsyncSession)
