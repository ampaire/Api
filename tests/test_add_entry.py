import json
import unittest

from app.add_entry import app
from flask import Flask, request


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_add_entry(self):
        response = self.client.post("/api/v1/entries",
                                    data=json.dumps(
                                        {
                                            'Topic': 'When I could take it no more',
                                            'Content': 'I stopped taking it'
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_both_required_fields_can_take_int(self):

        response = self.client.post("/api/v1/entries",
                                    data=json.dumps(
                                        {
                                            'Topic': 'When I could take it no more',
                                            'Content': 123
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_can_add_item_with_missing_Topic(self):
        response = self.client.post("/api/v1/entries",
                                    data=json.dumps(
                                        {
                                            'Topic':'' ,
                                            'Content': 123
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code ,200)

    def test_cannot_add_empty_entry(self):
        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
