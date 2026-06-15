from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    bio_en = db.Column(db.Text, nullable=False)
    bio_fr = db.Column(db.Text, nullable=False)
    bio2_en = db.Column(db.Text, nullable=False)
    bio2_fr = db.Column(db.Text, nullable=False)
    bio3_en = db.Column(db.Text, nullable=False)
    bio3_fr = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), default='OIP.webp')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Achievement(db.Model):
    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=False)
    title_en = db.Column(db.String(200), nullable=False)
    title_fr = db.Column(db.String(200), nullable=False)
    description_en = db.Column(db.String(500), nullable=False)
    description_fr = db.Column(db.String(500), nullable=False)
    order = db.Column(db.Integer, default=0)

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    description_en = db.Column(db.String(500), nullable=False)
    description_fr = db.Column(db.String(500), nullable=False)
    listen_url = db.Column(db.String(500), nullable=False)
    year = db.Column(db.Integer)
    order = db.Column(db.Integer, default=0)

class GalleryImage(db.Model):
    __tablename__ = 'gallery'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=False)
    title_en = db.Column(db.String(200), nullable=False)
    title_fr = db.Column(db.String(200), nullable=False)
    order = db.Column(db.Integer, default=0)

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    thumbnail_url = db.Column(db.String(200))
    platform = db.Column(db.String(50), default='youtube')
    order = db.Column(db.Integer, default=0)

class SocialLink(db.Model):
    __tablename__ = 'social_links'
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    icon_class = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    color_class = db.Column(db.String(50))
    order = db.Column(db.Integer, default=0)

class SongLink(db.Model):
    __tablename__ = 'song_links'
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    order = db.Column(db.Integer, default=0)