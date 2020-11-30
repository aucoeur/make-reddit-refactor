from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app.database import db
from app.models import Entry
from .forms import EntryForm

entry = Blueprint('entry', __name__)

@entry.route('/new', methods=['GET', 'POST'])
@login_required
def create_new():
    if not current_user.is_authenticated:
        return redirect(url_for('account.login'))
    form = EntryForm()
    if form.validate_on_submit():
        flash('Entry posted')
        return redirect(url_for('main.index'))
    return render_template('entry_new.html', form=form)