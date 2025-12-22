from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    work_status: bool

user_details = {
    'id': 111,
    'name': "Pk",
    'work_status': True
}

user_obj = User(**user_details)
print(f"User details are follows: {user_obj}")