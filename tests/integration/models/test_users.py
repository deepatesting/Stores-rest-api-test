from pythonProject.starter_code.models.users import UserModel
from pythonProject.starter_code.tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test_user', 'abcd')


            self.assertIsNone(UserModel.find_by_username('test_user'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test_user'))
            self.assertIsNotNone(UserModel.find_by_id(1))
