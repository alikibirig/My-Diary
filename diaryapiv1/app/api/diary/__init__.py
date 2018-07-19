"""
Inittialize.

Connection endpoints in this file.

"""
from flask import Blueprint

from flask_restful import Api

from app.api.diary.views import GetEntries, GetSingleEntry, AddEntry

entries = Blueprint("entries", __name__)


api = Api(entries)

api.add_resource(GetEntries, '/api/v1/entries')
api.add_resource(GetSingleEntry, '/api/v1/entries/<entry_id>')
api.add_resource(AddEntry, '/api/v1/entries')
