from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Meme
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import MemeBaseSchema, MemeCreateSchema, MemeUpdateSchema


async def get_memes(session: AsyncSession, skip: int, limit: int) -> list[Meme]:
    stmt = select(Meme).offset(skip).limit(limit).order_by(Meme.id)
    res: Result = await session.execute(stmt)
    memes = res.scalars()
    return list(memes)


async def get_meme(session: AsyncSession, meme_id: int) -> Meme | None:
    return await session.get(Meme, meme_id)


async def create_meme(session: AsyncSession, meme_in: MemeCreateSchema):
    meme = Meme(**meme_in.model_dump())
    session.add(meme)
    await session.commit()
    return meme


async def update_meme(
    session: AsyncSession, meme: Meme, meme_update: MemeUpdateSchema
) -> Meme:
    meme.description = meme_update.description
    meme.image_url = meme_update.image_url
    meme.title = meme_update.title
    await session.commit()
    await session.refresh(meme)
    return meme


async def delete_meme(session: AsyncSession, meme: Meme) -> None:
    await session.delete(meme)
    await session.commit()
    return f"Note {meme.id} has been deleted"
