from flask import Blueprint, render_template
from flask_login import login_required

from app.database import db
from app.models import Entry

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    # Returns 11 most recent entries in descending order
    entries = Entry.query.order_by(Entry.timestamp.desc()).limit(11).all()

    return render_template('index.html', entries=entries)
