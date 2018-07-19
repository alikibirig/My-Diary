"""This modelue holds all the api tests."""

from tests.base import BaseTestCase


class ApiTestCases(BaseTestCase):
    """This class carries out testing."""

    def test_many_entries(self):
        """This method carries out testing for all entries."""

        with self.client:
            reply = self.get_all_entries()
            self.assertEqual(reply.status_code, 200)

    def test_single_entry(self):
        """This method carries out testing for all entries."""

        with self.client:
            reply = self.get_single_entry(1000)
            self.assertEqual(reply.status_code, 200)        

    def test_single_invalid_entry(self):
        """This method carries out testing for all entries."""

        with self.client:
            reply = self.get_single_entry("16")
            self.assertEqual(reply.status_code, 200)                