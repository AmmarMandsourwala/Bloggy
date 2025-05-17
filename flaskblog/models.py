from itsdangerous.jws import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from typing import Optional
from FlaskBlog import db, login_manager, app
from datetime import datetime, timezone
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Creating a class for the database table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # This is a relationship
    posts = db.relationship('Post', backref='author',
                            lazy=True)

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    @classmethod
    def get_reset_token(cls, user_id, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': user_id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            # user_id = s.loads(token)['user_id']
            decoded_data = s.loads(token)
            user_id = s.loads(token)[0].get('user_id')
            # Check if the token is expired
            # Check if the token is expired
            if 'exp' in decoded_data and datetime.now(timezone.utc) > datetime.fromtimestamp(decoded_data['exp'], timezone.utc):
                raise SignatureExpired('Token expired')

        except SignatureExpired:
            print("Token expired")
            return None

        except BadSignature:
            print("Invalid token")
            return None

        except:
            print("Error decoding token")
            return None

        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"