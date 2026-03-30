from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    pr_title: str
    pr_description: str
    code_diff: str
    file_name: str
    previous_comments: List[str]