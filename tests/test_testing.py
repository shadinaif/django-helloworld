import ddt
from unittest import TestCase
from helloworld.helpers import add_it


@ddt.ddt
class TestTesting(TestCase):
    def test_helpers(self):
        assert add_it(3, 4) == 7
