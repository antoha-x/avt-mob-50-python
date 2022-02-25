import pytest
from MainClass import get_local_number

class TestMainClass:
    expected_value = 14

    def test_getLocal_number(self):
        assert get_local_number() == self.expected_value, "getLocalNumber return not 14"