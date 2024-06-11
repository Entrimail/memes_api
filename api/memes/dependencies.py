from typing import Annotated
from fastapi import Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from . import crud
from core.models import Meme
from core.models.db_helper import db_helper


async def meme_by_id(
    meme_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Meme:
    meme = await crud.get_meme(session=session, meme_id=meme_id)
    if meme:
        return meme
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Meme {meme_id} not found"
    )
