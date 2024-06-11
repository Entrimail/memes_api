from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class Meme(Base):
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=True)
    image_url = mapped_column(String())
