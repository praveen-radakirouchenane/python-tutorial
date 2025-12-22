from pydantic import BaseModel


class AddressInfo(BaseModel):
    street: str
    city: str
    state:str 


class UserInfo(BaseModel):
    name: str
    address: AddressInfo
    id: int

address_info = AddressInfo(
    street="george street",
    city="perth",
    state="wa"
)

user_info = UserInfo(
    name="pk",
    address=address_info,
    id=123
)

print(f"User details {user_info}")