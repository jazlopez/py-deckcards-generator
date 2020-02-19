from os import path, access, R_OK, getcwd
import unittest
from src.repository import Repository
from unittest.mock import MagicMock


class TestRepository(unittest.TestCase):

    """
    """

    repo = None

    def setUp(self) -> None:

        self.repo = Repository(path.join(getcwd(),"..", "sample", "repository.txt"))
        self.item = Repository.Item()

    def test_path_not_empty(self):

        self.assertIsNotNone(self.repo.path)

    def test_path_readable(self):

        self.assertTrue(path.exists(self.repo.path))
        self.assertTrue(access(self.repo.path, R_OK))

    def test_read_find_content(self):

        self.assertGreater(len(self.repo.read()), 0)

    def test_load_not_empty(self):

        self.assertIsNotNone(self.repo.load())

    def test_load_is_list_with_elements(self):

        self.assertGreater(len(self.repo.load()), 0)

    def test_load_is_list_with_term_definition_items(self):

        for item in self.repo.load():

            self.assertIsInstance(item, Repository.Item().__class__)

if __name__ == "__main__":
    unittest.main()




