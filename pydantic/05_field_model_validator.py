from pydantic import BaseModel, field_validator, model_validator


class UserInfo(BaseModel):
    name: str

    @field_validator('name')
    def name_length(cls,v):
        if len(v) < 5:
            raise ValueError("Please enter at least 5 characters")
        return v
    
class Registration(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_validation(self):
        if self.password != self.confirm_password:
            raise ValueError("Password doesn't match")
        return self
    
