"""All Endpoints reside here."""
from flask import Flask, request

from flask_restful import Resource

from app.api.diary.helper import get_all_entries, get_single_entry, response, \
store_entry, edit_entry

app = Flask(__name__)


class GetEntries(Resource):
    """Class  getting many offers."""

    def get(self):
        """entries are returned here."""
        return get_all_entries()


class GetSingleEntry(Resource):
    """Class  getting singel entry."""

    def get(self, entryid):
        """Entry is returned here."""
        try:
            int(entryid)
        except ValueError:
            return response("Invalid", "Entry does not exist")
        else:
            return get_single_entry(entryid)


class AddEntry(Resource):
    """class adding an entry"""

    def post(self):
        """entries are returned here."""
        return store_entry()    


class EditEntry(Resource):
    """class adding an entry"""

    def put(self, entryid ):
        """entries are returned here."""
        return edit_entry(entryid)    
