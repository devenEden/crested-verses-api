from flask import Blueprint, render_template, request, jsonify
from app.database.models import Poem
from datetime import date, timedelta
from app.utils.response_utils import custom_response
from app.utils.generate_poem import generate_poem

home_bp = Blueprint('home', __name__)

@home_bp.route('/api/poems', methods=['GET'])
def index():
    today = date.today()
    poem = Poem.query.filter(Poem.date == today).first()

    if (not poem):
        generate_poem()

    return jsonify(
        custom_response(
            status='Success',
            data=poem.serialize if poem else {},
            message="Successfully loaded todays poems",
            status_code=200)
        )
