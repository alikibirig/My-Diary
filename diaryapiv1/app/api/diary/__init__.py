"""
Inittialize.

Connection endpoints in this file.

"""
from flask import Blueprint

from flask_restful import Api

from app.api.diary.views import GetEntries

entries = Blueprint("entries", __name__)


api = Api(entries)

api.add_resource(GetEntries, '/api/v1/entries')