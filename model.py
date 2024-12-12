from Flask_DB_SQLalchemy import db
from flask_login import UserMixin


class person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'{self.pid} --> Person with name {self.name}, age {self.age}, and job {self.job}'

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    pasword = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self) -> str:
        return f'<User : {self.username}, Role: {self.role}>'
    
    def get_id(self):
        return self.uid