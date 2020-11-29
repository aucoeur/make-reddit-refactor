from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    username = '' #'hunter2'
    return render_template('index.html', username=username)