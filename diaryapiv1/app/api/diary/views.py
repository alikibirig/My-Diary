"""All Endpoints reside here."""
from flask import Flask, request

from flask_restful import Resource

from app.api.diary.helper import get_all_entries, get_single_entry, response, \
store_entry

app = Flask(__name__)


class GetEntries(Resource):
    """Class  getting many offers."""

    def get(self):
        """entries are returned here."""
        return get_all_entries()


class GetSingleEntry(Resource):
    """Class  getting singel entry."""

    def get(self, entry_id):
        """Entry is returned here."""
        try:
            int(entry_id)
        except ValueError:
            return response("Invalid", "Entry does not exist")
        else:
            return get_single_entry(entry_id)


class AddEntry(Resource):
    """class adding an entry"""

    def post(self):
        """entries are returned here."""
        return store_entry()    
