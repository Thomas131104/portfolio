from pydantic import BaseModel

class MailBase(BaseModel):
    name: str
    email: str
    content: str
    method: str   # "email" hoặc "outlook"

class MailCreate(MailBase):
    pass

class MailRead(MailBase):
    id: int

    class Config:
        from_attributes = True
