from sqlalchemy import Column, Integer
from database import Base

class Count(Base):
    __tablename__ = "count"

    id = Column(Integer, primary_key=True)
    value = Column(Integer)