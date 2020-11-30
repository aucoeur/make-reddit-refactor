from app.database import db

posts = [
  {
    'text': 'Look at this cool website!',
    'content': 'Here is some long-form text about this page.',
    'url': 'https://google.com',
    'author': 'meredith',
    'upvotes': ['meredith'],
    'downvotes': [],
  },
  {
    'text': 'Take fun courses online',
    'content': 'Here is some long-form text about this page.',
    'url': 'https://coursera.org',
    'author': 'meredith',
    'upvotes': [],
    'downvotes': [],
  },
  {
    'text': 'Learn Python',
    'content': 'Here is some long-form text about this page.',
    'url': 'https://www.learnpython.org/',
    'author': 'meredith',
    'upvotes': ['meredith'],
    'downvotes': []
  }
]

def reset_db(app):
    ''' Assumes you have imported all your db models already 
    '''

    with app.app_context():
        db.drop_all()
        db.create_all()
    db.session.commit()