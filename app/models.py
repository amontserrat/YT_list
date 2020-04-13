from app import myDB, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, myDB.Model):
    id = myDB.Column(myDB.Integer, primary_key=True)
    username = myDB.Column(myDB.String(64), index=True, unique=True)
    email = myDB.Column(myDB.String(120), index=True, unique=True)
    password_hash = myDB.Column(myDB.String(128))
    videos = myDB.relationship('Video', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
    	self.password_hash = generate_password_hash(password)

    def check_password(self, password):
    	return check_password_hash(self.password_hash, password)


class Video(myDB.Model):
    id = myDB.Column(myDB.Integer, primary_key=True)
    video_url = myDB.Column(myDB.String(150))
    video_name = myDB.Column(myDB.String(20))
    timestamp = myDB.Column(myDB.DateTime, index=True, default=datetime.utcnow)
    user_id = myDB.Column(myDB.Integer, myDB.ForeignKey('user.id'))

    def __repr__(self):
        return '<Video {}>'.format(self.video_name)


#A user loader function. It loads a user given its id
#this is function is used by the Flask-Login extension, so it knows which user is logged-in
@login.user_loader
def load_user(id):
	return User.query.get(int(id))
