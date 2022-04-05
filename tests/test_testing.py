import ddt
from unittest import TestCase
from helloworld.helpers import add_it, sub_it


class TestTesting(TestCase):
    def test_helpers(self):
        assert add_it(3, 4) == 7

    def test_helpers2(self):
        assert sub_it(3, 4) == -1
