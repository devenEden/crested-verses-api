import os
from .openaiApi import create_poem
from .website import get_news_details
from app.database.models import Poem
from datetime import date
from app.database import db

site_url = os.getenv('SITE_TO_SCRAPE')


def generate_poem():
    today = date.today()
    poems = Poem.query.filter(Poem.date == today).all()

    if (len(poems) == 0):
        content = get_news_details(site_url)
        piece = create_poem(content, site_url)

        poem = Poem(
            source=site_url,
            date=today,
            title=piece['title'],
            brief_summary=piece["brief_summary"],
            piece=piece['poem']
        )

        db.session.add(poem)
        db.session.commit()


