"""Helper module.

Puts together logic for the views.

"""

from flask import jsonify, make_response

from app.api.diary.model import ENTRIES


def response(status, msg, code):
    """This is a general response message function."""
    json_version = jsonify({"status": status, "message": msg, "code": code})
    return make_response(json_version)


def get_all_entries():
    """Returning offers."""
    success = {"status": "successfully returned"}
    json_version = jsonify({"entries": ENTRIES}, {"message": success})
    return make_response(json_version)
