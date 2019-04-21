from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types.email import EmailType
from sqlalchemy_utils.types.ip_address import IPAddressType


db = SQLAlchemy()


class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer(), primary_key=True)
    ip_address = db.Column(IPAddressType)
    full_name = db.Column(db.String(100),nullable=False)
    choice = db.Column(db.String(10))
    user_email = db.Column(EmailType, unique=True, nullable=False)

    def __init__(self, full_name, user_email):
        self.full_name = full_name
        self.user_email = user_email

    def __repr__(self):
        return '<User %r>' % self.full_name

    def to_dict(self):
        return {
            'IP Address': str(self.ip_address),
            'Full Name': self.full_name,
            'User answers': self.choice,
        }
