from pydantic import BaseModel


class MemeBaseSchema(BaseModel):
    id: int
    title: str
    description: str | None = None
    image_url: str | None = None


class MemeCreateSchema(BaseModel):
    title: str
    description: str | None = None
    image_url: str


class MemeUpdateSchema(MemeCreateSchema):
    pass
