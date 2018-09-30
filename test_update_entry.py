import unittest
# import flask_testing
from flask import Flask
import json

from update_an_entry import app

print(app)


class Testupdates(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        # self.client.testing = True

    def test_updateentry(self):
        response = self.client.put("/api/v1/entries/1",data=json.dumps({'topic':'matthew is awesome',
        'content':'and single'}),content_type='application/JSON' )

        self.assertEqual(response.status_code, 200)

    def test_assert_200(self):
        response = self.client.put("/api/v1/entries/1",data=json.dumps({'topic':'matthew is awesome',
        'content':'and single'}),content_type='application/JSON' )
        self.assertEqual(response.status_code, 200)

    def test_update(self):
    
           
        response = self.client.put('/api/v1/entries/1',
                                   data=json.dumps({"Topic": "Not today", "Contents": "But wny?"}),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
       

    def test_cannot_update_nonexisting_item(self):

        response = self.client.get('/api/v1/entries/4')
        self.assertEqual(response.status_code, 405)
        
    
    def test_fields_can_take_int(self):
        entry = [
            {
                "Topic": "Not today",
                "Contents": "But wny?"
            }]
        response = self.client.put('/api/v1/entries/1',
                                   data=json.dumps({"Topic":123, "Contents": "the day"}),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_invalid_JSON(self):
        response = self.client.post('/api/v1/entries/1',
                                    data="not a json",
                                    content_type='application/json')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
