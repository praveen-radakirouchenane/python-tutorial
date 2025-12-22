from pydantic import BaseModel, ConfigDict
from typing import List,Optional
from datetime import datetime


class AddressInfo(BaseModel):
    street: str
    city: str
    state:str 

class UserInfo(BaseModel):
    name: str
    address: AddressInfo
    id: int
    createdAt: datetime

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user_info = UserInfo(
    name="pk",
    address= AddressInfo(
        street="George st",
        city="perth",
        state="wa"
    ),
    id=101,
    createdAt=datetime(2025,3,5,14,30,0)
)

py_dict = user_info.model_dump()
print(f"Model dump {py_dict}")

print("=="*30)

py_dict_json = user_info.model_dump_json()
print(f"Model dump json {py_dict_json}")