from flask import Blueprint

quest_bp = Blueprint("quest", __name__)

from . import routes