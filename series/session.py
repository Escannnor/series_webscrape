        
from sqlmodel import Session, select
from .db import engine
from .model import Series

def add_series(title, date, season, link, country, image, rating):
    try:
        with Session(engine) as session:
            series = Series(title=title, date=date, season=season, link=link, country=country, image=image, rating=rating)
            session.add(series)
            session.commit()
            return 'Series added to database'
    except Exception as e:
        return f'Error in adding series: {e}'

def get_series():
    try:
        with Session(engine) as session:
            series_stmt = select(Series)
            results = session.exec(series_stmt).all()
            return results
    except Exception as e:
        return f'Error in retrieving series: {e}'

def update_series(id, title=None, date=None, season=None, link=None, country=None, image=None, rating=None):
    try:
        with Session(engine) as session:
            series = session.get(Series, id)
            if series:
                if title is not None:
                    series.title = title
                if date is not None:
                    series.date = date
                if season is not None:
                    series.season = season
                if link is not None:
                    series.link = link
                if country is not None:
                    series.country = country
                if image is not None:
                    series.image = image
                if rating is not None:
                    series.rating = rating
                session.commit()
                return f'Series with id {id} updated'
            else:
                return f'No series found with id {id}'
    except Exception as e:
        return f'Error in updating series: {e}'

def delete_series(id):
    try:
        with Session(engine) as session:
            series = session.get(Series, id)
            if series:
                session.delete(series)
                session.commit()
                return f'Series with id {id} deleted'
            else:
                return f'No series found with id {id}'
    except Exception as e:
        return f'Error in deleting series: {e}'
