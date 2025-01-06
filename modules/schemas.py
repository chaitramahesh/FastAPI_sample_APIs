from pydantic import BaseModel  
from typing import Optional

# Base Schema
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool

# Schema for creating an item
class ItemCreate(ItemBase):
    pass

# Schema for response
class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
