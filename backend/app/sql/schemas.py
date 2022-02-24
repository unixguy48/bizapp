from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class UserCrate(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True