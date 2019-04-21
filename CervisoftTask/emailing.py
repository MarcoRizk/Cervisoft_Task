from manage import mail
from flask_mail import Message
from .models import Email
from flask import request
from .settings import MAIL_SETTINGS


with mail.connect() as conn:
    for contact in Email.query.all():
        url = request.url_root + "form/" + str(contact.id)
        html = "<P>Please visit this link<P><a href=%s>link</a>" %url
        sender = ("Cervisoft", MAIL_SETTINGS['mail_username'])
        subject = "Survey For You, %s" % contact.full_name
        msg = Message(recipients=[contact.user_email],
                      html=html,
                      subject=subject,
                      sender=sender)

        conn.send(msg)

