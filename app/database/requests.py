from app.database.models import async_session
from app.database.models import User, Ranks, Mirage
from sqlalchemy import select


async def set_user(
    tg_id: int,
    first_name: str,
    last_name: str,
    is_premium: bool,
    is_admin: bool,
) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        f_name = await session.scalar(select(User).where(User.first_name == first_name))
        l_name = await session.scalar(select(User).where(User.last_name == last_name))
        premium = await session.scalar(select(User).where(User.is_premium == is_premium))
        admin = await session.scalar(select(User).where(User.is_admin == is_admin))

        if not user:
            session.add(
                User(
                    tg_id=tg_id,
                    first_name=first_name,
                    last_name=last_name,
                    is_premium=is_premium,
                    is_admin=is_admin,
                )
            )
            await session.commit()

        # if not f_name or not l_name or not premium or not admin:
        #     session.query(User).filter(User.tg_id == tg_id).update(
        #         {
        #             User.first_name: first_name,
        #             User.last_name: last_name,
        #             User.is_premium: is_premium,
        #             User.is_admin: is_admin,
        #         }
        #     )
        #     await session.commit()


async def get_rank(id):
    async with async_session() as session:
        return await session.scalar(select(Ranks.link).where(Ranks.id == id))

async def get_user_rank(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User.is_admin).where(User.tg_id == tg_id))

async def get_mirage_links(id):
    async with async_session() as session:
        return await session.scalar(select(Mirage.link).where(Mirage.id == id))