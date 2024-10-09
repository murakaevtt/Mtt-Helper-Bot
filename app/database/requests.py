from app.database.models import async_session
from app.database.models import User, CSGO_ranks
from sqlalchemy import select


async def set_user(
    tg_id: int, chat_id: int, first_name: str, last_name: str, is_premium: bool
) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        chat = await session.scalar(select(User).where(User.chat_id == chat_id))
        f_name = await session.scalar(select(User).where(User.first_name == first_name))
        l_name = await session.scalar(select(User).where(User.last_name == last_name))
        premium = await session.scalar(
            select(User).where(User.is_premium == is_premium)
        )

        if not user:
            session.add(
                User(
                    tg_id=tg_id,
                    chat_id=chat_id,
                    first_name=first_name,
                    last_name=last_name,
                    is_premium=is_premium,
                )
            )
            await session.commit()

        if not f_name or not l_name or not premium:
            session.query(User).filter(User.tg_id == tg_id).update(
                {
                    User.first_name: first_name,
                    User.last_name: last_name,
                    User.is_premium: is_premium,
                }
            )
            await session.commit()


async def get_rank(id):
    async with async_session() as session:
        return await session.scalar(select(CSGO_ranks.link).where(CSGO_ranks.id == id))
