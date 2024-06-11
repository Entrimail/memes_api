from fastapi import APIRouter, Depends, status
from . import crud
from .schemas import MemeBaseSchema, MemeCreateSchema, MemeUpdateSchema
from .dependencies import meme_by_id
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/memes", tags=["Memes"])


@router.get("/get-all-memes/", response_model=list[MemeBaseSchema])
async def get_memes(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_memes(session=session)


@router.post(
    "/create-meme/", response_model=MemeBaseSchema, status_code=status.HTTP_201_CREATED
)
async def create_meme(
    meme_in: MemeCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_meme(session=session, meme_in=meme_in)


@router.get("/get-meme/{meme_id}/", response_model=MemeBaseSchema)
async def get_meme(meme=Depends(meme_by_id)):
    return meme


@router.put("/update-meme/{meme_id}/")
async def update_meme(
    meme_update: MemeUpdateSchema,
    meme=Depends(meme_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_meme(session=session, meme=meme, meme_update=meme_update)


@router.delete("/delete-meme/{meme_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meme(
    meme: MemeBaseSchema = Depends(meme_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_meme(session=session, meme=meme)
