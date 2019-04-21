from flask import Blueprint, render_template, flash, request, redirect, url_for,json

from CervisoftTask.extensions import cache
from CervisoftTask.forms import SurveyForm
from CervisoftTask.models import Email,db

main = Blueprint('main', __name__)


@main.route('/home')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/")
def emails_api():
    request_email = request.args.get('email')
    api_email= Email.query.filter_by(user_email=request_email).first_or_404()
    return json.jsonify(api_email.to_dict())


@main.route("/form/<int:id>",methods=['GET', 'POST'])
def form(id):
    form = SurveyForm(request.form)
    ip = request.remote_addr
    if request.method == 'POST' and form.validate():
        contact = Email.query.get(id)
        contact.full_name = form.full_name.data
        contact.choice = form.choice.data
        contact.ip_address = ip
        db.session.commit()
        flash('Thanks for Taking the survey')
        return redirect(url_for('.home'))
    return render_template("survey.html", form=form)

