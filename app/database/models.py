from . import db
from datetime import datetime

class Poem (db.Model):
    __tablename__ = 'poems'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(200), nullable =False)
    date = db.Column(db.Date(), nullable=False)
    title = db.Column(db.String(255), nullable =False)
    brief_summary = db.Column(db.Text, nullable =False)
    piece = db.Column(db.Text, nullable =False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<Poem {self.id} {self.date} {self.title} >'
    
    @property
    def serialize (self):
        return {
            "id": self.id,
            "source": self.source,
            "date": self.date.isoformat() if self.date else None,
            "title": self.title,
            "brief_summary": self.brief_summary,
            "piece": self.piece,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }