from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean 
from modules.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2))
    on_offer = Column(Boolean, default=False)
