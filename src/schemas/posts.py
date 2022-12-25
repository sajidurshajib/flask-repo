from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    body: str


class PostIn(PostBase):
    pass


class PostOut(PostBase):
    pass
