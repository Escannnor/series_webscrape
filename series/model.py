from sqlmodel import SQLModel, Field
from .db import create_db_and_tables

class Series(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    title : str | None = Field(max_length=300)
    date : str 
    season : int | None = Field(default=None)
    link : str
    image: str
    rating: str


   
    
    
create_db_and_tables()