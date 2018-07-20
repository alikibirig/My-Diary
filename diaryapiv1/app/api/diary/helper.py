"""Helper module.

Puts together logic for the views.

"""

from flask import jsonify, make_response, request

from app.api.diary.model import ENTRIES


def response(status, msg):
    """This is a general response message function."""
    json_version = jsonify({"status": status, "message": msg})
    return make_response(json_version)


def get_all_entries():
    """Returning entries."""
    success = {"status": "successfully returned"}
    json_version = jsonify({"entries": ENTRIES}, {"message": success})
    return make_response(json_version)


def get_single_entry(entry_id):
    """Return single entry."""
    for content in ENTRIES:
        if content['id'] == int(entry_id.strip()):
            success = {"status": "successfully returned"}
            json_version = jsonify({"entry": content}, {"status": success})
            return make_response(json_version)
    return response("Invalid", "No such entry")


def store_entry():
    """Adds an entry."""
    data = request.get_json()
    ENTRIES.append(data)
    return response("success", "successfully stored")


def edit_entry(entry_id):
    count = 0
    data = request.get_json()
    for cont in ENTRIES:
        if cont['id'] == int(entry_id.strip()):
            del ENTRIES[count]
            ENTRIES.append(data)
            return response("success", "successfully edited..")
        count = count + 1
