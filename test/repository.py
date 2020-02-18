import unittest
from src.repository import Repository


class TestRepository(unittest.TestCase):

    """
    """

    repo = None

    def setUp(self) -> None:

        self.repo = Repository("foo")
        self.item = Repository.Item()

    def test_property_path_not_empty(self):

        self.assertIsNotNone(self.repo.path)

    def test_load_not_empty(self):

        self.assertIsNotNone(self.repo.load())

    def test_load_is_list_with_elements(self):

        self.assertGreater(len(self.repo.load()), 0)

    def test_load_is_list_with_term_definition_items(self):

        for i in self.repo.load():

            self.assertIsInstance(i, self.item.__class__)

if __name__ == "__main__":
    unittest.main()




