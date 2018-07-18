"""This modelue holds all the api tests."""

from tests.base import BaseTestCase


class ApiTestCases(BaseTestCase):
    """This class carries out testing."""

    def test_many_entries(self):
        """This method carries out testing for all entries."""

        with self.client:
            reply = self.get_all_entries()
            self.assertEqual(reply.status_code, 200)