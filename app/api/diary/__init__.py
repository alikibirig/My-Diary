"""
Inittialize.

Connection endpoints in this file.

"""
from flask import Blueprint

from flask_restful import Api

from app.api.diary.views import GetEntries, GetSingleEntry, AddEntry, \
    EditEntry

entries = Blueprint("entries", __name__)


api = Api(entries)

api.add_resource(GetEntries, '/api/v1/entries')
api.add_resource(GetSingleEntry, '/api/v1/entries/<entryid>')
api.add_resource(AddEntry, '/api/v1/entries')
api.add_resource(EditEntry, '/api/v1/entries/<entryid>')
