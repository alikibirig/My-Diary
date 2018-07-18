"""All Endpoints reside here."""
from flask import Flask, request

from flask_restful import Resource

from app.api.diary.helper import get_all_entries

app = Flask(__name__)


class GetEntries(Resource):
    """Class  getting many offers."""

    def get(self):
        """entries are returned here."""
        return get_all_entries()