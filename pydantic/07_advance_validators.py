from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class UserInfo(BaseModel):
    f_name: str
    l_name: str
    email: str
    price: str # $5.55
    start_date: datetime
    end_date: datetime


    @field_validator('f_name','l_name')
    def must_be_captilize(cls, v):
        if not v.istitle():
            raise ValueError("Names must me capitalized")
        return v
    
    @field_validator('email')
    def email_normalize(cls, v):
        return v.lower().strip()
    
    @field_validator('price', mode="before")
    def price_validation(cls, v):
        if isinstance(v, str):
            return float(v.replace('$',''))
        
    @model_validator(mode='after')
    def date_time_validator(self):
        if self.start_date >= self.end_date:
            raise ValueError("End date must be greater than start date")
        return self

