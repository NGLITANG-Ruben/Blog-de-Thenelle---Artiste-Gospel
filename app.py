from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import db, Artist, Achievement, Album, GalleryImage, Video, SocialLink, SongLink
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thenella-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thenella.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def init_database():
    """Initialize database with default data"""
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if Artist.query.first() is not None:
            return
        
        # Add Artist
        artist = Artist(
            name='THENELLA',
            full_name='Bonog Thérèse Ornella',
            bio_en='Thenella, born Bonog Thérèse Ornella, is a Cameroonian gospel singer, songwriter, worship leader, and evangelist. Her spiritual journey began in a Christian family where her father\'s miraculous healing experience profoundly shaped her faith.',
            bio_fr='Thenella, née Bonog Thérèse Ornella, est une chanteuse de gospel, auteure-compositrice, leader de louange et évangéliste camerounaise. Son parcours spirituel a commencé dans une famille chrétienne où l\'expérience de guérison miraculeuse de son père a profondément façonné sa foi.',
            bio2_en='For years, she served as lead vocalist and choir director at various churches, working with gospel groups like No Greater Love Family and Divine Harmonie. In September 2017, she was ordained as an evangelist, expanding her ministry beyond music to include preaching and outreach to vulnerable communities across Africa.',
            bio2_fr='Pendant des années, elle a servi comme vocaliste principale et directrice de chœur dans diverses églises, travaillant avec des groupes gospel comme No Greater Love Family et Divine Harmonie. En septembre 2017, elle a été ordonnée évangéliste, élargissant son ministère au-delà de la musique pour inclure la prédication et le soutien aux communautés vulnérables à travers l\'Afrique.',
            bio3_en='Married to Dr. Philippe Totto Ndong, Thenella continues to minister through her music and gospel outreach from Douala, Cameroon, touching hearts with worship that bridges earthly experiences and divine encounters.',
            bio3_fr='Mariée au Dr. Philippe Totto Ndong, Thenella continue à exercer son ministère à travers sa musique et son évangélisation depuis Douala, Cameroun, touchant les cœurs avec une louange qui relie les expériences terrestres aux rencontres divines.',
            image_url='OIP.webp'
        )
        db.session.add(artist)
        
        # Add Achievements
        achievements = [
            Achievement(icon='fa-trophy', title_en='Revelation of the Year', title_fr='Révélation de l\'Année',
                       description_en='Zamba Awards after the release of "Cœur Nouveau" album',
                       description_fr='Zamba Awards après la sortie de l\'album "Cœur Nouveau"', order=1),
            Achievement(icon='fa-music', title_en='Breakthrough Album', title_fr='Album Révélation',
                       description_en='"Cœur Nouveau" (2019) with 10 inspirational tracks',
                       description_fr='"Cœur Nouveau" (2019) avec 10 titres inspirants', order=2),
            Achievement(icon='fa-hands-praying', title_en='Ordained Evangelist', title_fr='Évangéliste Ordonnée',
                       description_en='Officially ordained in September 2017 for ministry work',
                       description_fr='Ordonnée officiellement en septembre 2017 pour le travail ministériel', order=3),
            Achievement(icon='fa-record-vinyl', title_en='Multiple Albums', title_fr='Plusieurs Albums',
                       description_en='Released several successful albums and singles since 2017',
                       description_fr='Plusieurs albums et singles à succès depuis 2017', order=4)
        ]
        for ach in achievements:
            db.session.add(ach)
        
        # Add Albums
        albums = [
            Album(title='Cœur Nouveau (2019)', image_url='592x592bb.webp',
                 description_en='Breakthrough album with 10 tracks of spiritual transformation',
                 description_fr='Album révélation avec 10 titres de transformation spirituelle',
                 listen_url='https://music.apple.com/us/album/c%C5%93ur-nouveau/1454733587', year=2019, order=1),
            Album(title='Une Autre Dimension (2024)', image_url='592x592bb (1).webp',
                 description_en='Latest album capturing praise, worship, and testimony themes',
                 description_fr='Dernier album capturant des thèmes de louange, d\'adoration et de témoignage',
                 listen_url='https://music.apple.com/sn/album/une-autre-dimension/1786566551', year=2024, order=2),
            Album(title='Je te bénirai (Live) (2024)', image_url='592x592bb (2).webp',
                 description_en='Live single reflecting grateful worship and praise',
                 description_fr='Single en direct reflétant une adoration et une louange reconnaissantes',
                 listen_url='https://music.apple.com/gb/album/je-te-b%C3%A9nirai-live-single/1755108856', year=2024, order=3)
        ]
        for album in albums:
            db.session.add(album)
        
        # Add Gallery Images
        gallery_images = [
            GalleryImage(image_url='OIP.webp', title_en='Ministry & Worship', title_fr='Ministère & Adoration', order=1),
            GalleryImage(image_url='download.webp', title_en='Live Gospel Performances', title_fr='Performances Gospel en Direct', order=2),
            GalleryImage(image_url='OIP (5).webp', title_en='Music Creation Process', title_fr='Processus de Création Musicale', order=3),
            GalleryImage(image_url='OIP (4).webp', title_en='Community Outreach & Evangelism', title_fr='Action Communautaire & Évangélisation', order=4)
        ]
        for img in gallery_images:
            db.session.add(img)
        
        # Add Social Links
        social_links = [
            SocialLink(platform='YouTube', icon_class='fab fa-youtube', url='https://www.youtube.com/results?search_query=Thenella+Officiel', color_class='youtube', order=1),
            SocialLink(platform='TikTok', icon_class='fab fa-tiktok', url='https://www.tiktok.com/search?q=thenella%20gospel&t=1717758924714', color_class='tiktok', order=2),
            SocialLink(platform='Facebook', icon_class='fab fa-facebook', url='https://www.facebook.com/search/top?q=thenella%20gospel', color_class='facebook', order=3),
            SocialLink(platform='Instagram', icon_class='fab fa-instagram', url='https://www.instagram.com/explore/tags/thenella/', color_class='instagram', order=4)
        ]
        for link in social_links:
            db.session.add(link)
        
        # Add Song Links
        song_links = [
            SongLink(platform='youtube', title='Ouvrier de la Moisson', url='https://www.youtube.com/results?search_query=Thenella+Officiel', order=1),
            SongLink(platform='youtube', title='Seigneur Mon Roi', url='https://www.youtube.com/results?search_query=Thenella+Officiel', order=2),
            SongLink(platform='youtube', title='La Gloire de l\'Éternel', url='https://www.youtube.com/results?search_query=Thenella+Officiel', order=3)
        ]
        for link in song_links:
            db.session.add(link)
        
        # Add Videos (pour les clics sur images)
        videos = [
            Video(title='Ouvrier de la Moisson', url='https://www.youtube.com/watch?v=VIDEO_ID_1', thumbnail_url='592x592bb.webp', platform='youtube', order=1),
            Video(title='Une Autre Dimension', url='https://www.youtube.com/watch?v=VIDEO_ID_2', thumbnail_url='592x592bb (1).webp', platform='youtube', order=2),
            Video(title='Je te bénirai', url='https://www.youtube.com/watch?v=VIDEO_ID_3', thumbnail_url='592x592bb (2).webp', platform='youtube', order=3)
        ]
        for video in videos:
            db.session.add(video)
        
        db.session.commit()
        print("Database initialized successfully!")

@app.route('/')
def index():
    artist = Artist.query.first()
    achievements = Achievement.query.order_by(Achievement.order).all()
    albums = Album.query.order_by(Album.order).all()
    gallery_images = GalleryImage.query.order_by(GalleryImage.order).all()
    social_links = SocialLink.query.order_by(SocialLink.order).all()
    song_links = SongLink.query.order_by(SongLink.order).all()
    videos = Video.query.order_by(Video.order).all()
    
    return render_template('index.html', 
                         artist=artist,
                         achievements=achievements,
                         albums=albums,
                         gallery_images=gallery_images,
                         social_links=social_links,
                         song_links=song_links,
                         videos=videos)

@app.route('/video/<int:video_id>')
def watch_video(video_id):
    video = Video.query.get_or_404(video_id)
    return redirect(video.url)

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    data = request.form
    # Here you can add email sending logic or save to database
    return jsonify({'success': True, 'message': 'Booking request received!'})

if __name__ == '__main__':
    init_database()
    app.run(debug=True, port=5000)