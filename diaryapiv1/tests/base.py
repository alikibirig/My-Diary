
import unittest
from app import app
from app.config import app_config


class BaseTestCase(unittest.TestCase):
    """Class for  testing all endpoints."""

    def create_app(self):
        """This method is called first."""
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        """This method is for setting up."""
        self.client = app.test_client(self)
        app.config.from_object(app_config["testing"])

    def tearDown(self):
        """This method is called last."""

    def get_all_entries(self):
        """Get all entry test case."""
        return self.client.get('/api/v1/entries',
                               content_type='application/json')