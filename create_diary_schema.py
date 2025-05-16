from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the DiaryEntry table
class DiaryEntry(Base):
    __tablename__ = 'diary_entries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, unique=True, nullable=False)  # Date of the entry
    content = Column(Text, nullable=False)  # Long text for the diary content

# Create the SQLite database and schema
engine = create_engine('sqlite:///diary.db')  # Change the path if needed
Base.metadata.create_all(engine)