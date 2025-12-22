from pydantic import BaseModel
from typing import List, Optional, Union

class AddressInfo(BaseModel):
    street: str
    city: str
    state:str 

class CompanyInfo(BaseModel):
    name: str
    address: Optional[AddressInfo] = None
    id: int

class UserInfo(BaseModel):
    name: str
    company: Optional[CompanyInfo] = None

 ## Mixed Data type   

class TextContent(BaseModel):
    type:str = "Text"

class ImageContent(BaseModel):
    type:str = "Image"

class Articles(BaseModel):
    text: List[Union[TextContent,ImageContent]]
