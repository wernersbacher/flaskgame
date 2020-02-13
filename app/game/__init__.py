from flask import Blueprint

bp = Blueprint('game', __name__)

from app.game.routes import racing

@bp.route('/test', methods=['GET', 'POST'])
def test():
	return "Test message"
