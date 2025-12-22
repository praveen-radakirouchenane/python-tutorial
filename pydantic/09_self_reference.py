from pydantic import BaseModel
from typing import List, Optional

class UserComment(BaseModel):
    id: int
    title: str
    comment: Optional[List['UserComment']] = None

UserComment.model_rebuild() # self reference forwarding 

user_comment = UserComment(
    id=1,
    title="First title",
    comment=[
        UserComment(id=2,title="second comment"),
        UserComment(id=3,title="third comment", comment=[
            UserComment(id=4, title="fourth comment")
        ])
        
    ]
)
