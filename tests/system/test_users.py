import json

from models.users import UserModel
from tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_register_user(self):
        # with app.test_client() as client:
        with self.app() as client:
            with self.app_context():
                response = client.post("/register", data={'username': 'test_user', 'password': '1234'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test_user'))
                self.assertDictEqual(json.loads(response.data), {'message': "User created successfully."})


    def test_register_and_login(self):
        # with app.test_client() as client:
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={'username': 'test_user', 'password': '1234'})
                auth_response = client.post("/auth",
                                            data=json.dumps({'username': 'test_user', 'password': '1234'}),
                                            headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())    # ['access_token']


    def test_register_duplicate_user(self):
        # with app.test_client() as client:
        with self.app() as client:
            with self.app_context():
                client.post("/register", data={'username': 'test_user', 'password': '1234'})
                response = client.post("/register", data={'username': 'test_user', 'password': '1234'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(json.loads(response.data), {'message': 'A user with that username already exists'})
