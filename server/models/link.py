import sqlite3
from db import db

class LinksModel(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    hash = db.Column(db.String(10))
    hits = db.Column(db.Integer)

    #store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #store = db.relationship('StoreModel')

    def __init__(self, url, hits, hash):
        #self.id = _id
        self.url = url
        self.hits = hits
        self.hash = hash

    def json(self):
        return {'url': self.url, 'hash': self.hash, 'hits': self.hits, 'id': self.id}

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_hash(cls, hash):
        return cls.query.filter_by(hash=hash).first()

    @classmethod
    def occupied(cls):
        return cls.query.first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
