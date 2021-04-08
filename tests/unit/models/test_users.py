from pythonProject.starter_code.tests.unit.unit_base_test import UnitBaseTest

from pythonProject.starter_code.models.users import UserModel

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("test", 'abcd')

        self.assertEqual(user.username, 'test',)
        self.assertEqual(user.password, 'abcd', )


