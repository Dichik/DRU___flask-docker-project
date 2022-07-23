from core import db
from sqlalchemy import Table, Column

# Table name -> 'association'
# Columns: 'actor_id' -> db.Integer, db.ForeignKey -> 'actors.id', primary_key = True
#          'movie_id' -> db.Integer, db.ForeignKey -> 'movies.id', primary_key = True
association = Table('association', db.MetaData(),
                    Column('actor_id', db.Integer, db.ForeignKey('Actor.id'), primary_key=True),
                    Column('movie_id', db.Integer, db.ForeignKey('Movie.id'), primary_key=True)
                    )
