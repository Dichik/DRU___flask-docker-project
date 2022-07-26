from sqlalchemy import Column

from core import db

# Table name -> 'association'
# Columns: 'actor_id' -> db.Integer, db.ForeignKey -> 'actors.id', primary_key = True
#          'movie_id' -> db.Integer, db.ForeignKey -> 'movies.id', primary_key = True
association = db.Table('association',
                       db.Column('actors.id', db.Integer(), db.ForeignKey('actors.id')),
                       db.Column('movies.id', db.Integer(), db.ForeignKey('movies.id')))
