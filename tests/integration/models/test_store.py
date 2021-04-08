from pythonProject.starter_code.models.item import ItemModel
from pythonProject.starter_code.models.store import StoreModel
from pythonProject.starter_code.tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel("test_store")

        self.assertListEqual(store.items.all(), [], "The store 's items lenght was not 0 even though no items added.")

    def test_crud(self):
        with self.app_context():
            """ Create ItemModel, check it doesnt exist in database then save it and check if exists, then delete it. 
                Check again item doesnt exist in database."""
            store = StoreModel('Test_Store')

            self.assertIsNone(StoreModel.find_by_name('Test_Store'),
                              f"Found a store exist with {store.name} name, but expected not to..")

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('Test_Store'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('Test_Store'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test_Store')
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('Test_Store')

        expected = {
            'name': 'Test_Store',
            'items': []
        }
        self.assertDictEqual(store.json(), expected, "Custom Error Msg: JSON export is not equal")

    def test_store_json_with_items(self):
        with self.app_context():
            store = StoreModel('Test_Store')
            item = ItemModel("test_item", 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'Test_Store',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }
            self.assertDictEqual(store.json(), expected, "Custom Error Msg: JSON export is not equal")
