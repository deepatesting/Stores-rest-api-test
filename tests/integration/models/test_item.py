from pythonProject.starter_code.models.item import ItemModel
from pythonProject.starter_code.models.store import StoreModel
from pythonProject.starter_code.tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            """ Create ItemModel, check it doesnt exist in database then save it and check if exists, then delete it. 
                Check again item doesnt exist in database."""
            StoreModel('Test_Store').save_to_db()
            item = ItemModel("test", 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item exist with {item.name} name, but expected not to..")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test_Store')
            #store2 = StoreModel('Test_Store2')

            item = ItemModel("test", 19.99, 1)

            store.save_to_db()
            #store2.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'Test_Store')


