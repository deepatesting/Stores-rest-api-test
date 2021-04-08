import json

from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store(self):
        # with app.test_client() as client:
        with self.app() as client:
            with self.app_context():
                response = client.post("/store/test_store")

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test_store'))
                self.assertDictEqual({'id': 1, 'name': 'test_store', 'items': []}, json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post("/store/test_store")
                response = client.post("/store/test_store")

                self.assertEqual(response.status_code, 400)

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                response = client.delete("/store/test_store")

                self.assertEqual(response.status_code, 200)

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():

                StoreModel("test_store").save_to_db()
                response = client.get("/store/test_store")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'id': 1, 'name': 'test_store', 'items': []}, json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():

                response = client.get("/store/test_store")

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():

                StoreModel("test_store").save_to_db()
                ItemModel("test_item", '19.35', 1).save_to_db()

                response = client.get("/store/test_store")

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'id': 1, 'name': 'test_store', 'items': [{'name':'test_item', 'price': 19.35}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                StoreModel("test_store2").save_to_db()

                response = client.get("/stores")

                self.assertDictEqual({'stores' : [{'id': 1, 'name': 'test_store', 'items': []},
                                                  {'id': 2, 'name': 'test_store2', 'items': []},
                                                ]
                                      },
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test_store").save_to_db()
                ItemModel("test_item", '19.35', 1).save_to_db()

                response = client.get("/stores")

                self.assertDictEqual({'stores': [{'id': 1, 'name': 'test_store', 'items': [{'name':'test_item', 'price': 19.35}]
                                                  }
                                                ]
                                      },
                                    json.loads(response.data))
