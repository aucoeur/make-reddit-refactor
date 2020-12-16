from datetime import datetime
from app.database import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    url = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # upvotes = db.relationship('')
    # downvotes = db.relationship('')

    def __repr__(self):
        return f'<Entry {self.title}>'
