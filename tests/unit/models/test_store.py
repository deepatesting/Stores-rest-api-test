from tests.unit.unit_base_test import UnitBaseTest

from models.store import StoreModel

class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel("test_store")

        self.assertEqual(store.name, 'test_store', "Custom Error Msg: Store %s is not equal" % store.name)
