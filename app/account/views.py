from flask import Blueprint, flash, redirect, render_template, url_for
from .forms import LoginForm

account = Blueprint('account', __name__)

@account.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Log in existing user
    '''
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)