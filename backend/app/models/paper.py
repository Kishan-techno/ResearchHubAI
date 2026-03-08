from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    abstract = Column(Text, nullable=False)
    embedding = Column(Text, nullable=True)