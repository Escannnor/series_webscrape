from pydantic import BaseModel

class Series(BaseModel):
    title : str
    date : str
    season : int
    link : str
    image: str
    rating: str
    
  
