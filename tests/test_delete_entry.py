import json
import unittest

from flask import Flask
from app.deleteentry import app

print(app)


class Testdeletes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_delete(self):
        response = self.client.delete("/api/v1/entries/1")
        self.assertEqual(response.status_code, 200)
        
    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/entries/43")
        self.assertEqual(response.status_code, 404)

if __name__ =="__main__":
    unittest.main()