from pydantic import BaseModel

class Action(BaseModel):
    review_comment: str
    approve: bool