import unittest
from app import create_app, db

class UserTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        response = self.client.post('/users', json={'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
