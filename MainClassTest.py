import pytest
from MainClass import MainClass

class TestMainClass:
    expected_value_test_1 = 14
    expected_value_test_2 = 45
    mc = MainClass()


    def test_get_local_number(self):
        assert self.mc.get_local_number() == self.expected_value_test_1, "getLocalNumber return not 14"

    def test_get_class_number(self):
        assert self.mc.get_class_number() > self.expected_value_test_2, "getClassNumber return less than 45"