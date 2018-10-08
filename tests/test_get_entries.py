import json
import unittest

from app.get_entries import app
from flask import Flask, request


class TestEntries(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_get_entries(self):
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test_cannot_get_non_existing(self):
        response = self.client.get('/api/v1/entries/3')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
