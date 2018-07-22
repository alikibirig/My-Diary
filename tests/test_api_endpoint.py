"""This modelue holds all the api tests."""

from tests.base import BaseTestCase


class ApiTestCases(BaseTestCase):
    """This class carries out testing."""


    SAMPLE_ENTRY = {
        "id": 1000,
        "owner_id": 401,
        "entry_category": 2,
        "entry_date": "18/07/2018 10:30pm",
        "due_date": "23/07/2018 10:30pm",
        "entry_content": "flight "}
    
    def test_many_entries(self):
        """This method carries out testing for all entries."""

        with self.client:
            reply = self.get_all_entries()
            self.assertEqual(reply.status_code, 200)

    def test_single_entry(self):
        """This method carries out testing for a single entry."""

        with self.client:
            reply = self.get_single_entry(1000)
            self.assertEqual(reply.status_code, 200)        

    def test_single_invalid_entry(self):
        """This method carries out testing for a single invalid entry."""

        with self.client:
            reply = self.get_single_entry("16")
            self.assertEqual(reply.status_code, 200)                

    def test_create_entry(self):
        """This method carries out testing for storing entries."""

        with self.client:
            val = self.SAMPLE_ENTRY
            reply = self.add_entry(val)
            self.assertEqual(reply.status_code, 200) 

    def test_edit_entry(self):
        """This method carries out testing for editing entries."""
        
        with self.client:
            val = self.SAMPLE_ENTRY
            reply = self.edit_entry(1000, val)
            self.assertEqual(reply.status_code, 200)                  