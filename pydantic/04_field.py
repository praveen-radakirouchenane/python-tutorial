from typing import List, Optional
from pydantic import BaseModel, Field 
import re

class User(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Enter your name",
        examples="Praveen Kumar"
    ),
    department: Optional[str] = 'Admin',
    salary: float = Field(
        ...,
        gt=10000,
        ge=200000
    ),
    email: str = Field(...,pattern=r''),
    age: int = Field(
        ...,
        gt=0,
        ge=100,
        description="Age in years"
    ),
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )    
