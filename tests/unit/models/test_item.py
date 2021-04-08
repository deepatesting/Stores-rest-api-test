from tests.unit.unit_base_test import UnitBaseTest

from models.item import ItemModel

class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel("test", 19.99, 1)

        self.assertEqual(item.name, 'test', "Custom Error Msg: Item %s is not equal" % item.name)
        self.assertEqual(item.price, 19.99)

        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel("test", 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }
        self.assertEqual(item.json(), expected, "Custom Error Msg: JSON export is not equal")
